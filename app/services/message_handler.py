from cgi import print_form
from app.models.whatsapp_message import WhatsAppMessage
from app.services.whatsapp_client import WhatsAppClient
from app.core.config import settings


class MessageHandler:
    def __init__(self):
        self.whatsapp_client = WhatsAppClient()

    def handle_message(self, message: dict):
        whatsapp_message = WhatsAppMessage(**message)
        print(whatsapp_message)
        try:
            self.whatsapp_client.mark_as_read(message["id"])

        except Exception as e:
            print(f"Error sending read receipt: {e}")

        self.handle_text_message(message)

    def handle_text_message(self, message: dict):
        pass
        # print(f"Received text message: {message}")
        