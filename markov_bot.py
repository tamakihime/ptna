import re
import random
from analyzer import *


class Markov:
    def make(self):
        """
        マルコフ連鎖尾利用して文章を作り出す
        :return:
        """
        print('テキストを読み込んでいます...')
        filename = "bocchan.txt"
        with open(filename, "r", encoding='utf_8') as f:
            text = f.read()
        text = re.sub("\n", "", text)
        wordlist = parse(text)
        # マルコフ辞書の作成
        markov = {}
        p1 = ''
        p2 = ''
        p3 = ''
        for word in wordlist:
            # p1,p2,p3のすべての値に格納されているかチェック
            if p1 and p2 and p3:
                # markobに（p1,p2,p3)にキーが存在するかどうかを確認
                if (p1, p2, p3) not in markov:
                    # ない場合は値キーののペアを追加する。
                    markov[(p1, p2, p3)] = []
                # キーのリストにサフィックスを追加（重複あり)
                markov[(p1, p2, p3)].append(word)
            # 3つのぷっれふぃっくの値を置き換え
            p1, p2, p3 = p2, p3, word
        # マルコフ辞書から文章を作成する
        count = 0
        sentence = ''
        # markovのキーをランダム抽出　プレフィックス1～3に代入
        p1, p2, p3 = random.choice(list(markov.keys()))
        # while count < 0
        while count < len(wordlist):
            # キーの存在を確認
            if ((p1, p2, p3) in markov) == True:
                # 文章用の単語を生成
                tmp = random.choice(markov[(p1, p2, p3)])
                # 　取得した値をセンテンスに代入
                sentence += tmp
            # 3つのプレフィックスの値を置き換える
            p1, p2, p3 = p2, p3, tmp
            count += 1
        # 最初に出てくる句点まで取り除く
        sentence = re.sub("^.+?。", "", sentence)
        # 最後の句点（。）から再起を取り除く
        if re.search('.+。', sentence):
            sentence = re.search('.+。', sentence).group()
        # 閉じ括弧を削除
        sentence = re.sub("」", "", sentence)
        # 開き括弧を削除
        sentence = re.sub("「", "", sentence)
        # 全角スペースを削除
        sentence = re.sub("　", "", sentence)

        # 生成した文章を戻り値として返す


##################################
# 　プログラムの起点
##################################
if __name__ == '__main__':
    markov = Markov()
    text = markov.make()
    ans = text.split('。')
    if '' in ans:
        ans.remove('')
    print('会話をはじめましょう。')
    while True:
        message = input('>')
        if ans:
            print(random.choice(ans))
