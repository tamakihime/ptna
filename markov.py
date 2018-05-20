import re
import random
from analyzer import *


class Markov:
    def make(self):
        # ログファイルを読み込む
        filename = 'log.txt'
        with open(filename,"r",encoding='utf_8') as f:
            text = f.read()
        # プロンプトの文字列を取り除く
        text = re.sub('>', '', text)
        text = re.sub(
            'ptna:Repeat|ptna:Random|ptna:Pattern|ptna:Template|ptna:Markov|ptna:破道|ptna:By野口|ptna:抽選|ptna:抽選 ',
            '',
            text)
        # タイムスタンプを取り除く
        text = re.sub('Ptna System Dialogue Log:.*\n','',text)
        # 空白行が含まれていると￥ｎ￥ｎが続くので￥ｎ1つにする
        text = re.sub('\n\n','\n',text)
