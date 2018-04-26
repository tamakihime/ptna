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
    def response(self, input):
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
        # ランダム辞書格納ようのインスタンス構築
        self.responses = []
        # ランダム辞書をオープン
        rfile = open('dictionary/random.txt', 'r', encoding='utf_8')
        # 各行を用佐とするリストを取得
        r_lines = rfile.readlines()
        rfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        for line in r_lines:
            str = line.rstrip('\n')
            if(str!=''):
                self.responses.append(str)

    def response(self, input):

        return random.choice(self.responses)


class HasdouResponder(Responder):
    """破道を返すためのサブクラス
    """
    def __init__(self, name):
        """スーパークラスの__init__（）を呼び出す


        """
        super().__init__(name)
        # ランダム辞書格納ようのインスタンス構築
        self.responses = []
        # ランダム辞書をオープン
        rfile = open('dictionary/hadou.txt', 'r', encoding='utf_8')
        # 各行を用佐とするリストを取得
        r_lines = rfile.readlines()
        rfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        for line in r_lines:
            str = line.rstrip('\n')
            if(str!=''):
                self.responses.append(str)

    def response(self, input):

        return random.choice(self.responses)

class NogutiResponder(Responder):
    """破道を返すためのサブクラス
    """
    def __init__(self, name):
        """スーパークラスの__init__（）を呼び出す


        """
        super().__init__(name)
        # ランダム辞書格納ようのインスタンス構築
        self.responses = []
        # ランダム辞書をオープン
        rfile = open('dictionary/hadou.txt', 'r', encoding='utf_8')
        # 各行を用佐とするリストを取得
        r_lines = rfile.readlines()
        rfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        for line in r_lines:
            str = line.rstrip('\n')
            if(str!=''):
                self.responses.append(str)

    def response(self, input):

        return random.choice(self.responses)

