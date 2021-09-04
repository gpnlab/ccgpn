import click
import yaml
import datetime
import os
import re
from dotenv import find_dotenv, load_dotenv

from {{ cookiecutter.repo_name }} import main_example
from {{ cookiecutter.repo_name }}.utils import setup_logging


@click.group()
def cli():
    """
    CLI for {{ cookiecutter.repo_name }}
    """
    pass


@cli.command()
@click.option('-c', '--config-filename', multiple=True,
              help=('Path to training configuration file. If multiple are '
                    'provided, runs will be executed in order'))
@click.option('-e', '--env-variables', multiple=True,
              help=('Environment variables\' names. Multiple variables are '
                    'supported'))
@click.option('-r', '--resume', default=None, type=str,
              help='path to checkpoint')
def train_example(config_filename, env_variables, resume):
    """
    Entry point to start training run(s) for model `example`.
    """
    configs = [load_config(f) for f in config_filename]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())
    env_variables = {e: os.environ.get(e) for e in env_variables}

    for config in configs:
        setup_logging(config)
        config['ENV'] = env_variables
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
