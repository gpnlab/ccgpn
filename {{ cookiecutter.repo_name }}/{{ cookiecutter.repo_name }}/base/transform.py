#!/usr/bin/env python
# coding=utf-8

from abc import ABC, abstractmethod

import torchvision.transforms as T


__all__ = ['AugmentationFactory', 'BaseTransform']


class AugmentationFactory(ABC):
    """
    Base class for augmentation factory
    """
    def get_transform(self, train):
        """
        Switch to select between train or test transforms
        """
        return self.get_train() if train else self.get_test()

    @abstractmethod
    def get_train(self):
        """
        Get transform to be applied to the train dataset
        """
        raise NotImplementedError

    @abstractmethod
    def get_test(self):
        """
        Get transform to be applied to the test dataset
        """
        raise NotImplementedError


class BaseTransform(ABC):
    """
    Base class for all custom transforms
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __call__(self, sample):
        raise NotImplementedError
