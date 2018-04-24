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
        return '{}ってなぁに？'.format(input)
###############################################################
#実行ブロック
###############################################################


def prompt(obj):
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
    print(prompt(ptna), response)
