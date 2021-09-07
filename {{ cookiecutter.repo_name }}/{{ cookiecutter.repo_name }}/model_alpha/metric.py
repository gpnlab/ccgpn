#!/usr/bin/env python
# coding=utf-8

import torch
from {{ cookiecutter.repo_name }}.base.BaseMetric import top_k_acc


def top_1_acc(output, target):
    """
    Computes the top 1 accuracy
    """
    return top_k_acc(output, target, k=1)


def top_3_acc(output, target):
    """
    Computes the top 3 accuracy
    """
    return top_k_acc(output, target, k=3)
