"""Application configuration."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "SynBioInventory API"
    synbiohub_base_url: str = "https://example.synbiohub.org"
    synbiohub_use_stub: bool = True
    max_upload_mb: int = 10

    model_config = SettingsConfigDict(env_file=".env", env_prefix="", extra="ignore")


settings = Settings()
