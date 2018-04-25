import tkinter as tk
from ptna import *

"""グローバル変数の定義
"""
entry = None
response_area = None
lb = None
action = None
ptna = ptna('ptna')


def putlog(str):
    """

    :param:　入力文字列　応答メッセージ
    :return: 対話ログをリストボックスに
    """
    lb.insert(tk.END, str)


def prompt():
    """

    :return:ptnaのプロント
    """
    p = ptna.name
    if (action.get()) == 0:
        p += ':' + ptna.responder.name
        return p + '>'


def talk():
    """
    対話を行う関数
    ptnaクラスのdialonguを実行　応答メッセージを取得すr
    :return: 入力文字列　応答メッセージ
    """
    value = entry.get()
    # 入力エリアに何も存在しなければ
    if not value:
        response_area.configure(text='なに？')
    # 入力が存在すれば対話オブジェクトを実行
    else:
        # 入力文字を因数にしてdialogue()の結果を取得
        response = ptna.dialogue(value)
        # 応答メッセージを表示
        response_area.configure(text=response)
        # 入力文字列引数にしてputolog()を呼ぶ
        putlog('> ' + value)
        # 応答文字列を引数にしてputlogを呼ぶ
        putlog(prompt() + response)
        # 入力データをクリア
        entry.delete(0, tk.END)
# ==========================================

# 画面を作成する関数

# ==========================================


def run():
    # グローバル変数を使用するための記述
    global entry, response_area, lb, action

    # メインウィンドウを構築
    root = tk.Tk()
    # ウィンドウのサイズを作成
    root.geometry('880x560')
    # ウィンドウのタイトルを変更
    root.title('Intelligent Agent :')
    # フォントの用意
    font = ('Helevetiva', 14)
    font_log=('Helevetiva', 11)

    # メニューバーの作成
    menubar = tk.Menu(root)
    root.config(menue=menubar)
    # [ファイル]メニュー作成
    filemenue = tk.Menu(menubar)
    menubar.add_cascade(label='オプション', menu=filemenue)
    filemenue.add_command(labei='閉じる', command=root.destroy)
    # オプションメニュー
    action = tk.IntVar()
    optionmenue = tk.Menu(menubar)
    menubar.add_cascade(label='オプション', menu=optionmenue)