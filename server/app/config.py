"""Runtime configuration for SynBioInventory backend."""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Environment-backed settings."""

    model_config = SettingsConfigDict(env_prefix="SYNBIO_", extra="ignore")

    app_name: str = "SynBioInventory API"
    use_stub_synbiohub: bool = Field(default=True)
    synbiohub_base_url: str = Field(default="https://example.synbiohub.org")
    max_upload_mb: int = Field(default=10)


settings = Settings()
