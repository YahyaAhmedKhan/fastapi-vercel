from pydantic import BaseModel, Field
from typing import Optional

# {
#     "field": "messages",
#     "value": {
#         "messaging_product": "whatsapp",
#         "metadata": {
#             "display_phone_number": "16505551111",
#             "phone_number_id": "123456123"
#         },
#         "contacts": [
#             {
#                 "profile": {
#                     "name": "test user name"
#                 },
#                 "wa_id": "16315551181"
#             }
#         ],
#         "messages": [
#             {
#                 "from": "16315551181",
#                 "id": "ABGGFlA5Fpa",
#                 "timestamp": "1504902988",
#                 "type": "text",
#                 "text": {
#                     "body": "this is a text message"
#                 }
#             }
#         ]
#     }
# }


class WhatsAppMessageText(BaseModel):
    body: str

class WhatsAppMessageProfile(BaseModel):
    name: str
class WhatsAppMessageMetadata(BaseModel):
    display_phone_number: str
    phone_number_id: str

class WhatsAppMessage(BaseModel):
    from_number: str = Field(alias="from")
    id: str
    timestamp: str
    text: WhatsAppMessageText
    type: str

class WhatsAppMessageContact(BaseModel):
    profile: WhatsAppMessageProfile
    wa_id: str

class WhatsAppMessageValue(BaseModel):
    messaging_product: str
    metadata: WhatsAppMessageMetadata
    contacts: list[WhatsAppMessageContact]
    messages: list[WhatsAppMessage]
    
class WhatsAppMessagePayload(BaseModel):
    field: str
    value: WhatsAppMessageValue