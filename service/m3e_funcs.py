import os
from typing import List, Tuple

from sentence_transformers import SentenceTransformer


def singleton(cls: type) -> type:
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class SingletonM3EModel:
    def __init__(self, model_path: str):
        self.model: SentenceTransformer = SentenceTransformer(model_path)


def get_target_path(relative_path: str) -> str:
    """
    获取目标路径

    Args:
        relative_path (str): 相对路径

    Returns:
        str: 目标路径
    """
    # 获取当前文件的绝对路径
    current_path: str = os.path.abspath(__file__)

    # 构建目标路径
    target_path: str = os.path.join(os.path.dirname(current_path), relative_path)

    return target_path


model_path: str = get_target_path("../models/m3e-base")
m3e_model: SingletonM3EModel = SingletonM3EModel(model_path)


# Our sentences we like to encode
sentences: List[str] = [
    "* Moka 此文本嵌入模型由 MokaAI 训练并开源，训练脚本使用 uniem",
    "* Massive 此文本嵌入模型通过**千万级**的中文句对数据集进行训练",
    "* Mixed 此文本嵌入模型支持中英双语的同质文本相似度计算，异质文本检索等功能，未来还会支持代码检索，ALL in one",
]


# def encode_sentences(sentences: List[str]) -> List[Tuple[str, np.ndarray]]:
#     """
#     对句子进行编码
#
#     Args:
#         sentences (List[str]): 要编码的句子列表
#
#     Returns:
#         List[Tuple[str, np.ndarray]]: 包含句子和对应嵌入向量的列表
#     """
#     # Sentences are encoded by calling model.encode()
#     embeddings = m3e_model.model.encode(sentences)
#     encoded_sentences = [(sentence, embedding)
#                          for sentence, embedding in zip(sentences, embeddings)]
#     return encoded_sentences
def encode_sentences(sentences: List[str]) -> List[Tuple[str, List[float]]]:
    """
    对句子进行编码

    Args:
        sentences (List[str]): 要编码的句子列表

    Returns:
        List[Tuple[str, List[float]]]: 包含句子和对应嵌入向量的列表
    """
    # Sentences are encoded by calling model.encode()
    embeddings = m3e_model.model.encode(sentences)
    encoded_sentences = [
        (sentence, embedding.tolist())
        for sentence, embedding in zip(sentences, embeddings)
    ]
    return encoded_sentences


def encode_sentence_with_m3e(sentence: str) -> List[float]:
    """
    对单个句子进行编码

    Args:
        sentence (str): 要编码的句子

    Returns:
        List[float]: 句子的嵌入向量
    """
    embedding = m3e_model.model.encode([sentence])[0]
    return embedding.tolist()
