from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Run(BaseModel):
    app: str = "main:app"
    host: str = "127.0.0.1"
    port: int = 8000


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=[BASE_DIR / ".env_template", BASE_DIR / ".env"],
        env_prefix="APP_CONFIG_",
        env_nested_delimiter="__",
        case_sensitive=False,
    )

    run: Run = Field(default_factory=Run)


settings = Settings()
