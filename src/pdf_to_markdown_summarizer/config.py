from typing import Any

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    OPENAI_API_KEY: str | None = None
    OPENAI_BASE_URL: str = "https://api.openai.com/v1"
    GEMINI_API_KEY: str | None = None
    GEMINI_BASE_URL: str = "https://generativelanguage.googleapis.com"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: Any,
        env_settings: Any,
        dotenv_settings: Any,
        file_secret_settings: Any,
    ) -> tuple[Any, ...]:
        return (
            init_settings,
            dotenv_settings,
            env_settings,
        )

    @field_validator("OPENAI_API_KEY")
    def validate_openai_api_key(cls, v):
        if v is not None and v.startswith("*"):
            raise ValueError(
                "OPENAI_API_KEY cannot start with *. Please provide a valid API key via environment variable or .env file."
            )
        return v

    @field_validator("GEMINI_API_KEY")
    def validate_gemini_api_key(cls, v):
        if v is not None and v.startswith("*"):
            raise ValueError(
                "GEMINI_API_KEY cannot start with *. Please provide a valid API key via environment variable or .env file."
            )
        return v


config = Config()
