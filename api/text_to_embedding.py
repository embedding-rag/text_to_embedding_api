from fastapi import APIRouter

from api.schema import EmbeddingParam, EmbeddingResponse
from service.m3e_funcs import encode_sentence_with_m3e

router = APIRouter()


@router.post(path="/", response_model=EmbeddingResponse)
async def api_text_to_embedding(param: EmbeddingParam):
    try:
        embedding_result = encode_sentence_with_m3e(param.text)
        return EmbeddingResponse(
            text=param.text,
            embedding=embedding_result,
            embedding_length=len(embedding_result),
            model=param.model,
        )
    except Exception as e:
        return {"error": str(e)}
