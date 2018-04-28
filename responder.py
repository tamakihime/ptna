import random
import re


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

    def response(self, input):
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
    def response(self, input):
        """応答文字を作って返す
            ＠param input入力された文字列
        """
        return '{}ってなに？'.format(input)


class RandomResponder(Responder):
    """ランダムな応答のためのサブクラス
    """
    def response(self, input):

        return random.choice(self.dictionary.random)


class PatternResponder(Responder):
    """
    パターン反応用サブクラス
    """
    def response(self, input):
        for ptn, prs in zip(
            self.dictionary.pattern['pattern'],
            self.dictionary.pattern['phrases']
                ):
            # インプットされた文字列に対して
            # パターンの値でパターンマッチングを行う
            m = re.search(ptn, input)
            # インプットされた文字列がパターンにマッチしている場合
            if m:
                # 応答フレーズ(ptn[1])を’｜’で切り分けて
                # rランダムに一文を取り出す
                resp = random.choice(prs.split('|'))
                # 抽出した応答フレーズを返す
                # 応答フレーズの中に％match％が埋め込まれたいた場合
                # インプットされた文字列内のパターンマッチした
                # 文字列に置き換える
                return re.sub('%match%',m.group(), resp)
            # パターンマッチ適応不可の場合は、ランダム辞書を呼び出す
            return random.choice(self.dictionary.random)


class HasdouResponder(Responder):
    """破道を返すためのサブクラス
    """
    def response(self, input):

        return random.choice(self.dictionary.hadou)


class NogutiResponder(Responder):
    """野口くん語録を返すためのサブクラス
    """
    def response(self, input):

        return random.choice(self.dictionary.noguti)


class tyuusennResponder(Responder):
    """抽選システム

    """
    def response(self, input):

        return random.choice(self.dictionary.tyuusenn)


class ttyuusennResponder(Responder):
    """
    詐欺用ちゅうせんしすてむ
    """
    def response(self, input):

        return random.choice(self.dictionary.ttyuusenn)



