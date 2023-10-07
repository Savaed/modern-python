from typing import Any

import pytest


@pytest.fixture
def sample_global_fixture(request: Any) -> Any:
    """Return always passed value."""
    return request.param
