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
        self.hadou = []
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
        self.noguti = []
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
        pfile = open('dictionary/pattern.txt', 'r', encoding = 'utf_8')
        # 各行を要素としてリストに格納
        p_lines = pfile.readlines()
        pfile.close()
        # 末尾の改行と空白文字を取り除いて
        # インスタンス変数（リスト）に格納
        self.new_lines = []
        for line in p_lines:
            str = line.rstrip('\n')
            if (str!=''):
                self.new_lines.append(str)

        # リスト型のインスタンス変数を用意
        self.pattern = []

        # 辞書データの各行をタブで切り分ける
        # ptn 正規表現のパターン
        # prs 応答例
        # ParseItemオブジェクトを生成(引数はptn、prs）して
        # インスタンス変数pattern（リスト）に追加
        for line in self.new_lines:
            ptn, prs = line.split('\t')
            self.pattern.append(ParseItem(ptn, prs))

    def study(self, input):
        """
        :param input: ユーザーの発言
        :return: 記憶
        """
        # ユーザー入力の末尾をどうこうする
        input = input.rstrip('\n')
        if not input in self.random:
            self.random.append(input)

    def save(self):
        """ self.randomの内容をまるごと辞書に書き込む
        """
        # 各要素の末尾に改行を追加する
        for index, element in enumerate(self.random):
            self.random[index] = element +'\n'
        # ランダム辞書に書き込む
        with open('dictionary/random.txt', 'w', encoding = 'utf_8') as f:
            f.writelines(self.random)


class ParseItem:
    SEPARATOR = '^((-?\d+)##)?(.*)$'

    def __init__(self, pattern, phrases):
        """ @param pattern  パターン
            @param phrases  応答例
        """
        # 辞書のパターンの部分にSEPARATORをパターンマッチさせる
        m = re.findall(ParseItem.SEPARATOR, pattern)
        # インスタンス変数modifyに0を代入
        self.modify = 0
        # マッチ結果の整数の部分が空でなければ値を代入
        if m[0][1]:
            self.modify = int(m[0][1])
        # インスタンス変数patternにマッチ結果のパターン部分を代入
        self.pattern = m[0][2]

        self.phrases = []  # 応答例を保持するインスタンス変数
        self.dic = {}  # インスタンス変数
        # 引数で渡された応答例を'|'で分割し、
        # 個々の要素に対してSEPARATORをパターンマッチさせる
        # self.phrases[ 'need'  : 応答例の整数部分
        #               'phrase': 応答例の文字列部分 ]
        for phrase in phrases.split('|'):
            # 応答例に対してパターンマッチを行う
            m = re.findall(ParseItem.SEPARATOR, phrase)
            # 'need'キーの値を整数部分m[0][1]にする
            # 'phrase'キーの値を応答文字列m[0][2]にする
            self.dic['need'] = 0
            if m[0][1]:
                self.dic['need'] = int(m[0][1])
            self.dic['phrase'] = m[0][2]
            # 作成した辞書をphrasesリストに追加
            self.phrases.append(self.dic.copy())

    def match(self, str):
        """self.pattern(各行ごとの正規表現)を
           インプット文字列にパターンマッチ
        """
        return re.search(self.pattern, str)

    def choice(self, mood):
        """インスタンス変数phrases(リスト）の
           要素('need''phrase'の辞書)
            'need':数値を

            @ptam mood 現在の機嫌値
        """
        choices = []
        # self.phrasesが保持するリストの要素（辞書）を反復処理する
        for p in self.phrases:
            # self.phrasesの'need'キーの数値と
            # パラメーターmoodをsuitable()に渡す
            # 結果がTrueであればchoicesリストに'phrase'キーの応答例を追加
            if (self.suitable(p['need'], mood)):
                choices.append(p['phrase'])
        # choicesリストが空であればNoneを返す
        if (len(choices) == 0):
            return None
            # choicesリストが空でなければランダムに
            # 応答文字列を選択して返す
        return random.choice(choices)

    def suitable(self, need, mood):
        """インスタンス変数phrases(リスト）の
           要素('need''phrase'の辞書)
            'need':数値を

            @ptam need 必要機嫌値
            @ptam mood 現在の機嫌値
        """
        # 必要機嫌値が0であればTrueを返す
        if (need == 0):
            return True
        # 必要機嫌値がプラスの場合は機嫌値が必要機嫌値を超えているか判定
        elif (need > 0):
            return (mood > need)
        # 応答例の数値がマイナスの場合は機嫌値が下回っているか判定
        else:
            return (mood < need)

