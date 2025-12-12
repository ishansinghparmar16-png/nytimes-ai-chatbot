"""
Configuration management for NY Times AI Chatbot.
All sensitive credentials are loaded from environment variables or Streamlit secrets.
"""
import os
from typing import Optional

# Try to import streamlit for cloud deployment
try:
    import streamlit as st
    HAS_STREAMLIT = True
except ImportError:
    HAS_STREAMLIT = False


class Settings:
    """Application settings loaded from environment variables or Streamlit secrets."""
    
    def __init__(self):
        # Try Streamlit secrets first (for Streamlit Cloud), then fall back to env vars
        if HAS_STREAMLIT and hasattr(st, 'secrets') and len(st.secrets) > 0:
            # Running on Streamlit Cloud - use st.secrets
            self.nyt_api_key = st.secrets.get("NYT_API_KEY", "")
            self.openai_api_key = st.secrets.get("OPENAI_API_KEY", "")
            self.anthropic_api_key = st.secrets.get("ANTHROPIC_API_KEY", "")
            self.llm_model = st.secrets.get("LLM_MODEL", "gpt-4-turbo-preview")
            self.llm_temperature = float(st.secrets.get("LLM_TEMPERATURE", "0.7"))
        else:
            # Running locally - use environment variables
            from dotenv import load_dotenv
            load_dotenv()
            
            self.nyt_api_key = os.getenv("NYT_API_KEY", "")
            self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
            self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", "")
            self.llm_model = os.getenv("LLM_MODEL", "gpt-4-turbo-preview")
            self.llm_temperature = float(os.getenv("LLM_TEMPERATURE", "0.7"))
        
        # Constants
        self.nyt_api_base_url = "https://api.nytimes.com/svc/search/v2"
        self.max_articles_to_fetch = 3
    
    def validate_api_keys(self) -> None:
        """Validate that required API keys are present."""
        if not self.nyt_api_key:
            raise ValueError("NYT_API_KEY must be set in environment variables or Streamlit secrets")
        
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
    print("Please create a .env file based on .env.example or add secrets in Streamlit Cloud")
    raise

