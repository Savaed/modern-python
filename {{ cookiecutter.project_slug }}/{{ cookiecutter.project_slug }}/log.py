import sys
from typing import Any

from loguru import logger


def format_key_value_context(record: dict[str, Any]) -> str:
    fmt_parts = [f"<cyan>{key}</>=<magenta>{value}</>" for key, value in record["extra"].items()]
    fmt = " ".join(fmt_parts)
    # BUG: There is a bug? with internal loguru parser when one of the ['extra'] has '{}' e.g. set
    # or dict and are passed to internal loguru formatter in the form like in line 8.
    # e.g. text: '... data={'A', 'B'} ...'.
{% raw %}
    return f"<dim>{{time:YYYY-MM-DD HH:mm:ss}}</> [<lvl>{{level:<8}}</>] <bold>{{message:<50}}</> <cyan>{{name}}</>:<cyan>{{function}}</>:<cyan>{{line}}</>    {fmt}{{exception}}\n"  # noqa
{% endraw %}

# Remove the default logger.
logger.remove()

# Console structured logs with colours
logger.add(
    sys.stderr,
    format=format_key_value_context,
    colorize=True,
    backtrace=True,
    diagnose=True,
)

# File logs. Same output as console logs
# logger.add(
#     "./logs/{{ cookiecutter.project_slug }}.log",
#     format=format_key_value_context,
#     level="DEBUG",
#     rotation="10 MB",
# )

# JSON serialized logs.
# logger.add(
#     "./logs/{{ cookiecutter.project_slug }}.log.json",
#     level="DEBUG",
#     serialize=True,
#     rotation="10 MB",
# )
