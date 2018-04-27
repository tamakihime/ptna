import random


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



