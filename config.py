"""
Configuration management for NY Times AI Chatbot.
All sensitive credentials are loaded from environment variables.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # NY Times API
    nyt_api_key: str
    nyt_api_base_url: str = "https://api.nytimes.com/svc/search/v2"
    
    # LLM Configuration
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    llm_model: str = "gpt-4-turbo-preview"
    llm_temperature: float = 0.7
    
    # Agent Configuration
    max_articles_to_fetch: int = 3
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    def validate_api_keys(self) -> None:
        """Validate that required API keys are present."""
        if not self.nyt_api_key:
            raise ValueError("NYT_API_KEY must be set in environment variables")
        
        if not self.openai_api_key and not self.anthropic_api_key:
            raise ValueError(
                "Either OPENAI_API_KEY or ANTHROPIC_API_KEY must be set"
            )


# Global settings instance
try:
    settings = Settings()
    settings.validate_api_keys()
except Exception as e:
    print(f"⚠️  Configuration Error: {e}")
    print("Please create a .env file based on .env.example")
    raise

