from __future__ import absolute_import, division, print_function
from os.path import join as pjoin
from pathlib import Path
import io
import re
import {{ cookiecutter.repo_name }} as pkg
root = Path(pkg.__path__[0]).parent.absolute()
readme = pjoin(root, 'README.md')

def read_long_description(readme):
    text_type = type(u"")
    with io.open(readme, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"),
                      fd.read())

# Format expected by setup.py and docs/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: {{ cookiecutter.open_source_license }}",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Programming Language :: Python :: 3.8",
               "Topic :: Scientific/Engineering"]

NAME = "{{ cookiecutter.repo_name }}"
MAINTAINER = "{{ cookiecutter.author_name }}"
MAINTAINER_EMAIL = "{{ cookiecutter.author_email }}"
DESCRIPTION = "p{{ cookiecutter.description }}"
LONG_DESCRIPTION = read_long_description(readme)
URL = "http://github.com/{{ cookiecutter.github_handle }}/{{ cookiecutter.repo_name }}"
DOWNLOAD_URL = ""
LICENSE = "{{ cookiecutter.open_source_license }}"
AUTHOR = "{{ cookiecutter.author_name }}"
AUTHOR_EMAIL = "{{ cookiecutter.author_email }}"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'{{ cookiecutter.repo_name }}': [pjoin('data', '*')]}
REQUIRES = [] # use environment.yml for conda or requirements.txt for pip
PYTHON_REQUIRES = ">= 3.8"
ENTRY_POINTS = {
    "console_scripts": [
        "{{ cookiecutter.repo_name }}={{ cookiecutter.repo_name }}.cli:cli"
    ]
}
