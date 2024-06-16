import logging

from transformers import BertForSequenceClassification
from transformers import BertTokenizer
import torch


def emotional_analy(comment):
    """
    加载预训练模型，进行文本情感分析

    :return: 正面和负面情感概率
    """
    try:
        # 加载tokenizer
        tokenizer = BertTokenizer.from_pretrained('/home/user/algorithm/wz/Roberta-330M-Sentiment_model/model/')
        # 加载预训练模型
        model = BertForSequenceClassification.from_pretrained(
            '/home/user/algorithm/wz/Roberta-330M-Sentiment_model/model/')
    except Exception as e:
        print("检查模型路径是否正确")
    else:
        text = comment
        # 对text进行编码
        indexed_tokens = tokenizer.encode(text)

        tokens_tensor = torch.tensor([indexed_tokens])
        output = model(tokens_tensor)
        # 概率分布
        probabilities = torch.nn.functional.softmax(output.logits, dim=-1)

        # 正面和负面情感概率，保留两位小数点
        positive_prob = round(probabilities[0][1].item(), 2)
        negative_prob = round(probabilities[0][0].item(), 2)

        print(f"负面情感概率: {negative_prob:.4f}")
        print(f"正面情感概率: {positive_prob:.4f}")

        return positive_prob, negative_prob


if __name__ == '__main__':
    text = "今天心情好"
    emotional_analy(text)
