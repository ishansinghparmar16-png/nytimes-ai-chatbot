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
        # Determine if we're running on Streamlit Cloud
        is_streamlit_cloud = False
        
        if HAS_STREAMLIT:
            try:
                # Check if we're in a Streamlit context and secrets exist
                if hasattr(st, 'secrets') and hasattr(st.secrets, '_secrets'):
                    # Try to access secrets dictionary
                    secrets_dict = dict(st.secrets)
                    if secrets_dict:
                        is_streamlit_cloud = True
                        print("✅ Running on Streamlit Cloud - using secrets")
            except Exception as e:
                print(f"ℹ️  Not using Streamlit secrets: {e}")
                is_streamlit_cloud = False
        
        if is_streamlit_cloud:
            # Running on Streamlit Cloud - use st.secrets
            self.nyt_api_key = str(st.secrets.get("NYT_API_KEY", ""))
            self.openai_api_key = str(st.secrets.get("OPENAI_API_KEY", ""))
            self.anthropic_api_key = str(st.secrets.get("ANTHROPIC_API_KEY", ""))
            self.llm_model = str(st.secrets.get("LLM_MODEL", "gpt-4-turbo-preview"))
            try:
                self.llm_temperature = float(st.secrets.get("LLM_TEMPERATURE", "0.7"))
            except (ValueError, TypeError):
                self.llm_temperature = 0.7
        else:
            # Running locally - use environment variables
            print("ℹ️  Running locally - loading from .env file")
            from dotenv import load_dotenv
            load_dotenv()
            
            self.nyt_api_key = os.getenv("NYT_API_KEY", "")
            self.openai_api_key = os.getenv("OPENAI_API_KEY", "")
            self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", "")
            self.llm_model = os.getenv("LLM_MODEL", "gpt-4-turbo-preview")
            try:
                self.llm_temperature = float(os.getenv("LLM_TEMPERATURE", "0.7"))
            except (ValueError, TypeError):
                self.llm_temperature = 0.7
        
        # Constants
        self.nyt_api_base_url = "https://api.nytimes.com/svc/search/v2"
        self.max_articles_to_fetch = 3
    
    def validate_api_keys(self) -> None:
        """Validate that required API keys are present."""
        if not self.nyt_api_key:
            raise ValueError(
                "NYT_API_KEY must be set. "
                "Local: Add to .env file. "
                "Streamlit Cloud: Add to secrets in Advanced Settings"
            )
        
        if not self.openai_api_key and not self.anthropic_api_key:
            raise ValueError(
                "Either OPENAI_API_KEY or ANTHROPIC_API_KEY must be set. "
                "Local: Add to .env file. "
                "Streamlit Cloud: Add to secrets in Advanced Settings"
            )


# Global settings instance
try:
    settings = Settings()
    settings.validate_api_keys()
except Exception as e:
    print(f"⚠️  Configuration Error: {e}")
    raise

