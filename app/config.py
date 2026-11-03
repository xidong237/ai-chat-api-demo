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
    DEEPSEEK_API_KEY: str = "sk-123"
    DEEPSEEK_BASE_URL: str = "https//api.deepseek.com"
    deepseek_model: str = "deepseek-v4-flash"

    # ===== OpenAI 配置 =====
    OPENAI_API_KEY: str = ""
    OPENAI_BASE_URL: str = "https://api.openai.com/v1"
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

    @property
    def available_models(self) -> list[dict]:
        """返回当前已配置的可用模型列表"""
        models = []
        if self.DEEPSEEK_API_KEY:
            models.append({
                "id": "deepseek",
                "name": "DeepSeek-V4-flash",
                "provider": "DeepSeek",
                "description": "高性价比通用模型，中文能力强",
            })
        if self.OPENAI_API_KEY:
            models.append({
                "id": "openai",
                "name": self.openai_model,
                "provider": "OpenAI",
                "description": "综合能力最强的模型之一",
            })
        return models


# 全局单例——用 lru_cache 保证只初始化一次
@lru_cache()
def get_settings() -> Settings:
    return Settings()
