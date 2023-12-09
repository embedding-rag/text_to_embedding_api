# API 文档

## Ping 路由

- **访问地址：** `/ping`
- **请求参数：** 无
- **返回格式：** JSON对象，包含 "message" 字段，用于测试API是否正常工作。

## Text to Embedding 单个文本转嵌入路由

- **访问地址：** `/text_to_embedding`
- **请求参数：** 
  - JSON对象，使用 `EmbeddingParam` 模型。
    ```json
    {
      "text": "Your Text Here",
      "model": "m3e-base"
    }
    ```
- **返回格式：** 
  - JSON对象，使用 `EmbeddingResponse` 模型。
    ```json
    {
      "text": "Your Text Here",
      "embedding": [ ... ],
      "embedding_length": 123,
      "model": "m3e-base"
    }
    ```

## Text to Embedding 批处理路由

- **访问地址：** `/text_to_embedding_batch`
- **请求参数：** 
  - JSON对象，使用 `EmbeddingBatchParams` 模型。
    ```json
    {
      "original_texts": ["Text 1", "Text 2"],
      "model": "m3e-base"
    }
    ```
- **返回格式：** 
  - JSON对象，使用 `EmbeddingBatchResponse` 模型。
    ```json
    {
      "data": [
        {
          "text": "Text 1",
          "embedding": [ ... ],
          "embedding_length": 123
        },
        {
          "text": "Text 2",
          "embedding": [ ... ],
          "embedding_length": 456
        }
      ],
      "model": "m3e-base"
    }
    ```

