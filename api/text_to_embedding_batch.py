from typing import List

from fastapi import APIRouter

from api.schema import (
    EmbeddingBatchDataResponse,  # 导入EmbeddingBatchDataResponse数据模型 Import the EmbeddingBatchDataResponse data model
    EmbeddingBatchParams,  # 导入EmbeddingBatchParams数据模型 Import the EmbeddingBatchParams data model
    EmbeddingBatchResponse,  # 导入EmbeddingBatchResponse数据模型 Import the EmbeddingBatchResponse data model
)
from service.m3e_funcs import (
    encode_sentence_with_m3e,
)  # 导入嵌入函数 Import the embedding function

router = APIRouter()


@router.post(path="/", response_model=EmbeddingBatchResponse)
async def api_text_to_embedding_batch(param: EmbeddingBatchParams):
    try:
        # 创建嵌入数据的响应列表，用于存储每个文本的嵌入数据
        # Create a response list for embedding data, used to store embedding data for each text
        response_list: List[EmbeddingBatchDataResponse] = [
            EmbeddingBatchDataResponse(
                text=text,
                embedding=encode_sentence_with_m3e(text),
                embedding_length=len(encode_sentence_with_m3e(text)),
            )
            for text in param.original_texts
        ]
        # 返回包含嵌入数据列表和模型字段的嵌入批处理响应
        # Return the embedding batch response containing the embedding data list and model field
        return EmbeddingBatchResponse(data=response_list, model=param.model)
    except Exception as e:
        # 发生异常时返回错误信息
        # Return an error message in case of an exception
        return {"error": str(e)}
