#!/usr/bin/env python
# coding=utf-8

from {{ cookiecutter.repo_name }}.base.scheduler import lr_scheduler, BaseScheduler


__all__ = ['StepLR']


def StepLR(defaults):
    return lr_scheduler.StepLR(defaults)
