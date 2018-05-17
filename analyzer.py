from janome.tokenizer import Tokenizer
import re

def analyze(text):
    """
    形態素解析を行う
    :param text:
    :return:
    """
    t = Tokenizer()
    tokens = t.tokenize(text)
    result = []

    # リストからTokenオブジェクトを一つずつ取り出す
    for token in tokens:
        result.append(
            [token.surface,
             token.part_of_speech])
    return (result)


def keyword_check(part):
    """
    品詞が名詞であるかどうかを調べる
    :param part:
    :return:
    """
    return re.match('名詞,(一般|固有名詞|サ変接続|形容動詞語幹)', part)

def parse(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    result = []
    for token in tokens:
        result.append(token.surface)
        return (result)