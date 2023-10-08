from hydra import compose, initialize
from pytest import CaptureFixture, LogCaptureFixture

from {{cookiecutter.project_slug}}.scripts.script1 import main


def test_main__console_log(loguru_caplog: LogCaptureFixture) -> None:
    """Test that the `script1.main()` logs are correct."""
    expected = "[SUCCESS ] Hello!                                             {{cookiecutter.project_slug}}.scripts.script1:main:11    key1=[1, 2, 3] key2=<class 'int'>" # noqa

    with initialize(version_base="1.3", config_path="../configs"):
        cfg = compose(config_name="config")

    main(cfg)
    assert expected in loguru_caplog.text


def test_main__console_print_config(capsys: CaptureFixture) -> None:
    """Test that the `script1.main()` console print is the actual Hydra configuration."""
    expected = "{'config': {'key1': 'value', 'key2': {'sub_key1': 1, 'sub_key2': 2}}}"

    with initialize(version_base="1.3", config_path="../configs"):
        cfg = compose(config_name="config")

    main(cfg)
    captured = capsys.readouterr()
    assert expected in captured.out
