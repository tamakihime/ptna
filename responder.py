import random
import re
from analyzer import *

class Responder:
    """応答クラス
    """
    def __init__(self, name, Dictionary):
        """Responderオブジェクトの名前をnameに格納

            @param name Responder オブジェクトの名前
            @:param dictiornary オブジェクトごそっと代入
        """
        self.name = name
        self.dictionary = Dictionary

    def response(self, input, mood, parts):
        """応答文字列を作って返す
            常にオーナーライドされる　だって返り値ないもの
            @param input 入力された文字列　
        """
        return ''

    def get_name(self):
        """
        応答オブジェクトの名前を返す
        :return:
        """
        return self.name


class RepeatResponder(Responder):
    """オウム返しのためのサブクラス
    """
    def response(self, input, mood, parts):
        """応答文字を作って返す
            ＠param input入力された文字列
        """
        return '{}ってなに？'.format(input)


class RandomResponder(Responder):
    """ランダムな応答のためのサブクラス
    """
    def response(self, input, mood, parts):

        return random.choice(self.dictionary.random)


class PatternResponder(Responder):
    """ パターンに反応するためのサブクラス
    """
    def response(self, input, mood, parts):
        """ パターンにマッチした場合に応答文字列を作って返す

            @param  input 入力された文字列
        """
        self.resp = None
        for ptn_item in self.dictionary.pattern:
            # match()でインプット文字列にパターンマッチを行う
            m = ptn_item.match(input)
            # マッチした場合は機嫌値moodを引数にしてchoice()を実行、
            # 戻り値の応答文字列、またはNoneを取得
            if (m):
                self.resp = ptn_item.choice(mood)
            # choice()の戻り値がNoneでない場合は
            # 応答例の中の%match%をインプットされた文字列内の
            # マッチした文字列に置き換える
            if self.resp != None:
                return re.sub('%match%', m.group(), self.resp)
        # パターンマッチしない場合はランダム辞書から返す
        return random.choice(self.dictionary.random)


class TemplateResponder(Responder):
    """
    テンプレートに反応するためのサブクラス
    """
    def response(self, input , mood, parts):
        """

        :param インプット文字列:
        :param インプット文字列の解析結果:
        :param 感情パラメータ:
        :return:
        """
        # インプット文字列の名詞の部分のみを格納するリスト
        keyword = []
        # テンプレート本体を格納する変数
        template= ''
        # 解析結果partsの「文字列」→word,「品詞情報」→part に順次格納
        for word, part in parts:
            #名詞であるかどうかを確認してwordリストに格納
            if keyword_check(part):
                keyword.append(word)
        # keywordリストに格納された名詞の数を取得する
        count = len(keyword)
        # keywordリストに一つ以上の名詞が存在し、
        # 名詞の数に対応するテンプレートが存在するかを確認
        if (count > 0) and (str(count) in self.dictionary.template):
            # kewwordリストに1つ以上の名詞が存在し
            # 名詞の数に対応するテンプレートが存在しするかをチェック
            template = random.choice(self.dictionary.template[str(count)])
            # テンプレートの空欄に
            # keywordに格納されている名詞を埋め込む
            for word in keyword:
                template = template.replace('%noun%', word, 1)
            return template
        return random.choice(self.dictionary.random)


class HasdouResponder(Responder):
    """破道を返すためのサブクラス
    """
    def response(self, input, mood, parts):

        return random.choice(self.dictionary.hadou)


class NogutiResponder(Responder):
    """野口くん語録を返すためのサブクラス
    """
    def response(self, input, mood, parts):

        return random.choice(self.dictionary.noguti)


class tyuusennResponder(Responder):
    """抽選システム

    """
    def response(self, input, mood, parts):

        return random.choice(self.dictionary.tyuusenn)


class ttyuusennResponder(Responder):
    """
    詐欺用ちゅうせんしすてむ
    """
    def response(self, input, mood, parts):

        return random.choice(self.dictionary.ttyuusenn)



