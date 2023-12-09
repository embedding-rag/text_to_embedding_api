from datetime import datetime

from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/")
async def api_ping(request: Request):
    try:
        client_host = request.client.host
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "client_host": client_host,
            "current_time": current_time,
            "description": "This API provides embedding services for text data.",
        }
    except Exception as e:
        return {"error": str(e)}
