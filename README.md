# Cookiecutter modern Python project template

A Python project with everything you need to get started.

## Features
This template provides the following features:
- A basic, fully functional project structure created in a [flat style](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/),
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
- GitHub [citation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) file (BibTeX and APA format).


## Usage

To generate a project using this template, follow these steps:
1. Install cookiecutter CLI, e.g. using PIP: `pip install --user cookiecutter`,
2. Navigate to the desired directory and run the `cookiecutter https://github.com/Savaed/modern-python.git` command.
3. Go to the root of the project you created (the one where the *README.md* file is located) and run the bash script: `bash sanity-check.sh`.
4. You should see plenty of console outputs, especially with **poetry install, loggin, and pre-commit stufs**.
5. If there are no errors, remove the *sanity-check.sh* script and check the generated files to make any necessary changes.

## Sample project structure
The project tree created with `cookiecutter https://github.com/Savaed/modern-python.git`

```
sample_project/                 < Root directory (flat style)
├── .dockerignore               < Ignore files in Docker builds
├── .env                        < Environment variables
├── .github
│   └── workflows
│       └── main.yaml           < Github Actions CI/CD
├── .gitignore                  < Ignore files in git operations
├── .pre-commit-config.yaml     < pre-commit hooks config
├── .vscode
│   ├── launch.json
│   └── settings.json
├── CITATION.cff                < Let others cite your software
├── Dockerfile                  < Docker build definition
├── LICENSE                     < License [MIT/BSD/ISC/Apache v2.0/GNU v.3]
├── README.md                   < README skeleton file
├── configs
│   └── config.yaml             < Hydra config, see config.py
├── data
│   ├── final                   < Final, pre-processed data
│   │   └── .gitkeep
│   ├── interim                 < Pre-processed temporary data
│   │   └── .gitkeep
│   └── raw                     < Raw, external data
│       └── .gitkeep
├── pyproject.toml              < Project metadata and Python dependencies
├── sample_project
│   ├── config.py               < Pydantic configuration and its validation
│   ├── file.py
│   ├── log.py                  < Loguru minimal structured logging
│   └── scripts
│       └── script1.py
├── sanity-check.sh             < One script to test them all
├── tests                       < Pytest and hypothesis tests
│   ├── conftest.py
│   └── file_test.py
└── tox.ini                     < Environment setup for test/CI
```
