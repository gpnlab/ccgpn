#!/usr/bin/env python
# coding=utf-8

from torch.optim import Optimizer

from torch.optim import (Adadelta, Adagrad, Adam, AdamW, SparseAdam, Adamax,
                         ASGD, LBFGS, RMSprop, Rprop, SGD)

# For a guide on writing custon PyTorch optimizers see:
# http://mcneela.github.io/machine_learning/2019/09/03/Writing-Your-Own-Optimizers-In-Pytorch.html

class BaseOptimizer(Optimizer):
    """
    Base class for all custom optimizers
    """
    def __init__(self, params, defaults):
        super(BaseOptimizer, self).__init__(params, defaults)

    def step(self, closure=None):
        raise NotImplementedError
