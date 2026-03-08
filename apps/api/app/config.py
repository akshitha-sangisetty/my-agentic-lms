from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ─── Database ─────────────────────────────────────────────
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/agentic_lms"
    valkey_url: str = "valkey://localhost:6379/0"
    weaviate_url: str = "http://localhost:8080"
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"

    # ─── MinIO ────────────────────────────────────────────────
    minio_endpoint: str = "localhost:9000"
    minio_access_key: str = "minioadmin"
    minio_secret_key: str = "minioadmin"
    minio_bucket: str = "agentic-lms-uploads"
    minio_secure: bool = False

    # ─── vLLM ─────────────────────────────────────────────────
    vllm_base_url_primary: str = "http://localhost:8000/v1"
    vllm_base_url_fast: str = "http://localhost:8001/v1"
    vllm_base_url_vision: str = "http://localhost:8002/v1"
    vllm_model_primary: str = "Qwen/Qwen2.5-72B-Instruct-AWQ"
    vllm_model_fast: str = "Qwen/Qwen2.5-7B-Instruct"
    vllm_model_vision: str = "Qwen/Qwen2.5-VL-7B-Instruct"

    # ─── Embeddings ───────────────────────────────────────────
    embedding_model: str = "BAAI/bge-m3"
    embedding_device: str = "cpu"

    # ─── Auth ─────────────────────────────────────────────────
    keycloak_url: str = "http://localhost:8081"
    keycloak_realm: str = "agentic-lms"
    jwt_secret: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 60

    # ─── Feature Flags ───────────────────────────────────────
    enable_dynamic_hint_pricing: bool = False
    enable_debate_bot: bool = False
    enable_economy_balancing: bool = False

    # ─── App ──────────────────────────────────────────────────
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    cors_origins: str = "http://localhost:3000"
    debug: bool = True

    model_config = {"env_file": ".env.local", "env_file_encoding": "utf-8"}


settings = Settings()
