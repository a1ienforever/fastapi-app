from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    db_url: str | None = None
    model_config = SettingsConfigDict(env_file=".env")
