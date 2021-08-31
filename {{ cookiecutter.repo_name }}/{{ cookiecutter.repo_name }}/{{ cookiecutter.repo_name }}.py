#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function

import os
import random
from typing import Any, List, Tuple, Dict
from types import ModuleType

from .due import due, Doi, BibTeX, Text
from .data import *
from .features import *
from .models import *
from .visualization import *


# Use duecredit (duecredit.org) to provide a citation to relevant work to
# be cited. This does nothing, unless the user has duecredit installed,
# And calls this with duecredit (as in `python -m duecredit script.py`):
due.cite(Doi("00.0000/00.0.00"),
         description="{{ cookiecutter.description }}",
         tags=["{{ cookiecutter.tags }}"],
         path='{{ cookiecutter.repo_name }}')
