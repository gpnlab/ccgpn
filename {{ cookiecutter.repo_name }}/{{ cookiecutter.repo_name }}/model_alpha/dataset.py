#!/usr/bin/env python
# coding=utf-8

from torch.utils.data import Dataset
from {{ cookiecutter.repo_name }}.base import BaseDataset


__all__ = ['MNISTDataset']


def MNISTDataset(data_dir, train, download, transform):
    return Dataset.MNIST(data_dir, train, download, transform)
