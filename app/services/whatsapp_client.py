"""
WhatsApp Client Service
Handles all outgoing communication with WhatsApp Business API
"""
import httpx
from typing import Optional, Dict, Any
from app.core.config import settings
from app.core.logger import logger


class WhatsAppClient:
    """
    Client for WhatsApp Business API
    Handles sending messages and media
    """
    
    def __init__(self):
        self.phone_number_id = settings.WHATSAPP_PHONE_NUMBER_ID
        self.access_token = settings.WHATSAPP_ACCESS_TOKEN
        self.api_version = settings.META_API_VERSION
        self.base_url = f"https://graph.facebook.com/{self.api_version}"
    
    

    
    async def download_media(self, media_id: str) -> bytes:
        """
        Download media file from WhatsApp
        
        Args:
            media_id: Media ID from webhook
            
        Returns:
            Media file bytes
        """
        try:
            # Step 1: Get media URL
            url = f"{self.base_url}/{media_id}"
            headers = {"Authorization": f"Bearer {self.access_token}"}
            
            async with httpx.AsyncClient() as client:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                media_info = response.json()
                
                # Step 2: Download media from URL
                media_url = media_info["url"]
                media_response = await client.get(media_url, headers=headers)
                media_response.raise_for_status()
                
            logger.info(f"Downloaded media {media_id}")
            return media_response.content
            
        except Exception as e:
            logger.error(f"Media download error: {str(e)}")
    
    
    async def mark_as_read(self, message_id: str) -> None:
        """
        Mark message as read
        
        Args:
            message_id: Message ID to mark as read
        """
        # Call WhatsApp API to mark message as read

        try:
            url = f"{self.base_url}/{self.phone_number_id}/messages"
            headers = {"Authorization": f"Bearer {self.access_token}"}
            payload = {
                "messaging_product": "whatsapp",
                "status": "read",
                "message_id": message_id
            }
            async with httpx.AsyncClient() as client:
                response = await client.post(url, headers=headers, json=payload)
                response.raise_for_status()
        except Exception as e:
            logger.error(f"Error marking message as read: {str(e)}")