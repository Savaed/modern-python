echo 'Performing sanity checks...'

pip --quiet install --user pre-commit poetry=={{ cookiecutter.poetry_version }} tox=={{ cookiecutter.tox_version }}
poetry update && poetry install

git init && git add . && git status

pre-commit install && pre-commit run --all-files
poetry run python -m {{ cookiecutter.project_slug }}.scripts.script1
poetry run coverage run -m pytest tests -v
poetry run coverage report

cd ..
echo 'Done'
