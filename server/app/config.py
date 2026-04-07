"""Configuration for SynBioInventory backend."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="SYNBIOHUB_", extra="ignore")

    base_url: str = "https://example-synbiohub.org"
    use_stub: bool = True


settings = Settings()
