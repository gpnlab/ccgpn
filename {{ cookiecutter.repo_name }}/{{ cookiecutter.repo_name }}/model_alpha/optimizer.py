#!/usr/bin/env python
# coding=utf-8

import torch.optim as optim
from {{ cookiecutter.repo_name }}.base.optimizer import BaseOptimizer


__all__ = ['Adam']


def Adam(params, defaults):
    return optim.Adam(params, defaults)
