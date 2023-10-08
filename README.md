# Modern Python project template

A Python [cookiecutter](https://www.cookiecutter.io/) project template with everything you need to get started.

## Features
This template provides the following features:
- A basic, fully functional project structure created in a [flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/),
- [Poetry](https://python-poetry.org/) Python dependency management ([pyproject.toml](https://python-poetry.org/docs/pyproject/) support),
- [Hydra](https://hydra.cc)-based configuration with [Pydantic](https://docs.pydantic.dev/latest/) validation,
- Various open source licenses,
- Python minimal [.gitignore](https://git-scm.com/docs/gitignore),
- Management Python environments with [tox](https://tox.wiki/en/stable/),
- Testing using [pytest](https://docs.pytest.org/en/stable/) and [hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html) (for [property-based tests](https://www.youtube.com/watch?v=uN6JjpzVsAo)),
- [Docker](https://www.docker.com/) support,
- [pre-commit](https://pre-commit.com/) with [CI support](https://pre-commit.ci/),
- CI/CD with [GitHub actions](https://github.com/features/actions),
- [Codecov](https://about.codecov.io/) test coverage reports in CI,
- GitHub [citation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) file (BibTeX and APA format),
- User friendly project creation prompts,
- *One command to test them all* (just type `tox`),
- Post-project generation tips.


## Prerequisites

The only prerequisites for this template are **Python**, **cookiecutter** and **tox** installed on your local machine.

Check Python version:
```
python --version
```

Use [pip](https://pip.pypa.io/en/stable/) to install cookiecutter and tox in the latest available versions:
```
pip install --user cookiecutter tox
```

Check installed versions:

```
cookiecutter --version
tox --version
```

## Usage

To generate a new project follow these steps:
1. Navigate to the desired directory and run the `cookiecutter https://github.com/Savaed/modern-python.git` command.
2. Go to the root of the project you created (the one where the *README.md* file is located).
3. Use the `tox` command to **test the entire project**. You can then remove the `sanity-check` environment configuration from the *tox.ini* file.


> **Once the project has been successfully created, check the generated files to make any necessary changes.**

## Sample project structure
The default project created with `cookiecutter https://github.com/Savaed/modern-python.git`:

```
sample_project/                   < Root directory (flat layout)
├── .dockerignore                 < Ignore files in Docker builds
├── .env                          < Environment variables
├── .github
│   └── workflows
│       └── main.yaml             < Github Actions CI/CD
├── .gitignore                    < Ignore files in git operations
├── .pre-commit-config.yaml       < pre-commit hooks config
├── .vscode
│   ├── launch.json
│   └── settings.json
├── CITATION.cff                  < Let others cite your software
├── Dockerfile                    < Docker build definition
├── LICENSE                       < License [MIT/BSD/ISC/Apache v2.0/GNU v.3]
├── README.md                     < README template
├── configs
│   ├── __init__.py
│   └── config.yaml               < Hydra config, see config.py
├── data
│   ├── final                     < Final, pre-processed data
│   │   └── .gitkeep
│   ├── interim                   < Pre-processed intermidiate data
│   │   └── .gitkeep
│   └── raw                       < Raw, external data
│       └── .gitkeep
├── pyproject.toml                < Project metadata and Python dependencies
├── sample_project                < Top-level Python package (source code goes here)
│   ├── config.py                 < Pydantic configuration and its validation
│   ├── file.py
│   ├── log.py                    < Loguru minimal structured logging
│   └── scripts
│       └── script1.py            < Sample script
├── tests                         < Pytest and hypothesis tests
│   ├── conftest.py
│   ├── file_test.py
│   └── script1_test.py
└── tox.ini                       < Environment setup for test/CI
```
