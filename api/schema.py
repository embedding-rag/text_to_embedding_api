from typing import List

from pydantic import BaseModel


# 请求参数模型，包含单个文本的嵌入参数
class EmbeddingParam(BaseModel):
    text: str
    model: str = "m3e-base"


# 用于表示嵌入响应的数据模型，包含原始文本和计算得到的嵌入
class EmbeddingResponse(BaseModel):
    text: str
    embedding: list
    embedding_length: int
    model: str


# 请求参数模型，包含字符串列表的嵌入批处理参数
class EmbeddingBatchParams(BaseModel):
    original_texts: List[str]  # 仅包含原始文本
    model: str = "m3e-base"


# 批量转换返回的单个嵌入响应
class EmbeddingBatchDataResponse(BaseModel):
    text: str
    embedding: list
    embedding_length: int


# 批量转换返回的数据模型，包含字符串列表的嵌入批处理响应
class EmbeddingBatchResponse(BaseModel):
    data: List[EmbeddingBatchDataResponse]
    model: str
