from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from datetime import datetime
from app.core.config import settings
from app.core.logger import logger
from app.services.message_handler import MessageHandler



app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)


@app.get("/", response_class=JSONResponse)
def read_root():
    return JSONResponse({
        "message": "Hello, World!"
    })


@app.get("/webhook", response_class=PlainTextResponse)
async def verify_webhook(
    mode: str = Query(alias="hub.mode"),
    token: str = Query(alias="hub.verify_token"),
    challenge: str = Query(alias="hub.challenge")
):
    """
    WhatsApp webhook verification endpoint.
    Meta will call this to verify your webhook URL.
    """
    if mode == "subscribe" and token == settings.WHATSAPP_VERIFY_TOKEN:
        return challenge
    else:
        return PlainTextResponse("Forbidden", status_code=403)


@app.post("/webhook")
async def receive_webhook(request: Request):
    """
    WhatsApp webhook endpoint for receiving messages and events.
    """
    try:
        body = await request.json()
        logger.info(f"Received webhook: {body}")
        message_handler = MessageHandler()
        message_handler.handle_message(body)
        return JSONResponse({"status": "success", "message": body}, status_code=200)
    
    except Exception as e:
        logger.error(f"Error processing webhook: {e}", exc_info=True)
        return JSONResponse({"status": "error", "message": str(e)}, status_code=200)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
