#!/usr/bin/env python
# coding=utf-8

import torch.optim.lr_scheduler as lr_scheduler
from {{ cookiecutter.repo_name }}.base import BaseScheduler


def StepLR(defaults):
    return lr_scheduler.StepLR(defaults)
