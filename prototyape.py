class ptna:
    """ピティナの本体クラス
    """
    def __init__(self,name):
        """ptnaオブジェクトの名前をnameに格納
           Respondeオブジェクトを生成してresponderに格納
        　 @param name ptnaオブジェクトの名前
        """
        self.name = name
        self.responder = Responder('What')
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
class Responder:
    """応答クラス
    """
    def __init__(self,name):
        """Responderオブジェクトの名前をnameに格納

            @param name Responder オブジェクトの名前
        """
        self.name = name
    def response(self,input):
        """応答文字列を作って返す

            @param input 入力された文字列　
        """
        return '{}ってなぁに？'.format(input)
###############################################################
#実行ブロック
###############################################################
def prompt (obj):
    """ピティナのプロントを作る関数
        戻り値'ptnaオブジェクト名：応答オブジェクト名＞'
    """
    return obj.get_name() + ':'+obj.get_responder_name()+'>'
print('ptna System prototype : ptna')
ptna = ptna('ptna')
while True:
    inputs = input('>')
    if not inputs:
        print('バイバイ')
        break
    response = ptna.dialogue(inputs)
    print(prompt(ptna),response)
