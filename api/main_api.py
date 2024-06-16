import asyncio
import traceback

from common.config_handler import get_config
from fastapi import APIRouter


from common.response_handler import success, error
from popo.word_frequency_vo import WordFrequencyResponse
from services.word_frequency import split_word_count_frequency
from services.sentiment_analysis import emotional_analy

router = APIRouter()
my_config = get_config()


@router.get("/emotional_analysis")
def run_main(comment: str):
    try:
        # 分词和词频统计
        word_frequency_dict = split_word_count_frequency(comment)

        # 情感分析
        negative_prob, positive_prob = emotional_analy(comment)

        response = WordFrequencyResponse(
            word_frequency_dict=word_frequency_dict,
            negative_prob=negative_prob,
            positive_prob=positive_prob
        )

        return success(data=response)
    except Exception as e:
        print(e)
        return error(message="系统异常！")
