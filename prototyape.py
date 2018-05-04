from math import sin

from ptna import *

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
    print(sin(180));