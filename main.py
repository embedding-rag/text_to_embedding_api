import uvicorn
from fastapi import APIRouter, FastAPI, Request, Response

from router.api_router import api_router

app = FastAPI()

app.include_router(router=api_router)


# 中间件函数，用于过滤特定请求
@app.middleware("http")
async def filter_requests(request: Request, call_next):
    if request.url.path in ["/favicon.ico", "/robots.txt"]:
        return Response(status_code=200)
    response = await call_next(request)
    return response


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug",
        workers=1000,
        limit_concurrency=1000,
        access_log=True,
    )
