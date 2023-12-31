import string
import tempfile
from pathlib import Path

import hypothesis.strategies as st
from cookiecutter.main import cookiecutter
from hypothesis import event, given


LETTERS_AND_DIGITS = string.ascii_letters + string.digits
DISALLOWED_NAME_CHARACTERS = set(string.digits + string.punctuation) - set("-.'")

versions = st.sampled_from(
    [
        "3",
        "3.1",
        "3.1.1",
        "3.11.1",
        "3.1.0",
        "3.10",
        "0.1.0",
        "0.0.0",
        "1.0.0",
        "1.1.1.1.1.11.1",
    ],
)

cookiecutter_configs = st.fixed_dictionaries(
    {
        "project_name": st.text(min_size=1, alphabet=f"{LETTERS_AND_DIGITS}-_. ").map(
            lambda name: "test_name" if name.isspace() else name,
        ),
        "project_slug": st.text(min_size=1, alphabet=f"{LETTERS_AND_DIGITS}-_.").map(
            lambda slug: "test_slug" if slug.strip("./").isspace() else slug,
        ),
        "friendly_name": st.text(min_size=1),
        "author": st.text(
            min_size=1,
            alphabet=string.ascii_letters + ". -'",
        ).map(
            lambda author: "author" if author.strip("-.' ").isspace() else author,
        ),  # Not the best solustion as it cannot generate non standard characters
        "github_user": st.text(min_size=1, alphabet=string.printable),
        "mail": st.emails(),
        "project_description": st.text(min_size=1, alphabet=string.printable),
        "version": versions,
        "python_version": versions,
        "poetry_version": versions,
        "tox_version": versions,
        "git_main_branch": st.text(min_size=1, alphabet=f"{LETTERS_AND_DIGITS}_-./"),
        "use_vscode": st.booleans(),
        "use_hypothesis": st.booleans(),
        "use_docker": st.booleans(),
        "use_pre_commit_ci": st.booleans(),
        "use_github_actions": st.booleans(),
        "github_ci_os": st.text(min_size=1),
        "codecov_token_name": st.text(alphabet=f"{LETTERS_AND_DIGITS}-_"),
        "add_citation": st.booleans(),
        "line_length": st.integers(min_value=1, max_value=120),
        "license": st.sampled_from(
            [
                "MIT",
                "BSD",
                "ISC",
                "Apache Software License 2.0",
                "GNU General Public License v3",
                "none",
            ],
        ),
        "__python_version_str": st.sampled_from(["31", "311", "38", "310"]),
        "__current_year": st.integers(min_value=1, max_value=3000),
    },
)


@given(cookiecutter_configs)
def test_cookiecutter__run_without_errors(cfg: dict[str, str | int | bool]) -> None:
    """Test that for valid inputs the function runs without errors."""
    template_path = Path(__file__).parents[1].as_posix()

    with tempfile.TemporaryDirectory() as tmp_dir:
        project_path = cookiecutter(
            template_path,
            no_input=True,
            extra_context=cfg,
            output_dir=tmp_dir,
        )
        files_num = len(list(Path(project_path).iterdir()))

    event(f"Files created: {files_num}")
    assert files_num >= 10  # 10 files are the minimum that can be created
