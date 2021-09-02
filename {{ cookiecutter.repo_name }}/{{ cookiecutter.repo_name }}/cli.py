import click
import yaml
import datetime
import os
import re

from {{ cookiecutter.repo_name }} import main
from {{ cookiecutter.repo_name }}.utils import setup_logging


@click.group()
def cli():
    """
    CLI for {{ cookiecutter.repo_name }}
    """
    pass


@cli.command()
@click.option(
    '-c',
    '--config-filename',
    default=['experiments/config.yml'],
    multiple=True,
    help=(
        'Path to training configuration file. If multiple are provided, runs will be '
        'executed in order'
    )
)
@click.option('-r', '--resume', default=None, type=str, help='path to checkpoint')
def train_example(config_filename, resume):
    """
    Entry point to start training run(s) for model `example`.
    """
    configs = [load_config(f) for f in config_filename]
    for config in configs:
        setup_logging(config)
        main_example.train(config, resume)


def load_config(filename: str) -> dict:
    """
    Load a configuration file as YAML.
    """
    with open(filename) as fh:
        config = yaml.safe_load(fh)

    # Parse filename to get this particular experimental run info
    trial_info = {}

    nameRegex = re.compile(r'((A\d\d)-(E\d\d)-(S\d\d\d\d))')
    trial_ID, aim_ID, exp_ID, setup_ID = nameRegex.search(filename).groups()
    trial_info['ID'] = trial_ID

    aimRegex = re.compile(f'({aim_ID})_([\w\-]+)')
    trial_info['Aim'] = aimRegex.search(path).groups()

    expRegex = re.compile(f'({exp_ID})_([\w\-]+)')
    trial_info['Experiment'] = expRegex.search(path).groups()

    setupRegex = re.compile(f'({setup_ID})_([\w\-]+)')
    trial_info['Setup'] = setupRegex.search(path).groups()

    trial_info['timestamp'] = get_timestamp()

    config['trial_info'] = trial_info

    return config

def get_timestamp() -> str:
    """
    Get this experimental run timestamp, e.g., 20211231235959UTC'
    """
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    return timestamp + 'UTC'
