from pathlib import Path

from pydantic import BaseModel, Field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Run(BaseModel):
    app: str = "main:app"
    host: str = "127.0.0.1"
    port: int = 8000


class DatabaseConfig(BaseModel):
    """
    params:
        url - expected as `async` compatible, received via .env
        metadata - configuration for alembic on naming convention
    """
    url: PostgresDsn
    echo: bool = True


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=[BASE_DIR / ".env_template", BASE_DIR / ".env"],
        env_prefix="APP_CONFIG_",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="allow"
    )

    run: Run = Field(default_factory=Run)
    db: DatabaseConfig = Field(default_factory=DatabaseConfig)


settings = Settings()
