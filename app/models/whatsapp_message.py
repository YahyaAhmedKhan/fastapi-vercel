from pydantic import BaseModel, Field
from typing import Optional

# {
#     "object": "whatsapp_business_account",
#     "entry": [
#       {
#         "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
#         "changes": [
#           {
#             "value": {
#               "messaging_product": "whatsapp",
#               "metadata": {
#                 "display_phone_number": "15550000000",
#                 "phone_number_id": "920388481168316"
#               },
#               "contacts": [
#                 {
#                   "profile": {
#                     "name": "Test User"
#                   },
#                   "wa_id": "15551234567"
#                 }
#               ],
#               "messages": [
#                 {
#                   "from": "15551234567",
#                   "id": "wamid.HBgNMTU1NTEyMzQ1NjcVAgARGBI5QTNDQTVCN0Y4RjhFRkU5MTYA",
#                   "timestamp": "1234567890",
#                   "text": {
#                     "body": "Hello! This is a test message."
#                   },
#                   "type": "text"
#                 }
#               ]
#             },
#             "field": "messages"
#           }
#         ]
#       }
#     ]
#   }
class WhatsAppMessageText(BaseModel):
    body: str

class WhatsAppMessageContent(BaseModel):
    from_number: str = Field(alias="from")
    id: str
    timestamp: str
    text: WhatsAppMessageText
    type: str
    
    class Config:
        populate_by_name = False  

class WhatsAppMessageProfile(BaseModel):
    name: str

class WhatsAppMessageContact(BaseModel):
    profile: WhatsAppMessageProfile
    wa_id: str

class WhatsAppMessageMetadata(BaseModel):
    display_phone_number: str
    phone_number_id: str

class WhatsAppMessageValue(BaseModel):
    messaging_product: str
    metadata: WhatsAppMessageMetadata
    contacts: list[WhatsAppMessageContact]
    messages: list[WhatsAppMessageContent]
    
class WhatsAppMessageChange(BaseModel):
    value: WhatsAppMessageValue
        
class WhatsAppMessageEntry(BaseModel):
    id: str
    changes: list[WhatsAppMessageChange]
    

class WhatsAppMessage(BaseModel):
    object_type: str = Field(alias="object")
    entry: list[WhatsAppMessageEntry]
    
    class Config:
        populate_by_name = True

