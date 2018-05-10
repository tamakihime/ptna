from janome.tokenizer import Tokenizer
import re
import random


def parase(text):
    """
    形態素解析によって形態素を取り出す
    :param text: 　
    :return: 形態素のリスト
    """
    t = Tokenizer() # Tokenizer オブジェクトの生成
    tokens = t.tokenize(text)
    result = [] # 形態素を保存しておくためのリスト
    for token in tokens:
        result.append(token.surface)
    return result


filename = "text.txt"
with open(filename,"r",encoding='utf_8') as f:
    text =f.read()
# 文末の改行文字を取り除く
text = re.sub("\n", "", text)
# 形態素の部分のをリストとして取得
worldlist = parase(text)

# マルコフ辞書の作成
markov = {}
pl = ''
p2 = ''
p3 = ''
for word in worldlist:
    # p1,p2,p3のすべてに値が収納されているかどうかをチェック
    if p1 and p2 and p3:
        # makovに（ｐ1，ｐ2，ｐ3)
        if (p1, p2, p3) not in markov:
            markov[(p1, p2, p3)] = []
        markov[(p1, p2, p3)].append(word)
    p1, p2, p3 = p2, p3, word

# 生成した文章を格納するグローバル変数

sentence = ''

def generate():
    """
    マルコフ辞書から文書を作り出す
    :return:
    """
    global sentence
    count = 0
    #　markovのキーをランダムに抽出し、プレフィックス1～3に代入
    p1,p2,p3 =random.choice(list(markov.keys()))
    count += 1