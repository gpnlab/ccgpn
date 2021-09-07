#!/usr/bin/env python
# coding=utf-8

import torch.nn.functional as F
from {{ cookiecutter.repo_name }}.base import BaseLoss


def nll_loss(input, target):
    return F.nll_loss(input, target)
