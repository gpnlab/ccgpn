#!/usr/bin/env python
# coding=utf-8

from {{ cookiecutter.repo_name }}.base import BaseTransform, AugmentationFactory
import torchvision.transforms as T


class MNISTTransform(AugmentationFactory):

    MEANS = [0]
    STDS = [1]

    def get_train(self):
        return T.Compose([T.ToTensor(), T.Normalize(self.MEANS, self.STDS)])

    def get_test(self):
        return T.Compose([T.ToTensor(), T.Normalize(self.MEANS, self.STDS)])
