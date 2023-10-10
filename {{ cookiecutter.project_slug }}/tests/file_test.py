{% if cookiecutter.use_hypothesis -%}
from hypothesis import given
from hypothesis import strategies as st
{% endif -%}
import pytest

from {{cookiecutter.project_slug}}.file import add_two


@pytest.mark.parametrize("sample_global_fixture", [0.3, 1.0, 2.6], indirect=True)
def test_add_two__add_correctly(sample_global_fixture: float) -> None:
    """Test that this function correctly adds 2 to `x`."""
    expected = sample_global_fixture + 2
    actual = add_two(sample_global_fixture)
    assert actual == expected
{% if cookiecutter.use_hypothesis %}

@given(st.floats(allow_nan=False, allow_infinity=False))
def test_add_two__add_correctly_hypothesis_version(x: float) -> None:
    """Test that this function correctly adds 2 to `x`.

    This version uses the `hypothesis` library.
    """
    expected = x + 2
    actual = add_two(x)
    assert actual == expected
{% endif -%}
