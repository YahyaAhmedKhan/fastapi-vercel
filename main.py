from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from datetime import datetime
import os


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
    # You should replace this with your actual verify token
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
    
    if mode == "subscribe" and token == VERIFY_TOKEN:
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
        response = JSONResponse({
            "status": "success",
            "body": body,
            "timestamp": datetime.now().isoformat()
        }, status_code=200)
    
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return JSONResponse({"status": "error", "message": str(e)}, status_code=500)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
