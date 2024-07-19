from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        # env_prefix = "app_"

    # OpenAI
    openai_api_key: str

    # Anthropic
    anthropic_api_key: str


settings = AppSettings()  # type: ignore[call-arg]
