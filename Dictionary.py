import random
import re
from analyzer import *


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
        pfile = open('dictionary/pattern.txt', 'r', encoding='utf_8')
        # 各行を要素としてリストに格納
        p_lines = pfile.readlines()
        pfile.close()
        # 末尾の改行と空白文字を取り除いて
        # インスタンス変数（リスト）に格納
        self.new_lines = []
        for line in p_lines:
            str = line.rstrip('\n')
            if (str != ''):
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

        # テンプレート辞書格納よインスタンス生成
        self.template = {}
        # パターン辞書のデータを使うためパターン辞書のデータをオープン
        tefile = open('dictionary/template.txt', 'r', encoding='utf_8')
        # 各行を要素としてリストに格納
        te_lines = tefile.readline()
        tefile.close()
        # 各行の開業と空這う文字を取り除いて
        # インスタンス変数にか苦悩する
        self.new_te_lines = []
        for line in te_lines:
            str = line.rstrip('\n')
            if str != '':
                self.new_te_lines.append(str)
        # テンプレート辞書の各行をタブで切り分ける
        # count %noun%の出現回数
        # template　テンプレート文字列
        for line in self.new_te_lines:
            # まずは分割
            count, template = line.split('\t')
            # self.templateのキーにcountが存在しなければ
            # count をキーにしてからのリストを要素として追加する
            if not count in self.template:
                self.template[count]= []
            # countキーのリストにテンプレート文字列を追加
            self.template[count].append(template)

    def study(self, input, parts):
        """
        :param input: ユーザーの発言
        :return: 記憶
        """
        # ユーザー入力の末尾をどうこうする
        input = input.rstrip('\n')
        # インプット文字を引数としてランダム辞書登録用もメソッドを呼ぶ
        self.study_random(input)
        # インプット文字と解析結果を引数としパターン辞書の登録メソッドを呼ぶ
        self.study_pattern(input, parts)

    def study_random(self, input):
        """
        ユーザ発言を学習
        :param input:　ユーザー発言
        :return:
        """
        if not input in self.random:
            self.random.append(input)

    def study_pattern(self, input, parts):
        """ ユーザーの発言を学習する

            @param input  インプット文字列
            @param parts  形態素解析の結果（リスト）
        """
        # 多重リストの要素を2つのパラメーターに取り出す
        for word, part in parts:
            # analyzerのkeyword_check()関数による名詞チェックが
            # Trueの場合
            if keyword_check(part):
                depend = False  # ParseItemオブジェクトを保持する変数
                # patternリストのpatternキーを反復処理
                for ptn_item in self.pattern:
                    # インプットされた名詞が既存のパターンとマッチしたら
                    # patternリストからマッチしたParseItemオブジェクトを取得
                    if re.search(ptn_item.pattern, word):
                        depend = ptn_item
                        break  # マッチしたら止める
                # 既存パターンとマッチしたParseItemオブジェクトから
                # add_phraseを呼ぶ
                if depend:
                    depend.add_phrase(input)  # 引数はインプット文字列
                else:
                    # 既存パターンに存在しない名詞であれば
                    # 新規のParseItemオブジェクトを
                    # patternリストに追加
                    self.pattern.append(ParseItem(word, input))

    def study_template(self, parts):
        """

        :param patrs 形態素解析の結果:
        :return:
        """
        template = ''
        count = 0
        for word ,part in parts:
            # 名詞であるかをチェック
            if (keyword_check(part)):
                word = '%noun%'
                count += 1
                template += word
        # self.templateのキーにしてからのリストを要素として追加
        # countをキーにしてからのリストを要素として追加
        if count > 0:
            count = str(count)
            if not count in self.template:
                self.template[count] = []
        # countキーのリストにテンプレート文字列を追加
        if not template in self.template[count]:
            self.template[count].append(template)

    def save(self):
        """ self.randomの内容をまるごと辞書に書き込む
        """
        # 各要素の末尾に改行を追加する
        for index, element in enumerate(self.random):
            self.random[index] = element + '\n'
        # ランダム辞書に書き込む
        with open('dictionary/random.txt', 'w', encoding='utf_8') as f:
            f.writelines(self.random)

        # パターン辞書にファイルを書き込むデータを保持するリスト
        pattern = []
        for ptn_item in self.pattern:
            # make_line()で行データを作成
            pattern.append(ptn_item.make_line() + '\n')
            # パターン辞書ファイルに書き込む
            with open('dictionary/pattern.txt', 'w', encoding='utf_8') as f:
                f.writelines(pattern)


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

        self.phrases = []  # 応答例を保持するリスト
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

            @param mood 現在の機嫌値
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
        """必要機嫌値を現在の機嫌値と比較

            @param need 必要機嫌値
            @param mood 現在の機嫌値
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

    def add_phrase(self, phrase):
        """パターン辞書1行ぶんの応答例のみを作る

            @param phrase インプット文字列
        """
        # インプット文字列がphrasesリストの応答例に一致するか
        # self.phrases  インプットにマッチした応答フレーズの辞書リスト
        # [ {'need'  : 応答例の整数部分, 'phrase': 応答例の文字列部分}, ... ]
        for p in self.phrases:
            # print('phrases===',p)####################
            # 既存の応答例に一致したら終了
            if p['phrase'] == phrase:
                return
        # phrasesリストに辞書を追加
        # {'need'  :0, 'phrase':インプット文字列}
        self.phrases.append({'need': 0, 'phrase': phrase})

    def make_line(self):
        """パターン辞書1行ぶんのデータを作る
        """
        # 必要機嫌値 + '##' + パターン
        pattern = str(self.modify) + '##' + self.pattern
        phrases = []
        for p in self.phrases:
            resp = str(p['need']) + '##' + str(p['phrase'])
            phrases.append(str(p['need']) + '##' + p['phrase'])

        return pattern + '\t' + '|'.join(phrases)

