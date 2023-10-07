#### {{ cookiecutter.friendly_name }}


[![Python {{ cookiecutter.python_version }}](https://img.shields.io/badge/python-{{ cookiecutter.python_version.split('.')[:2] | join('.') }}-blue.svg)](https://www.python.org/downloads)

{% if cookiecutter.use_pre_commit_ci -%}
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pre-commit/main.svg)](https://results.pre-commit.ci/latest/github/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}/{{ cookiecutter.git_main_branch }})

{% else %}
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
{%- endif %}

[![workflow](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}/actions/workflows/main.yaml/badge.svg)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}/actions)

[![codecov](https://codecov.io/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }}/branch/{{ cookiecutter.git_main_branch }}/graph/badge.svg?token=D482CSZ7MJ)](https://codecov.io/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.project_slug }})

[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://docs.astral.sh/ruff/)

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

{{ cookiecutter.project_description }}


## Features

- TODO

## Requirements

- TODO

## Installation

You can install _{{cookiecutter.friendly_name}}_ via [pip] from [PyPI]:

```console
$ pip install {{cookiecutter.project_slug}}
```

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

{% if cookiecutter.license != 'none' -%}
## License

Distributed under the terms of the [{{ cookiecutter }} license][license],
_{{cookiecutter.friendly_name}}_ is free and open source software.
{% endif -%}

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

<!-- github-only -->

[pypi]: https://pypi.org/
[pip]: https://pip.pypa.io/
{%- if cookiecutter.license != 'none' -%}
[license]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_slug}}/blob/{{ cookiecutter.git_main_branch }}/LICENSE
{% endif -%}
