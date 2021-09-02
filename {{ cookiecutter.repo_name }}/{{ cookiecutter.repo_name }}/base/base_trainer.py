from os.path import join as pjoin
from pathlib import Path
import math

import yaml
import torch

from {{ cookiecutter.repo_name }}.utils import setup_logger, etc_path, trainer_paths, TensorboardWriter


logger = setup_logger(__name__)


class BaseTrainer:
    """
    Base class for all trainers
    """
    def __init__(self, model, optimizer, loss, metrics, start_epoch, config,
                 device):
        self.model = model
        self.optimizer = optimizer
        self.loss = loss
        self.metrics = metrics
        self.start_epoch = start_epoch
        self.config = config
        self.device = device

        self._setup_monitoring(config['training'])

        self.checkpoint_dir, writer_dir = trainer_paths(config)
        self.writer = TensorboardWriter(writer_dir,
                                        config['training']['tensorboard'])

        # Save configuration file into etc directory:
        etc_dir = etc_path(config)
        cfg_filename = config["trial_info"]["ID"] + ".yml"
        config_save_path = pjoin(etc_dir, cfg_filename)
        with open(config_save_path, 'w') as handle:
            yaml.dump(config, handle, default_flow_style=False)


    def train(self):
        """
        Full training logic
        """
        logger.info('Start training...')
        for epoch in range(self.start_epoch, self.epochs):
            result = self._train_epoch(epoch)

            # save logged informations into log dict
            results = {'epoch': epoch}
            for key, value in result.items():
                if key == 'metrics':
                    results.update({
                        mtr.__name__: value[i] for i, mtr in enumerate(self.metrics)})
                elif key == 'val_metrics':
                    results.update({
                        'val_' + mtr.__name__: value[i] for
                        i, mtr in enumerate(self.metrics)
                    })
                else:
                    results[key] = value

            # print logged informations to the screen
            for key, value in results.items():
                logger.info(f'{str(key):15s}: {value}')

            # evaluate model performance according to configured metric,
            # save best checkpoint as model_best
            best = False
            if self.mnt_mode != 'off':
                try:
                    # check whether model performance improved or not, according
                    # to specified metric(mnt_metric)
                    improved = (self.mnt_mode == 'min' and results[self.mnt_metric] < self.mnt_best) or\
                               (self.mnt_mode == 'max' and results[self.mnt_metric] > self.mnt_best)
                except KeyError:
                    logger.warning(f"Warning: Metric '{self.mnt_metric}' is not found. Model "
                                        "performance monitoring is disabled.")
                    self.mnt_mode = 'off'
                    improved = False
                    not_improved_count = 0

                if improved:
                    self.mnt_best = results[self.mnt_metric]
                    not_improved_count = 0
                    best = True
                else:
                    not_improved_count += 1

                if not_improved_count > self.early_stop:
                    logger.info(f"Validation performance didn\'t improve for {self.early_stop} "
                                     "epochs. Training stops.")
                    break

            if epoch % self.save_period == 0:
                self._save_checkpoint(epoch, save_best=best)

    def _train_epoch(self, epoch: int) -> dict:
        """
        Training logic for an epoch.
        """
        raise NotImplementedError

    def _save_checkpoint(self, epoch: int, save_best: bool=False) -> None:
        """
        Saving checkpoints

        :param epoch: current epoch number
        :param log: logging information of the epoch
        :param save_best: if True, rename the saved checkpoint to 'model_best.pth'
        """
        model = type(self.model).__name__
        state = {
            'model': model,
            'epoch': epoch,
            'state_dict': self.model.state_dict(),
            'optimizer': self.optimizer.state_dict(),
            'monitor_best': self.mnt_best,
            'config': self.config
        }
        filename = self.checkpoint_dir / f'ckpt_epoch-{epoch}.pth'
        torch.save(state, filename)
        logger.info(f"Saving checkpoint: {filename} ...")
        if save_best:
            best_path = self.checkpoint_dir / 'model_best.pth'
            torch.save(state, best_path)
            logger.info(f'Saving current best: {best_path}')

    def _setup_monitoring(self, config: dict) -> None:
        """
        Configuration to monitor model performance and save best.
        """
        self.epochs = config['epochs']
        self.save_period = config['save_period']
        self.monitor = config.get('monitor', 'off')
        if self.monitor == 'off':
            self.mnt_mode = 'off'
            self.mnt_best = 0
        else:
            self.mnt_mode, self.mnt_metric = self.monitor.split()
            assert self.mnt_mode in ['min', 'max']
            self.mnt_best = math.inf if self.mnt_mode == 'min' else -math.inf
            self.early_stop = config.get('early_stop', math.inf)


class AverageMeter:
    """
    Computes and stores the average and current value.
    """

    def __init__(self, name):
        self.name = name
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count
