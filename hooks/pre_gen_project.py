import re
import string

LETTERS_AND_DIGITS = string.ascii_letters + string.digits

PROJECT_NAME = "{{ cookiecutter.project_name }}"
PACKAGE_NAME = "{{ cookiecutter.project_slug }}"
EMAIL = "{{ cookiecutter.mail }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"
POETRY_VERSION = "{{ cookiecutter.poetry_version }}"
TOX_VERSION = "{{ cookiecutter.tox_version }}"
AUTHOR = "{{ cookiecutter.author }}"

INVALID_VERSION_MSG = "is invalid. Examples of valid package versions are: '0.3', '3', '3.1', '3.11.0' etc."
VALID_PROJECT_NAME_PATTERN = set(f"{LETTERS_AND_DIGITS}-_. ")
VALID_PACKAGE_NAME_PATTERN = set(f"{LETTERS_AND_DIGITS}-_.")
DISALLOWED_NAME_CHARACTERS = set(string.digits + string.punctuation) - set("-.'")
EMAIL_REGEX = "(?P<username>[\.\w\-\!~#$%&\|{}\+\/\^\`\=\*']+).(?P<domain>[\w\.\-]+)"


def is_invalid_version(version: str) -> bool:
    return any(
        [
            version.startswith("."),
            version.endswith("."),
            not version.replace(".", "").isdigit(),
        ],
    )


def main() -> int:
    if is_invalid_version(PYTHON_VERSION):
        raise ValueError(f"{PYTHON_VERSION=} {INVALID_VERSION_MSG}")

    if is_invalid_version(POETRY_VERSION):
        raise ValueError(f"{POETRY_VERSION=} {INVALID_VERSION_MSG}")

    if is_invalid_version(TOX_VERSION):
        raise ValueError(f"{TOX_VERSION=} {INVALID_VERSION_MSG}")

    # Name cannot contain only special characters like ' ', ''', '-', '.'
    if DISALLOWED_NAME_CHARACTERS.intersection(AUTHOR) or not AUTHOR.strip("-.' "):
        raise ValueError(
            f"{AUTHOR=} name is invalid. Author name cannot contain digits and punctuation characters other than '-', '.' and '",
        )

    if not PACKAGE_NAME.strip(" .") or not set(PACKAGE_NAME).issubset(
        VALID_PACKAGE_NAME_PATTERN,
    ):
        raise ValueError(
            f"{PACKAGE_NAME=} is invalid. Package name can only contains numbers, letters and '_', '-', '.'",
        )

    if not PROJECT_NAME.strip() or not set(PROJECT_NAME).issubset(
        VALID_PROJECT_NAME_PATTERN,
    ):
        raise ValueError(
            f"{PROJECT_NAME=} is invalid. Project name can only contains numbers, letters, '_', '-', '.'  and spaces",
        )

    if not re.match(EMAIL_REGEX, EMAIL):
        raise ValueError(f"{EMAIL=} is not a valid email address")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
