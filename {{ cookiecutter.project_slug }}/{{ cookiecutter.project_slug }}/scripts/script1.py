import hydra
from omegaconf import OmegaConf

from {{cookiecutter.project_slug}}.config import AppConfig
from {{cookiecutter.project_slug}}.log import logger


@hydra.main("../../configs", "config", "1.3")
def main(cfg: AppConfig) -> int:
    cfg = AppConfig(**OmegaConf.to_object(cfg))
    logger.bind(key1=[1, 2, 3], key2=type(0)).success("Hello!")
    print(cfg.model_dump())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
