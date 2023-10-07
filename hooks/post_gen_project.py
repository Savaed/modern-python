from pathlib import Path
import shutil
from textwrap import dedent


TIPS = """
✨ Project '{{ cookiecutter.project_slug }}' created successfuly using cookiecutter CLI.

🚀 Take a few next steps:
  - change Python packages versions in pyproject.toml file if needed,
  {%- if cookiecutter.add_citation -%}
  - check CITATION.cff file,
  {%- endif %}
  {%- if cookiecutter.use_github_actions %}
  - check .github/* files,
  {%- endif %}
  - check README.md file,
  {%- if cookiecutter.license != 'none' %}
  - check LICENSE file,
  {%- endif %}
  - check .pre-commit-config.yaml file,
  - check tox.ini file,
  - check .gitignore file,
  - run `cd {{ cookiecutter.project_slug }} && bash sanity-check.sh` to check
    if everthing was created correctly.
  - remove sanity-check.sh script.

🎉 Happy coding
"""


def remove_unnecessary_dirs():
    project_dir = Path.cwd()

    # Creating conditional directories using name templates e.g. {% raw %}{{ 'dir' if condition_is_true }} {% endraw %}
    # is buggy, so create them all first and then remove the ones you don't need. Conditional files
    # can be safely templated.

    if not {{cookiecutter.use_vscode}}:
        vscode_dir = project_dir / ".vscode"
        shutil.rmtree(vscode_dir)

    if not {{cookiecutter.use_github_actions}}:
        github_dir = project_dir / ".github"
        shutil.rmtree(github_dir)


def main() -> int:
    remove_unnecessary_dirs()
    print(dedent(TIPS))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
