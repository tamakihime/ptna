from responder import *


class ptna:
    """ピティナの本体クラス
    """
    def __init__(self, name):
        """ptnaオブジェクトの名前をnameに格納
           Respondeオブジェクトを生成してresponderに格納
        　 @param name ptnaオブジェクトの名前
        """
        self.name = name
        self.responder = RandomResponder('Random')

    def dialogue(self, input):
        """ 応答オブジェクトresponse()を呼び出して
            応答文字列を取得する
            ＠program inputユーザーによって入力された文字列
            戻り値　応答文字列
        """
        return self.responder.response(input)

    def get_responder_name(self):
        """ptnaクラスの名前を返す
        """
        return self.responder.name

    def get_name(self):
        """ptnaオブジェクトの名前を返す
        """
        return self.name
