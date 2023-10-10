{% if cookiecutter.use_hypothesis -%}
import os
{% endif -%}
from typing import Any, Iterator

import pytest
{%- if cookiecutter.use_hypothesis %}
from hypothesis import settings
{% endif %}
from loguru import logger
from pytest import LogCaptureFixture

from {{cookiecutter.project_slug}}.log import format_key_value_context
{% if cookiecutter.use_hypothesis %}

settings.register_profile("ci", max_examples=250)

if os.getenv("CI", False):
    settings.load_profile("ci")
else:
    settings.load_profile("default")
{% endif %}

@pytest.fixture
def sample_global_fixture(request: Any) -> Any:
    """Always return the value passed."""
    return request.param


@pytest.fixture
def loguru_caplog(caplog: LogCaptureFixture) -> Iterator[LogCaptureFixture]:
    try:
        handler_id = logger.add(
            caplog.handler,
            format=format_key_value_context,
            level="DEBUG",
            filter=lambda record: record["level"].no >= caplog.handler.level,
            enqueue=False,  # Set to 'True' if your test is spawning child processes.
        )
        yield caplog
    finally:
        logger.remove(handler_id)
