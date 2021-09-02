#!/usr/bin/env python
# coding=utf-8

import abc
from abc import ABC

import torchvision.transforms as T


class AugmentationFactory(ABC):
    def build_transforms(self, train):
        return self.build_train() if train else self.build_test()

    @abc.abstractmethod
    def build_train(self):
        pass

    @abc.abstractmethod
    def build_test(self):
        pass
