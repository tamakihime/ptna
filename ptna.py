from Dictionary import Dictionary
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
        # Dictionaryを生成
        self.dictionary = Dictionary()
        # randomresponderを生成
        self.res_random = RandomResponder('Random',self.dictionary)
        # RepeatResponderを生成
        self.res_what = RepeatResponder('Repeat', self.dictionary)
        # PatternResponderを生成
        self.res_pattern = PatternResponder('Pattern',self.dictionary)
        # Hadouresponderを生成
        self.res_hadou = HasdouResponder('破道', self.dictionary)
        # Nogutiresponderを生成
        self.res_Noguti = NogutiResponder('By野口', self.dictionary)
        # tyuusennを生成
        self.res_tyuusenn = tyuusennResponder('抽選', self.dictionary)
        # ttyuusenn
        self.res_ttyuusenns = ttyuusennResponder('抽選',self.dictionary)
        # 初期値をセット
        self.responder = self.res_what

    def dialogue(self, input):
        """ 応答オブジェクトresponse()を呼び出して
            応答文字列を取得する
            ＠program inputユーザーによって入力された文字列
            戻り値　応答文字列
        """
        # 0か１をランダムセレクト 0ならrandomresponder をセット　1ならrepeatresponderをセット
        x = random.randint(0, 100)
        if input =="野口くん発言集":
            x = 20000
        if input == "破道":
            x = 10000
        if input == "抽選":
            x = 30000
        if input == '抽選　':
            x = 40000
        if x <= 60:
            self.responder = self.res_pattern
        elif x <= 90:
            self.responder = self.res_what
        elif x == 10000:
            self.responder = self.res_hadou
        elif x == 20000:
            self.responder = self.res_Noguti
        elif x == 30000:
            self.responder = self.res_tyuusenn
        elif x == 40000:
            self.responder = self.res_ttyuusenns
        else:
            self.responder = self.res_random

        return self.responder.response(input)

    def get_responder_name(self):
        """ptnaクラスの名前を返す
        """
        return self.responder.name

    def get_name(self):
        """ptnaオブジェクトの名前を返す
        """
        return self.name
