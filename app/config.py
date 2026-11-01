"""应用配置--所有环境相关的变量都在这里"""
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """应用配置类--自动从 .env 文件和系统环境变量读取"""
    # ===== 应用基础 =====
    app_name: str = "AI Chat API"
    app_version: str = "0.1.0"
    environment: str = "development" # development / production
    log_level: str = "INFO"

    # ===== 服务器 =====
    host: str = "0.0.0.0"
    port: int = 8000

    # ===== DeepSeek 配置 =====
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https//api.deepseek.com"
    deepseek_model: str = "deepseek-v4-flash"

    # ===== OpenAI 配置 =====
    openai_api_key: str = ""
    openai_base_url: str = "https://api.openai.com/v1"
    openai_model: str = "gpt-5.6-luna"

    # ===== 服务限制 =====
    max_tokens_default: int = 4096
    request_timeout: int = 60  # 秒

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
    }

    @property
    def is_development(self) -> bool:
        return self.environment == "development"


s = Settings()

print(s.is_development)