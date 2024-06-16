import jieba
import logging
import json
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# 选择使用的停用词库
# stopword_library = {"中文停用词库": "cn_stopwords", "哈工大停用词库": "hit_stopwords.txt", "百度停用词库": "baidu_stopwords"}


def split_word_count_frequency(texts):
    """
    1. 使用jieba分词
    2. 去除停用词
    3. 统计词频
    :return  词频统计的结果（字典）
    """
    # 分词，存为列表word_list
    word_list = jieba.lcut(texts)
    print(f"分词后的原始结果：{word_list}")

    try:
        # 读取停用词库，存为列表stopword_list
        with open(r'stopwords/hit_stopwords.txt', 'r', encoding='UTF-8') as f:
            stopword_list = f.readlines()
    except Exception as e:
        print("没有停用词txt文件，检查路径是否正确")
    else:
        stopword_list = [stopword.strip("\n") for stopword in stopword_list]
        print(f"停用词库列表：{stopword_list}")

        temp_list = []
        for word in word_list:
            if word not in stopword_list:
                temp_list.append(word)
        print(f"去除停用词之后的结果：{temp_list}")

        # 统计词频
        word_frequency_dict = {}
        for word in temp_list:
            word_frequency_dict[word] = word_frequency_dict.get(word, 0) + 1

        # 按照 频次降序
        word_frequency_dict = {k: v for k, v in
                               sorted(word_frequency_dict.items(), key=lambda item: item[1], reverse=True)}
        print(f"词频统计的结果：{word_frequency_dict}")

        return word_frequency_dict


def move_stopword(stopword_file, split_word_dict):
    """
    读取停用词库,去除评论中包含停用词的词语

    Parameter:
        - stopword_file: 停用词库文件
        - split_word_dict:

    return: 分词后的对象进行去除停用词
    """
    with open(stopword_file, 'r', encoding='UTF-8') as f:
        stopwords_list = f.readlines()
    # 停用词列表
    stopwords_list = [i.strip() for i in stopwords_list]

    # 去除停用词
    new_split_word_dict = {}
    for key, values in split_word_dict.items():
        if key not in stopwords_list:
            new_split_word_dict[key] = values

    return new_split_word_dict


def jieba_split_word(texts):
    """
    使用jieba分词，并且统计所有词的频率
    :param text:
    :return:
    """
    split_word_list = []
    for text in texts:
        words = jieba.lcut(text)

        counts = {}
        for word in words:
            # 去掉单个字符
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        split_word_list.append(counts)

    result_dict = {}
    # 遍历列表中的每个字典
    for d in split_word_list:
        for key, value in d.items():
            # 如果键在结果字典中已经存在，则将值相加
            if key in result_dict:
                result_dict[key] += value
            else:
                result_dict[key] = value

    return result_dict


def drawcounts(word_dict):
    """
    统计词频、绘制柱状图
    Parameter
        - word_dict:
    :return:
    """
    counts = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    # 输出前10个词频最高的单词，根据需求修改
    for i in range(10):
        word, count = counts[i]
        print('{:<10}{:>5}'.format(word, count))
    # 绘制柱状图
    x_word = []
    y_count = []
    for i in range(10):
        word, count = counts[i]
        x_word.append(word)
        y_count.append(count)
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.figure(figsize=(20, 15))
    plt.bar(range(len(y_count)), y_count, color='r', tick_label=x_word, facecolor='#9999ff', edgecolor='white')

    plt.xticks(rotation=45, fontsize=20)
    plt.yticks(fontsize=20)

    plt.title("评论词频统计柱状图", fontsize=24)
    plt.savefig('./work/test/bar_result.jpg')
    plt.show()


def drawcloud(strs):
    """
    绘制词云图
    :param strs:
    :return: None
    """
    wc = WordCloud(font_path="fonts\simhei.ttf", width=500, height=400, mode="RGBA",
                   background_color=None).generate(strs)
    # 显示词云图
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    # 保存文件
    wc.to_file("./work/test/WordCloud.png")


def get_textjson(json_filename):
    """
    读取评论的json文件，清洗评论中一些特殊字符
    Parameter
        - json_filename: 评论json文件，里面: [{},{} ... {} ]

    return: 清洗后的 评论:  ['','' ... '' ]
    """
    with open('work/' + json_filename, 'r', encoding='UTF-8') as file:
        comments = json.loads(file.read())
    text = []
    for con in comments:
        # 去除评论中换行符、制表符等特殊字符
        con = re.sub(r"\n|\t|\r|\r\n|\n\r|\x08|\\", "", con['comment'])
        text.append(con)

    return text
