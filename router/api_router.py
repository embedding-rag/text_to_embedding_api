from fastapi import APIRouter

from api.ping import router as ping_router
from api.text_to_embedding import router as text_to_embedding_router
from api.text_to_embedding_batch import router as text_to_embedding_batch_router

api_router = APIRouter()

api_router.include_router(router=ping_router, prefix="/ping", tags=["ping"])
api_router.include_router(
    router=text_to_embedding_router,
    prefix="/text_to_embedding",
    tags=["text_to_embedding"],
)
api_router.include_router(
    router=text_to_embedding_batch_router,
    prefix="/text_to_embedding_batch",
    tags=["text_to_embedding"],
)
