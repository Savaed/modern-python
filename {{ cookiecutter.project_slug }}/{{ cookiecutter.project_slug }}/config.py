from pydantic import BaseModel, constr


class SomeConfig(BaseModel):
    key1: str = constr(min_length=2)
    key2: dict[str, int]


class AppConfig(BaseModel):
    config: SomeConfig
