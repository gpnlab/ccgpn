#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function

from .due import due, Doi, BibTeX, Text

# Use duecredit (duecredit.org) to provide a citation to relevant work to
# be cited. This does nothing, unless the user has duecredit installed,
# And calls this with duecredit (as in `python -m duecredit script.py`):
due.cite(Doi("00.0000/00.0.00"),
         description="{{ cookiecutter.description }}",
         tags=["{{ cookiecutter.tags }}"],
         path='{{ cookiecutter.repo_name }}')
