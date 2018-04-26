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
        # randomresponderを生成
        self.res_random = RandomResponder('Random')
        # RepeatResponderを生成
        self.res_what = RepeatResponder('Repeat')
        # Hadouresponderを生成
        self.res_hadou = HasdouResponder('破道')
        # 初期値をセット
        self.responder = self.res_what

    def dialogue(self, input):
        """ 応答オブジェクトresponse()を呼び出して
            応答文字列を取得する
            ＠program inputユーザーによって入力された文字列
            戻り値　応答文字列
        """
        # 0か１をランダムセレクト 0ならrandomresponder をセット　1ならrepeatresponderをセット
        x = random.randint(0, 1)
        if input == "破道":
            x = 10000
        if x == 1:
            self.responder = self.res_what
        if x == 0:
            self.responder = self.res_random
        if x == 10000:
            self.responder = self.res_hadou

        return self.responder.response(input)

    def get_responder_name(self):
        """ptnaクラスの名前を返す
        """
        return self.responder.name

    def get_name(self):
        """ptnaオブジェクトの名前を返す
        """
        return self.name
