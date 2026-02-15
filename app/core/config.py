"""
Application Configuration
Manages environment variables and application settings
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
import pathlib

env_path = pathlib.Path(__file__).parent.parent.parent / ".env"

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables
    """
    # Security
    WHATSAPP_VERIFY_TOKEN: str  # Token for webhook verification
    WHATSAPP_ACCESS_TOKEN: str  # Meta API access token
 
    # WhatsApp Business API
    WHATSAPP_PHONE_NUMBER_ID: str
    WHATSAPP_BUSINESS_ACCOUNT_ID: str
    META_API_VERSION: str = "v22.0"

    model_config = SettingsConfigDict(env_file=env_path)


settings = Settings()

print(settings)