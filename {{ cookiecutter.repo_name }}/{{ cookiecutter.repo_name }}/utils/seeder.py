#!/usr/bin/env python
# coding=utf-8

# Manages Reproducibility

import numpy as np
import random
import torch


def set_seed(logger, seed=None, seed_torch=True, seed_cudnn=False):
    """Set seed of random number generators to limit the number of sources of
    nondeterministic behavior for a specific platform, device, and PyTorch
    release. For more information, see
    https://pytorch.org/docs/stable/notes/randomness.html.

    Parameters
    ----------
    logger : logging.Logger object
    seed : int
        Seed for random number generators.
    seed_torch : bool
        If we will set the seed for torch random number generators.
        Default: True

    Returns
    -------
    seed : int
        Seed used for random number generators
    """
    if seed is None:
        seed_str = "{{ cookiecutter.repo_name }}"
        seed = [str(ord(letter) - 96) for letter in seed_str]
        seed = abs(int(''.join(seed))) % 2 ** 32
        #seed = np.random.choice(2 ** 32)

    # Set python seed for custom operators
    random.seed(seed)

    # Set seed for the global NumPy RNG if any of the libraries rely on NumPy
    np.random.seed(seed)

    if seed_torch:
        # Seed the RNG for all devices (both CPU and CUDA)
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.cuda.manual_seed(seed)
        if seed_cudnn:
            # Set cuDNN to deterministically select a convolution algorithm
            torch.backends.cudnn.benchmark = False
            # Ensure that the cuDNN convolution algorithm is deterministic
            torch.backends.cudnn.deterministic = True

    logger.info(f'Random seed {seed} has been set.')

    return seed


def seed_worker(worker_id, logger):
    """Set seed for Dataloader. DataLoader will reseed workers the "Randomness
    in multi-process data loading" algorithm. Use `worker_init_fn()` to
    preserve reproducibility. For more information, see
    https://pytorch.org/docs/stable/notes/randomness.html.
    """
    worker_seed = torch.initial_seed() % 2**32
    np.random.seed(worker_seed)
    random.seed(worker_seed)
    msg = f"Dataloader worker {worker_id}'s seed {worker_seed} has been set."
    logger.info(msg)

def get_generator(logger, seed=0):
    """Set seed for Dataloader generators. DataLoader will reseed workers the
    "Randomness in multi-process data loading" algorithm. Use `generator` to
    preserve reproducibility. For more information, see
    https://pytorch.org/docs/stable/notes/randomness.html.

    Parameters
    ----------
    logger : logging.Logger object
    seed : int
        Seed for random number generators.
        Default: 0

    Returns
    -------
    generator : torch.Generator
        Seeded torch generator
    """
    generator = torch.Generator()
    generator.manual_seed(seed)

    msg = f"Dataloader generator with seed {worker_seed} has been created."
    logger.info(msg)

    return generator


def get_device(target_devices, logger):
    """
    Setup device: GPU if available, else CPU.

    Parameters
    ----------
    target_devices : list of device IDs
    logger : logging.Logger object

    Returns
    -------
    device: list[int]
        A list of device pointers to be used

    """
    available_devices = list(range(torch.cuda.device_count()))

    if not available_devices:
        msg = ("There is no GPU available on this machine. "
               "Training will be performed on CPU.")
        logger.warning(msg)
        device = torch.device('cpu')
        return device

    max_target_gpu = max(target_devices)
    max_available_gpu = max(available_devices)

    if max_target_gpu > max_available_gpu:
        msg = (f"Configuration requestes GPU #{max_target_gpu} "
               "but only {max_available_gpu} available. "
               "Check the configuration and try agaion.")
        logger.critical(msg)
        raise Exception(msg)

    msg = (f"Using devices {target_devices} of "
           "available devices {available_devices}")
    logger.info(msg)
    device = torch.device(f'cuda:{target_devices[0]}')
    return device
