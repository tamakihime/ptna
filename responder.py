import random

class Responder:
    """応答クラス
    """
    def __init__(self, name):
        """Responderオブジェクトの名前をnameに格納

            @param name Responder オブジェクトの名前
        """
        self.name = name

    def response(self, input):
        """応答文字列を作って返す

            @param input 入力された文字列　
        """
        return ''


class RepeatResponder(Responder):
    """オウム返しのためのサブクラス
    """
    def response(selfself,input):
        """応答文字を作って返す
            ＠param input入力された文字列
        """
        return '{}ってなに？'.format(input)


class RandomResponder(Responder):
    """ランダムな応答のためのサブクラス
    """
    def __init__(self, name):
        """スーパークラスの__init__（）を呼び出す


        """
        super().__init__(name)
        self.responses = ['いい天気だね', '君はパーリーピーポー', '10円拾った']

    def response(self, input):
        return (random.chice(self.response))