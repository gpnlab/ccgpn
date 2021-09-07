![ccgpn-logo](./docs/docs/ccgpn-logo.png)

## **Cookiecutter GPN:**

### A flexible template for implementing and sharing machine learning models.

#### Project GitHub Repo: [https://github.com/gpnlab/ccgpn/](https://github.com/gpnlab/ccgpn)
--------------------

Why this template? A well-defined, standard project structure means that a
newcomer can begin to understand an analysis without digging in to extensive
documentation. It also means that they don't necessarily have to read 100% of
the code before knowing where to look for very specific things.

Well organized code tends to be self-documenting in that the organization
itself provides context for your code without much overhead. A great example is
the [Filesystem Hierarchy
Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard) for
Unix-like systems. The `/etc` directory has a very specific purpose, as does
the `/tmp` folder, and everybody (more or less) agrees to honor that social
contract. That means a Red Hat user and an Ubuntu user both know roughly where
to look for certain types of files, even when using each other's system — or
any other standards-compliant system for that matter! Ideally, that's how it
should be when a colleague opens up your data science project.

The recommendations we make here follow the standards and conventions of much
of the scientific Python eco-system. Following these standards and
recommendations will make it easier

 * for others to use your code,
 * to port your code into other projects
 * to collaborate with other users of this eco-system,
 * to learn about the analysis process and the domain, and
 * to feel confident in analysis conclusions.

We're not talking about bikeshedding the indentation aesthetics or pedantic
formatting standards — ultimately, data science code quality is about
correctness and reproducibility.

Just Python? Your analysis doesn't have to be in Python, but the template does
provide some Python boilerplate that you'd want to remove (in the
`package_name` folder for example, and the Sphinx documentation skeleton in
`docs`).

Disagree with a couple of the default folder names? Working on a project that's
a little nonstandard and doesn't exactly fit with the current structure? Prefer
to use a different package than one of the (few) defaults?

**Go for it!** This is a lightweight structure, and is intended to be a good
starting point for many projects.

![standards](./docs/docs/standards.png)

### Requirements to use this cookiecutter:
-----------
 - Python 2.7 or 3.8+
 - PyTorch >= 1.9
 - Tensorboard >= 2.6
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.7.0:
 - This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```
or
``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

### To start a new project, run:
------------
```bash
cookiecutter https://github.com/gpnlab/ccgpn
```

### Installing development requirements
------------
```bash
make requirements
```

### Create virtual environment
------------
```bash
make create_environment
```

### Run MNIST hello world example
------------
```bash
conda activate <your_repo_name>
<your_repo_name> train
```

### Example setup
------------
[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)

### The resulting directory structure
------------
The directory structure of your new project looks like this:

```
├── LICENSE
├── Makefile             <- Makefile with commands like `make data` or `make train`
├── README.md            <- The top-level README for developers using this project.
│
├── references/          <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports              <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures/         <- Generated graphics and figures to be used in reporting
│
├── docs/                <- A default Sphinx project; see sphinx-doc.org for details
│
├── data                 <- directory for storing input data
│   ├── external/        <- Data from third party sources.
│   ├── interim/         <- Intermediate data that has been transformed.
│   ├── processed/       <- The final, canonical data sets for modeling.
│   └── raw/             <- The original, immutable data dump.
│
├── experiments                                     <- directory for storing experimental setups
│   ├── A01_MLP-XOR-implementation/
│   ├── A02_clustering-interleaving-moons/
│   ├── A03_MNIST-handwritten-digit-classification/
│   └── A04_fashion-MNIST-clothing-classification   <- Aims. Naming convention is
│           │                                          aim ID (A + ordered two-digit integer)
│           │                                          + "_" + short "-" delimited description
│           ├── E01_linear-model/
│           ├── E02_MLP/
│           └── E03_CNN                             <- Experiments. Naming convention is
│                │                                     experiment ID
│                │                                     (E + ordered two-digit integer)
│                │                                     + "_" + short "-" delimited description
│                ├── S0001_pilot/
│                ├── S0002_adam/
│                ├── S0003_dec-lr/
│                └── S0004_inc-batch                <- Setups. Naming convention is setup ID
│                      │                               (S + ordered four-digit integer)
│                      │                               + "_" + short "-" delimited description
│                      └── A04-E03-S0004.yml        <- YAML configuration file.
│                                                      Naming convention is aim ID +
│                                                      "-" + experiment ID + "-" setup ID
│
│
├── notebooks/                     <- Jupyter notebooks. Naming convention is
│                                     a number (for ordering) + "_" + the creator's initials
│                                     + "_" experiment ID + "_" + short `-` delimited
│                                     description, e.g. `1.0_ed_E01_results-visualization`
│
├── trials                         <- directory for storing experimental trials
│    ├── A01-E01-S0001/            <- Name of the YAML config file
│    ├── A02-E01-S0001/
│    ├── A03-E01-S0001/
│    └── A04-E03-S0004
│         ├── timestamp1/           <- timestamp, in YYYYMMDDhhmmssUTC format,
│         │                            i.e., year (YYYY), month (MM), day (DD),
│         │                            hour (hh), minute (mm), second (ss), all according to
│         │                            the Coordinated Universtal Time (UTC) standard
│         └── timestamp2
│                    ├── etc/       <- stores all information necessary to reproduce this trial,
│                    │                 e.g., the YAML config file, resuming session, seeds
│                    ├── logs/      <- stores all logging information
│                    ├── runs/      <- stores Tensorboard runs
│                    └── ckpts/     <- stores checkpoints
│
│
├── observations                    <- directory for storing experimental observations
│    ├── A01-E01-S0001/
│    ├── A02-E01-S0001/
│    ├── A03-E01-S0001/
│    └── A04-E03-S0004
│         ├── timestamp1/
│         └── timestamp2/
│
│
├── tox.ini              <- tox file with settings for running tox; see tox.readthedocs.io
│
├── requirements.txt     <- The requirements file for reproducing the analysis environment,
│                           e.g., generated with `pip freeze > requirements.txt`
├── requirements-dev.txt <- The requirements file with the devel dependencies
│
├── setup.py             <- makes project pip installable (pip install -e .)
│                           so package_name can be imported
├── tests/               <- folder with test code
│
├── logging.yml          <- logging configuration
│
└── package_name                  <- package directory
    ├── __init__.py               <- Makes package_name a Python package
    ├── cli.py                    <- command line interface
    ├── package_name.py           <- package script
    ├── main_foo.py               <- training script for model "foo"
    ├── main_example.py           <- training script for model "example"
    │
    ├── base                      <- abstract base classes
    │   ├── __init__.py           <- Makes the abstract base class a Python subpackage
    │   ├── base_transform.py     <- abstract base class for data transformations
    │   ├── base_dataset.py       <- abstract base class for datasets
    │   ├── base_dataloader.py    <- abstract base class for data loaders
    │   ├── base_arch.py          <- abstract base class for models' archtectures
    │   ├── base_loss.py          <- abstract base class for losses
    │   ├── base_metric.py        <- abstract base class for metrics
    │   ├── base_optimizer.py     <- abstract base class for optimizers
    │   ├── base_scheduler.py     <- abstract base class for schedulers
    │   └── base_trainer.py       <- abstract base class for trainers
    │
    ├── utils                     <- utilities
    │    ├── seeder.py            <- manages reproducibility
    │    ├── logger.py            <- trainning logger
    │    ├── monitor.py           <- Tensorboard visualization support
    │    └── backer.py            <- manages paths for saving models + logs
    │
    ├── model_foo/                <- each model is a subpackage
    └── model_example               <- model "example"
         ├── __init__.py          <- Makes model_bar a Python subpackage
         ├── dataset.py
         ├── transform.py
         ├── dataloader.py
         ├── loss.py
         ├── metric.py
         ├── arch.py
         ├── optimizer.py
         ├── scheduler.py
         └── trainer.py

```
### Config file format
------------------
Config files are in `.yml` format:

```yaml
name: A04-E03-S0004
seed: 12345
target_devices: [0]
save_dir: trials/

arch:
    type: bar
    args: {}

data_loader:
    type: MNIST
    args:
        batch_size: 128
        data_dir: data/
        num_workers: 2
        shuffle: true
        validation_split: 0.1

loss: nll_loss

lr_scheduler:
    type: StepLR
    args:
        gamma: 0.1
        step_size: 50

metrics:
    - my_metric
    - my_metric2

optimizer:
    type: Adam
    args:
        lr: 0.001
        weight_decay: 0

training:
    early_stop: 10
    epochs: 100
    monitor: min val_loss
    save_period: 1
    tensorboard: true

testing:
    data_dir: data/
    batch_size: 128
    num_workers: 8
```

Add additional configurations as needed.

### Checkpoints
-----------
You can specify the name of the training session in config files:

```yaml
name: A04-E03-S0004
```

The checkpoints will be saved in

`<save_dir>/<trial>/<timestamp>/ckpts/ckpt_epoch-<n>_<trial>_<timestamp>`,

where `<save_dir>` and `<trial>` are as defined in the config file, `<n>` is an
integer identifying the checkpoint, and timestamp is a datetime footprint in
the `YYYYMMDDhhmmssUTC` format, with year (`YYYY`), month (`MM`), day (`DD`),
hour (`hh`), minute (`mm`), second (`ss`), all according to the Coordinated
Universtal Time (`UTC`) standard. A copy of config file will be saved in

`<save_dir>/<trial>/<timestamp>/etc/config_<trial>_<timestamp>.yml`.

**Note**: checkpoints contain:

```python
checkpoint = {
'arch': arch,
'epoch': epoch,
'state_dict': self.model.state_dict(),
'optimizer': self.optimizer.state_dict(),
'monitor_best': self.mnt_best,
'config': self.config
}
```

### Tensorboard Visualization
--------------------------
This template supports [Tensorboard visualization](https://pytorch.org/docs/stable/tensorboard.html)

1. Run training

> Set `tensorboard` option in config file true.

2. Open tensorboard server

> Type `tensorboard --logdir <save_dir>/` at the project root, then server will
> open at `http://localhost:6006`

By default, values of loss and metrics specified in config file, input images,
and histogram of model parameters will be logged. If you need more
visualizations, use `add_scalar('tag', data)`, `add_image('tag', image)`, etc
in the `trainer._train_epoch` method. `add_something()` methods in this
template are basically wrappers for those of `tensorboard.SummaryWriter`
module.

**Note**: You don't have to specify current steps, since `TensorboardWriter`
class defined at `logger/monitor.py` will track current steps automatically.

## Repository Structure
------------
Features:

 * Clearfolder structure which is suitable for many deep learning projects.
 * Runs are configured via ``.yml`` files allowing for easy experimentation.
 * Checkpoint saving and resuming.
 * Tensorboard logging

We now examine the newly created repository in more detail.

### `data`
------------

Don't ever edit your raw data, especially not manually, and especially not in
Excel. Don't overwrite your raw data. Don't save multiple versions of the raw
data. Treat the data (and its format) as immutable. The code you write should
move the raw data through a pipeline to your final analysis. You shouldn't have
to run all of the steps every time you want to make a new figure, but anyone
should be able to reproduce the final products with only the code in `package_name`
and the data in `data/raw`.

**Analysis should be a DAG**. Ever tried to reproduce an analysis that you
did a few months ago or even a few years ago? You may have written the code,
but it's now impossible to decipher whether you should use
`make_figures.py.old`, `make_figures_working.py` or `new_make_figures01.py` to
get things done. Here are some questions we've learned to ask with a sense of
existential dread:

 * Are we supposed to go in and join the column X to the data before we get
  started or did that come from one of the notebooks?
 * Come to think of it, which notebook do we have to run first before running
  the plotting code: was it "process data" or "clean data"?
 * Where did the shapefiles get downloaded from for the geographic plots?
 * $\textrm{\textit{etc.}}\cdot \infty$

These types of questions are painful and are symptoms of a disorganized
project. A good project structure encourages practices that make it easier to
come back to old work, for example separation of concerns, abstracting analysis
as a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph), and
engineering best practices like version control.

**If Analysis is a DAG, it is streamlinable**. Often in an analysis you have
long-running steps that preprocess data or train models. If these steps have
been run already (and you have stored the output somewhere like the
`data/interim` directory), you don't want to wait to rerun them every time. We
prefer [`make`](https://www.gnu.org/software/make/) for managing steps that
depend on each other, especially the long-running ones. Make is a common tool
on Unix-based platforms (and is available for Windows). Following the [`make`
documentation](https://www.gnu.org/software/make/), [Makefile
conventions](https://www.gnu.org/prep/standards/html_node/Makefile-Conventions.html#Makefile-Conventions),
and [portability
guide](http://www.gnu.org/savannah-checkouts/gnu/autoconf/manual/autoconf-2.69/html_node/Portable-Make.html#Portable-Make)
will help ensure your Makefiles work effectively across systems. Here are
[some](http://zmjones.com/make/)
[examples](http://blog.kaggle.com/2012/10/15/make-for-data-scientists/) to [get
started](https://web.archive.org/web/20150206054212/http://www.bioinformaticszen.com/post/decomplected-workflows-makefiles/).
A number of data folks use `make` as their tool of choice, including [Mike
Bostock](https://bost.ocks.org/mike/make/). There are other tools for managing
DAGs that are written in Python instead of a DSL (e.g.,
[Paver](http://paver.github.io/paver/#),
[Luigi](http://luigi.readthedocs.org/en/stable/index.html),
[Airflow](https://airflow.apache.org/index.html),
[Snakemake](https://snakemake.readthedocs.io/en/stable/),
[Ruffus](http://www.ruffus.org.uk/), or
[Joblib](https://pythonhosted.org/joblib/memory.html)). Feel free to use these
if they are more appropriate for your analysis.

Also, if data is immutable, it doesn't need source control in the same way that
code does. Therefore, ***by default, the data folder is included in the
`.gitignore` file.*** If you have a small amount of data that rarely changes,
you may want to include the data in the repository. Github currently warns if
files are over 50MB and rejects files over 100MB. Some other options for
storing/syncing large data include [AWS S3](https://aws.amazon.com/s3/) with a
syncing tool (e.g., [`s3cmd`](http://s3tools.org/s3cmd)), [Git Large File
Storage](https://git-lfs.github.com/), [Git
Annex](https://git-annex.branchable.com/), and [dat](http://dat-data.com/).
Currently by default, we support instantiating a S3 bucket and use [AWS
CLI](http://docs.aws.amazon.com/cli/latest/reference/s3/index.html) to sync
data in the `data` folder with the server (you can also sync data from a local
server).

**AWS CLI configuration**. When using Amazon S3 to store data, a simple method
of managing AWS access is to set your access keys to environment variables.
However, managing mutiple sets of keys on a single machine (e.g. when working
on multiple projects) it is best to use a [credentials
file](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html),
typically located in `~/.aws/credentials`. A typical file might look like:
```
[default]
aws_access_key_id=myaccesskey
aws_secret_access_key=mysecretkey

[another_project]
aws_access_key_id=myprojectaccesskey
aws_secret_access_key=myprojectsecretkey
```
You can add the profile name when initialising a project; assuming no
applicable environment variables are set, the default profile credentials will
be used.

Finally, a handy code snippet to get the standard file-system location for the
`data` folder:
```python
import os.path as op
from pathlib import Path
import package_name as pkg
root = Path(pkg.__path__[0]).parent.absolute()
data_path = op.join(root, 'data')
```

### `package_name`
------------

We place the main module for the source code in a file called `package_name.py`
in directory called `package_name`. This structure is a bit confusing at first,
but it is a simple way to create a structure where when we type `import
package_name as pkg` in an interactive Python session, the classes and
functions defined inside of the `package_name.py` file are available in the
`pkg` namespace. For this to work, we need to also create a file in
`__init__.py` which contains code that imports everything in that file into the
namespace of the project:

```python
from .package_name import *
```

As a general rule, in module code, we follow the convention that all functions
are either imported from other places, or are defined in lines that precede the
lines that use that function. This helps readability of the code, because you
know that if you see some name, the definition of that name will appear earlier
in the file, either as a function/variable definition, or as an import from
some other module or package.

### Environment
------------

The first step in reproducing an analysis is always reproducing the
computational environment it was run in. You need the same tools, the same
libraries, and the same versions to make everything play nicely together.

One effective approach to this is use a virtual environment . We included a
target in the Makefile (`make create_environment`) which will create a `conda`
environment (see [`Miniconda`](http://conda.pydata.org/miniconda.html) software
distribution, not to be confused with
[`Anaconda`](https://store.continuum.io/cshop/anaconda/), though they are
similar and both produced by Continuum) if conda is installed, else create a
[virtualenv](https://virtualenv.pypa.io/en/latest/)
([virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) is
recommended for managing virtualenvs).

By listing all of your requirements in the repository (we include a
`requirements.txt` file) you can easily track the packages needed to recreate
the analysis. Here is a good workflow:

* run `make create_environment` when creating a new project. This will create a
  `conda` environment if conda available, else create `virtualenv`.

* run `conda activate project_name` (or `workon project_name`) to activate the
  virtual environment.

* `pip install`/`conda install` the packages that your analysis needs.

* Run `conda list --export > requirements.txt` (or `pip freeze >
  requirements.txt`) to pin the exact package versions used to recreate the
  analysis.

* If you find you need to install another package, run `conda list --export >
  requirements.txt` (or `pip freeze > requirements.txt`) again and commit the
  changes to version control.


You can easily duplicate your environment and the associated dependencies with
`conda create --name <env_name> --file requirements.txt` (or `mkvirtualenv
<env_name>; workon <env_name>; pip install -r requirements.txt`).

This awesome [conversion
table](https://docs.conda.io/projects/conda/en/latest/commands.html#conda-vs-pip-vs-virtualenv-commands)
lists operation equivalences between `conda`, `pip` and `virtualenv`. For more
on the differences between `conda` and `pip`, see [this
article](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)
by Jake VanderPlas.

If you have more complex requirements for recreating your environment, consider
a container-based approach such as [Docker](https://www.docker.com/) or
[Vagrant](https://www.vagrantup.com/). Both of these tools use text-based
formats (Dockerfile and Vagrantfile, respectively) you can easily add to source
control to describe how to create a container with the requirements you
need.

### Making the Repository an Installable Package
------------

For installation and distribution we will use the python standard library
`setuptools` module. This module uses a `setup.py` file to figure out how to
install your software on a particular system. For a small project such as this
one, managing installation of the software modules and the data is rather
simple.

A `package_name/version.py` contains all of the information needed for the
installation and for setting up the [PyPI
page](https://pypi.python.org/pypi/shablona) for the software. This also makes
it possible to install your software using `pip` and `easy_install`, which
are package managers for Python software. The `setup.py` file reads this
information from there and passes it to the `setup` function which takes care
of the rest.

Much more information on packaging Python software can be found in the
[Hitchhiker's guide to
packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.org).

### Continuous integration
![continuous integration](./docs/docs/continuous-integration.png)

Travis-CI is a system that can be used to automatically test every revision of
your code directly from github, including testing of github pull requests,
before they are merged into the `master` branch. This provides you with
information needed in order to evaluate contributions made by others. It also
serves as a source of information for others interested in using or contributing
to your project about the degree of test coverage of your project.

You will need a .travis.yml file in your repo. This file contains the
configuration of your testing environment. This includes the different
environments in which you will test the source code (for example, we test
`package_name` against Python 2.7, Python 3.7 and Python 3.8). It includes steps
that need to be taken before installation of the software. For example,
installation of the software dependencies.

For details on setting up Travis-CI with github, see Travis-CI's
[getting started
page](https://docs.travis-ci.com/user/getting-started/#To-get-started-with-Travis-CI%3A).
To summarize:

1. Go to the Travis-CI [website](https://travis-ci.org/) and get a
Travis user account, linked to your github user account.

2. You will need to set up your github repo to talk to Travis.

3. You will need to go back to travis-ci, and flip on the switch on that side as
well.

4. The travis output will also report to you about test coverage, if you set it up
that way.

5. You will start getting emails telling you the state of the testing suite on
every pull request for the software, and also when you break the test suite on
the `master` branch. That way, you can be pretty sure that the `master` is
working (or at least know when it isn't...).

You can also continuously test your code on a Windows system. This is done on
another CI system called [Appveyor](http://www.appveyor.com/). In prinicple, it
does something that is very similar to what Travis does: downloads your code,
installs it on a Windows machine, with various versions of python, and runs the
tests. Appveyor is controlled through another configuration file: the
`appveyor.yml`. In addition to committing this file into the repository, you
will need to activate Appveyor for your project. This is done by signing into
the Appveyor interface with your Github account, clicking on the "projects" tab
at the top of the page, then clicking on the "+" sign for "New project" and
selecting the project you would like to add from the menu that appears (you
might need to give Appveyor the permission to see projects in your Github
account).

### Distribution
------------

The main venue for distribution of Python software is the [Python
Package Index](https://pypi.python.org/), or PyPI, also lovingly known
as "the cheese-shop". To distribute your software on PyPI, you will need to create a user account on
[PyPI](http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#register-your-project).
It is recommended that you upload your software using
[twine](http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/#upload-your-distributions).
Using Travis, you can automatically upload your software to PyPI, every time
you push a tag of your software to github. The instructions on setting this up
can be found [here](http://docs.travis-ci.com/user/deployment/pypi/). You will
need to install the travis command-line interface.

### Version Control
------------
![documents](./docs/docs/documents.png)

Source code versioning control is managed with git. Currently there are two
files in the repository which help working with this repository, and which you
could extend further:

- `.gitignore` -- specifies intentionally untracked files (such as
  compiled `*.pyc` files), which should not typically be committed to
  git (see `man gitignore`)
- `.mailmap` -- if any of the contributors used multiple names/email
  addresses or his git commit identity is just an alias, you could
  specify the ultimate name/email(s) for each contributor, so such
  commands as `git shortlog -sn` could take them into account (see
  `git shortlog --help`)

**Keep secrets and configuration out of version control**. You _really_ don't
want to leak your AWS secret key or Postgres username and password on Github.
Enough said — see the [Twelve Factor App](http://12factor.net/config)
principles on this point. One solution is to create a `.env` file in the
project root folder. Thanks to the `.gitignore`, this file should never get
committed into the version control repository. Here's an example:
```nohighlight
# example .env file
DATABASE_URL=postgres://username:password@localhost:5432/dbname
AWS_ACCESS_KEY=myaccesskey
AWS_SECRET_ACCESS_KEY=mysecretkey
OTHER_VARIABLE=something
```
If you look at the stub script in `package_name/data/make_dataset.py`, it uses
a package called [python-dotenv](https://github.com/theskumar/python-dotenv) to
load up all the entries in this file as environment variables so they are
accessible with `os.environ.get`. Here's an example snippet adapted from the
`python-dotenv` documentation:
```python
# src/data/dotenv_example.py
import os
from dotenv import load_dotenv, find_dotenv

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

database_url = os.environ.get("DATABASE_URL")
other_variable = os.environ.get("OTHER_VARIABLE")
```


### Styling
------------
![code style](./docs/docs/code-style.png)

Remember that code will be probably be read more times than it will be written.
Make it easy to read (for others, but also for yourself when you come back to
it), by following a consistent formatting style. We strongly recommend
following the [PEP8 code formatting
standard](https://www.python.org/dev/peps/pep-0008/), and we enforce this by
running a code-linter called `flake8` (it combines the tools `pep8` and
`pyflakes`), which automatically checks the code and reports any violations of
the PEP8 standard (and checks for other general code hygiene issues).

Some projects include `flake8` inside their automated tests, so that every pull
request is examined for code cleanliness. In this project, we have run `flake8`
most (but not all) files, on most (but not all) checks:

```bash
flake8 --ignore N802,N806 `find . -name *.py | grep -v setup.py | grep -v /doc/`
```

This means, check all .py files, but exclude setup.py and everything in
directories named "docs". Do all checks except N802 and N806, which enforce
lowercase-only names for variables and functions.

The `Makefile` contains an instruction for running this command as well:

```bash
make flake8
```

### Documentation
------------
![rtfm](./docs/docs/rtfm.png)

Documenting your software is a good idea. Not only as a way to communicate to
others about how to use the software, but also as a way of reminding yourself
what the issues are that you faced, and how you dealt with them, in a few
months/years, when you return to look at the code.

The first step in this direction is to document every function in your module
code. We recommend following the [numpy docstring
standard](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt),
which specifies in detail the inputs/outputs of every function, and specifies
how to document additional details, such as references to scientific articles,
notes about the mathematics behind the implementation, etc.

This standard also plays well with a system that allows you to create more
comprehensive documentation of your project. Writing such documentation allows
you to provide more elaborate explanations of the decisions you made when you
were developing the software, as well as provide some examples of usage,
explanations of the relevant scientific concepts, and references to the relevant
literature.

To document `package_name` we use the [Sphinx documentation
system](http://sphinx-doc.org/). You can follow the instructions on the sphinx
website, and the example [here](http://matplotlib.org/sampledoc/) to set up the
system, but we have also already initialized and commited a skeleton
documentation system in the `docs` directory, that you can build upon.

Sphinx uses a `Makefile` to build different outputs of your documentation. For
example, if you want to generate the HTML rendering of the documentation (web
pages that you can upload to a website to explain the software), you will type:

```
make html
```

This will generate a set of static webpages in the `docs/_build/html`, which you
can then upload to a website of your choice.

Alternatively, [readthedocs.org](https://readthedocs.org) (careful,
*not* readthedocs.**com**) is a service that will run sphinx for you,
and upload the documentation to their website. To use this service,
you will need to register with RTD. After you have done that, you will
need to "import your project" from your github account, through the
RTD web interface. To make things run smoothly, you also will need to
go to the "admin" panel of the project on RTD, and navigate into the
"advanced settings" so that you can tell it that your Python
configuration file is in `docs/conf.py`.

### Testing
------------
![TDD](./docs/docs/tdd.jpeg)

Most scientists who write software constantly test their code. That is, if you
are a scientist writing software, I am sure that you have tried to see how well
your code works by running every new function you write, examining the inputs
and the outputs of the function, to see if the code runs properly (without
error), and to see whether the results make sense.

Automated code testing takes this informal practice, makes it formal, and
automates it, so that you can make sure that your code does what it is supposed
to do, even as you go about making changes around it.

Most scientists writing code are not really in a position to write a complete
[specification](http://www.wired.com/2013/01/code-bugs-programming-why-we-need-specs/)
of their software, because when they start writing their code they don't quite
know what they will discover in their data, and these chance discoveries might
affect how the software evolves. Nor do most scientists have the inclination to
write complete specs - scientific code often needs to be good enough to cover
our use-case, and not any possible use-case. Testing the code serves as a way to
provide a reader of the code with very rough specification, in the sense that it
at least specifies certain input/output relationships that will certainly hold
in your code.

We recommend using the ['pytest'](http://pytest.org/latest/) library for
testing. The `py.test` application traverses the directory tree in which it is
issued, looking for files with the names that match the pattern `test_*.py`
(typically, something like our `package_name/tests/test_package_name.py`).
Within each of these files, it looks for functions with names that match the
pattern `test_*`. Typically each function in the module would have a
corresponding test (e.g. `test_transform_data`). This is sometimes called 'unit
testing', because it independently tests each atomic unit in the software.
Other tests might run a more elaborate sequence of functions ('end-to-end
testing' if you run through the entire analysis), and check that particular
values in the code evaluate to the same values over time. This is sometimes
called 'regression testing'. Regressions in the code are often canaries in the
coal mine, telling you that you need to examine changes in your software
dependencies, the platform on which you are running your software, etc.

Test functions should contain assertion statements that check certain relations
in the code. Most typically, they will test for equality between an explicit
calculation of some kind and a return of some function. We recommend using
functions from the `numpy.testing` module (which we import as `npt`) to assert
certain relations on arrays and floating point numbers. This is because `npt`
contains functions that are specialized for handling `numpy` arrays, and they
allow to specify the tolerance of the comparison through the `decimal` key-word
argument.

To run the tests on the command line, change your present working directory to
the top-level directory of the repository (e.g. `/home/user/code/package_name`),
and type:

```bash
py.test package_name
```

This will exercise all of the tests in your code directory. If a test fails, you
will see a message such as:


    package_name/tests/test_package_name.py .F...

    =================================== FAILURES =============================

    .
    .
    .


    E       AssertionError:

    .
    .
    .

    package_name/tests/test_package_name.py:49: AssertionError
    ====================== 1 failed, 4 passed in 0.82 seconds ================

As your code grows and becomes more complicated, you might develop new features
that interact with your old features in all kinds of unexpected and surprising
ways. As you develop new features of your code, keep running the tests, to make
sure that you haven't broken the old features.  Keep writing new tests for your
new code, and recording these tests in your testing scripts. That way, you can
be confident that even as the software grows, it still keeps doing correctly at
least the few things that are codified in the tests.

We have also provided a `Makefile` that allows you to run the tests with more
verbose and informative output from the top-level directory, by issuing the
following from the command line:

```bash
make test
```

### Notebooks
------------
![code style](./docs/docs/notebooks.png)

Notebook packages like the [Jupyter notebook](http://jupyter.org/), [Beaker
notebook](http://beakernotebook.com/),
[Zeppelin](http://zeppelin-project.org/), and other literate programming tools
are very effective for exploratory data analysis. Hence, the notebooks
directory can be used as a place to experiment with your module code, and as a
place to produce scripts that contain a narrative structure, demonstrating the
use of the code, or producing scientific results from your code and your data
and telling a story with these elements. For example, an IPython notebook that
reads in some data, and creates a figure. Maybe this is *Figure 1* from some
future article?

When we use notebooks in our work, we often subdivide the `notebooks` folder.
For example, `notebooks/exploratory` contains initial explorations, whereas
`notebooks/reports` is more polished work that can be exported as html to the
`reports` directory.

Since notebooks are challenging objects for source control (e.g., diffs of the
`json` are often not human-readable and merging is near impossible), we
recommended not collaborating directly with others on Jupyter notebooks. There
are two steps we recommend for using notebooks effectively:

1. Follow a naming convention that shows the owner and the order the analysis
   was done in. We use the format `<step>_<ghuser>_<description>.ipynb` (e.g.,
   `1.0-ed-visualize-distributions.ipynb`).

2. Refactor the good parts. Don't write code to do the same task in multiple
   notebooks. If it's a data preprocessing task, put it in the pipeline at
   `package_name/data` and load data from `data/interim`. If it's useful
   utility code, refactor it to `package_name`.

Now, by default we turn the project into a Python package, so you can import
your code and use it in notebooks with a cell like the following:

```python
# OPTIONAL: Load the "autoreload" extension so that code can change
%load_ext autoreload

# OPTIONAL: always reload modules so that as you change code in src, it gets loaded
%autoreload 2

import package_name.data as data
```

### Licensing
------------
![open source](./docs/docs/open_source.png)

License your code! A repository like this without a license maintains
copyright to the author, but does not provide others with any
conditions under which they can use the software. In this case, we use
the BSD-3 license. You can read the conditions of the license in the
`LICENSE` file. As you can see, this is not an Apple software license
agreement (has anyone ever actually tried to read one of those?). It's
actually all quite simple, and boils down to "You can do whatever you
want with my software, but I take no responsibility for what you do
with my software"

For more details on what you need to think about when considering
choosing a license, see this
[article](http://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/)!

### Getting cited
------------
![citation needed](./docs/docs/citation_needed.png)

When others use your code in their research, they should probably cite you. To
make their life easier, we use [duecredit](http://www.duecredit.org). This is a software
library that allows you to annotate your code with the correct way to cite it.
To enable `duecredit`, we have added a file `due.py` into the main directory.
This file does not need to change at all (though you might want to occasionally
update it from duecredit itself. It's
[here](https://github.com/duecredit/duecredit/blob/master/duecredit/stub.py),
under the name `stub.py`).

In addition, you will want to provide a digital object identifier (DOI) to the
article you want people to cite.

To get a DOI, use the instructions in [this page](https://guides.github.com/activities/citable-code/).

Another way to get your software cited is by writing a paper. There are several
[journals that publish papers about software](https://www.software.ac.uk/resources/guides/which-journals-should-i-publish-my-software).

### Contributing
------------
![here to help](./docs/docs/here_to_help.png)

Best practices change, tools evolve, and lessons are learned. **The goal of
this project is to make it easier to start, structure, and share an analysis.**
[Pull requests](https://github.com/gpnlab/ccgpn/pulls)
and [filing
issues](https://github.com/gpnlab/ccgpn/issues) is
encouraged. We'd love to hear what works for you, and what doesn't!

### Links to related projects and references
------------
Project structure and reproducibility is talked about more in the R research
community. Here are some projects and blog posts if you're working in R that
may help you out.

 - [Project Template](http://projecttemplate.net/index.html) - An R data analysis template
 - "[Designing projects](http://nicercode.github.io/blog/2013-04-05-projects/)" on Nice R Code
 - "[My research workflow](http://www.carlboettiger.info/2012/05/06/research-workflow.html)" on Carlboettiger.info
 - "[A Quick Guide to Organizing Computational Biology Projects](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)" in PLOS Computational Biology

### Acknowledgements
------------
![reinvent the wheel](./docs/docs/reinvent_the_wheel.png)

Many thanks to the
[Cookiecutter](https://cookiecutter.readthedocs.org/en/latest/) project
([github](https://github.com/audreyr/cookiecutter)), which is helping us all
spend less time molding and more time getting things baked.

This cookiecutter was developed abreast the awesome [Cookiecutter Data
Science](http://drivendata.github.io/cookiecutter-data-science/)
project ([github](https://github.com/drivendata/cookiecutter-data-science)),
borrowing features from
[shablona](https://github.com/uwescience/shablona) (e.g. duecredit, travis CI) and inspired by the directory
scaffold of
[Cookiecutter-Pytorch](https://github.com/khornlund/cookiecutter-pytorch). Here are some examples of projects using `cookiecutter-pytorch` template:
 1. [Severstal Steel Defect Detection (Kaggle)](https://github.com/khornlund/severstal-steel-defect-detection)
 2. [Aptos Blindness Detection (Kaggle)](https://github.com/khornlund/aptos2019-blindness-detection)
 3. [Understanding Cloud Organization (Kaggle)](https://github.com/khornlund/understanding-cloud-organization)
