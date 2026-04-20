from pathlib import Path
from typing import Any

import yaml
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


def _load_yaml() -> dict[str, Any]:
    path = Path(__file__).parent.parent / "config.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


_yaml = _load_yaml()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Secrets from .env
    discord_token: str
    anthropic_api_key: str
    voyage_api_key: str
    qdrant_url: str = f"http://{_yaml['qdrant']['host']}:{_yaml['qdrant']['port']}"
    qdrant_api_key: str | None = None
    redis_url: str = f"redis://{_yaml['redis']['host']}:{_yaml['redis']['port']}"
    vault_path: Path

    # Non-secret settings sourced from config.yaml
    llm_model_id: str = _yaml["llm"]["model_id"]
    embedding_model_id: str = _yaml["embeddings"]["model_id"]
    embedding_dimensions: int = _yaml["embeddings"]["dimensions"]

    qdrant_collection: str = _yaml["qdrant"]["collection"]

    cache_ttl_seconds: int = _yaml["redis"]["cache_ttl_seconds"]

    chunk_size: int = _yaml["rag"]["chunk_size"]
    chunk_overlap: int = _yaml["rag"]["chunk_overlap"]
    retrieval_top_k: int = _yaml["rag"]["retrieval_top_k"]
    retrieval_confidence_threshold: float = _yaml["rag"]["retrieval_confidence_threshold"]
    cache_similarity_threshold: float = _yaml["rag"]["cache_similarity_threshold"]

    voice_inactivity_timeout: int = _yaml["voice"]["inactivity_timeout_seconds"]
    wake_phrases: list[str] = _yaml["voice"]["wake_phrases"]
    activation_rate_limit_seconds: int = _yaml["voice"]["activation_rate_limit_seconds"]

    @field_validator("qdrant_url", mode="before")
    @classmethod
    def ensure_full_url(cls, v: str) -> str:
        if v.startswith("http"):
            return v
        return f"http://{v}"


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
