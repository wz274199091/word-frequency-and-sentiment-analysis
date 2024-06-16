from typing import Dict, Any
from pydantic import BaseModel


# 定义 Pydantic 模型类
class WordFrequencyResponse(BaseModel):
    word_frequency_dict: Dict[str, int]
    negative_prob: float
    positive_prob: float
