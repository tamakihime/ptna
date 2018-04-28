import random
import re

class Dictionary:
    def __init__(self):
        self.random = []
        # ランダム辞書ファイルオープン
        rfile = open('dictionary/random.txt', 'r', encoding='utf_8')
        # 各行を要素としてリストに格納
        r_lines = rfile.readlines()
        rfile.close()

        # 末尾の改行と空白文字を取り除いて
        # インスタンス変数（リスト）に格納
        self.random = []
        for line in r_lines:
            str = line.rstrip('\n')
            if str != '':
                self.random.append(str)

        # 破道辞書格納ようのインスタンス構築
        self.hadou = []
        # 破道辞書をオープン
        hfile = open('dictionary/hadou.txt', 'r', encoding='utf_8')
        # 各行を要素とするリストを取得
        h_lines = hfile.readlines()
        hfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        self.hadou=[]
        for line in h_lines:
            str = line.rstrip('\n')
            if str != '':
                self.hadou.append(str)


        # ランダム辞書格納ようのインスタンス構築
        self.noguti = []
        # ランダム辞書をオープン
        nfile = open('dictionary/Noguti.txt', 'r', encoding='utf_8')
        # 各行を用佐とするリストを取得
        n_lines = nfile.readlines()
        nfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        self.noguti=[]
        for line in n_lines:
            str = line.rstrip('\n')
            if str != '':
                self.noguti.append(str)

        # 抽選見せよう辞書格納ようのインスタンス構築
        self.tyuusenn = []
        # 抽選見せよう辞書をオープン
        tfile = open('dictionary/tyuusenn.txt', 'r', encoding='utf_8')
        # 各行を用佐とするリストを取得
        t_lines = tfile.readlines()
        tfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        self.tyuusenn = []
        for line in t_lines:
            str = line.rstrip('\n')
            if str != '':
                self.tyuusenn.append(str)

        # 抽選詐欺辞書格納ようのインスタンス構築
        self.ttyuusenn = []
        # 抽選詐欺辞書をオープン
        ttfile = open('dictionary/tyuusenn1.txt', 'r', encoding='utf_8')
        # 各行を用佐とするリストを取得
        tt_lines = ttfile.readlines()
        tfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        self.ttyuusenn = []
        for line in tt_lines:
            str = line.rstrip('\n')
            if str != '':
                self.ttyuusenn.append(str)

        # パターン辞書オープン
        pfile = open('dictionary/pattern.txt', 'r', encoding='utf_8')
        # 各行を要素としてリストに格納
        p_lines = pfile.readlines()
        pfile.close()
        # 末尾の改行と空白文字を取り除いて
        # インスタンス変数（リスト）に格納
        self.new_lines = []
        for line in p_lines:
            str = line.rstrip('\n')
            if str != '':
                self.new_lines.append(str)
        # 辞書型のインスタンス変数を用意
        self.pattern = {}
        # 一行をタブで切り分けて辞書オブジェクトに格納
        # ’pattern’キー　：正規表現のパターン
        # 'phrases'キー　:応答列
        for line in self.new_lines:
            ptn, prs = line.split('\t')
            self.pattern.append(ParseItem(ptn, prs))


class ParseItem:
    SEPARATOR = '~((-?\d+)##)?(.*)$'

    def __init__(self, pattern, phrases):
        """

        :param pattern パターン:
        :param phrases　応答例:
        """
        # 辞書のパターンの部分にSEPARATORをパターンマッチさせる
        m = re.findall(ParseItem.SEPARATOR, pattern)
        # インスタンス変数modifyに代入
        self.modify = 0
        # マッチ結果の整数部分がからでなければ値を再代入
        if m[0][1]:
            self.modify = int(m[0][1])
        # インスタンス変数patternにマッチ結果のパターン部分を代入
        self.pattern = m[0][2]

        self.phrases = []
        self.dic = {}
        # 引数でwたされた応答例を'|'で分割し
        # 個々の要素に対してパターンマッチさせる
        # self.phrases[ 'need' : 応答例の整数部分
        #                'phrase'; 応答例の文字列部]
        for phrases in phrases.split('|'):
            # 応答例に対してパターンマッチさせる
            m = re.findall(ParseItem.SEPARATOR, phrases)
            # 'need'キーの値を整数部分ｍ[0][1]にする
            # 'phrase'キーの値を応答文字列ｍ[0][2]にする
            self.dic['need'] = 0
            if m[0][1]:
                self.dic['need'] = int(m[0][1])
            self.dic['phrase'] = m[0][2]
            # 作成した辞書をphraseリストに追加
            self.phrases.append(self.dic.copy())

     def match(self, str):
         """

         :param str:
         :return:
         """
         return re.search(self.pattern, str)

     def chice (self, mood):
         """
         現在の機嫌値と
         必要な機嫌値を比較して
         適切な応答例を返す
         :param mood:
         :return:
         """
         choices = []
         # self.phrasesが保持するリストの要素（辞書）を反復する
         for p in self.phrases:
            # self.phrasesの'need'キーの数値と
            # パラメータmoodをsuitable（）に渡す
            #　結果が１であればchoiceリストに追加する
            if self.suitable(p)