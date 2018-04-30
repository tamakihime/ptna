import tkinter as tk
from ptna import *

"""グローバル変数の定義
"""
entry = None
response_area = None
lb = None
action = None
ptna = ptna('ptna')
on_canvas = None
ptyna_image = []


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


def changeImg(img):
    """ 画像をセットする関数
    """
    canvas.itemconfig(
        on_canvas,
        image=ptyna_image[img]  # イメージオブジェクトを指定
    )
    canvas.update()


def change_looks():
    em = ptna.emotion.mood
    if -5 <= em <= 5:
        changeImg(0)
    elif -10 <= em < -5:
        changeImg(1)
    elif -15 <= em < -10:
        changeImg(2)
    elif 5 <= em < 15:
        changeImg(3)


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

    change_looks()


# ==========================================

# 画面を作成する関数

# ==========================================


def run():
    # グローバル変数を使用するための記述
    global entry, response_area, lb, action, on_canvas, ptyna_image, canvas

    # メインウィンドウを構築
    root = tk.Tk()
    # ウィンドウのサイズを作成
    root.geometry('880x560')
    # ウィンドウのタイトルを変更
    root.title('Intelligent Agent :')
    # フォントの用意
    font = ('Helevetica', 14)
    font_log = ('Helevetica', 11)

    # メニューバーの作成
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    # [ファイル]メニュー作成
    filemenu = tk.Menu(menubar)
    menubar.add_cascade(label='オプション', menu=filemenu)
    filemenu.add_command(label='閉じる', command=root.destroy)
    # オプションメニュー
    action = tk.IntVar()
    optionmenu = tk.Menu(menubar)
    menubar.add_cascade(label='オプション', menu=optionmenu)
    optionmenu.add_radiobutton(
        label='Responderを表示',
        variable=action,
        value=0
    )
    optionmenu.add_radiobutton(
        label='Responderを表示しない',
        variable=action,
        value=1
    )

    # キャンバスの作成
    canvas = tk.Canvas(
        root,
        width=500,
        height=300,
        relief=tk.RIDGE,
        bd=2
    )
    canvas.place(x=370, y=0)
    # イメージを用意
    ptyna_image.append(tk.PhotoImage(file="talk.gif"))
    ptyna_image.append(tk.PhotoImage(file="empty.gif"))
    ptyna_image.append(tk.PhotoImage(file="angry.gif"))
    ptyna_image.append(tk.PhotoImage(file="happy.gif"))

    on_canvas = canvas.create_image(
        0,
        0,
        image=ptyna_image[0],
        anchor=tk.NW
    )

    # 応答エリアの作成
    response_area = tk.Label(
        root,
        width=50,
        height=10,
        bg='yellow',
        font=font,
        relief=tk.RIDGE,
        bd=2
    )
    response_area.place(x=370, y=305)

    # フレームの作成
    frame = tk.Frame(
        root,
        relief=tk.RIDGE,
        borderwidth=4
    )

    # 入力ボックスの作成
    entry = tk.Entry(
        frame,
        width=70,
        font=font
    )
    entry.pack(side=tk.LEFT)
    entry.focus_set()

    # ボタンの作成
    button = tk.Button(
        frame,
        width=15,
        text='話す',
        command=talk
    )
    button.pack(side=tk.LEFT)
    frame.place(x=30, y=520)

    # リストボックスを作成
    lb = tk.Listbox(
        root,
        width=42,
        height=30,
        font=font_log,
    )
    # 縦のスクロールバーを作成
    sb1 = tk.Scrollbar(
        root,
        orient=tk.VERTICAL,
        command=lb.yview
    )

    # 横のスクロールバーを作成
    sb2 = tk.Scrollbar(
        root,
        orient=tk.HORIZONTAL,
        command=lb.xview
    )

    # リストボックスとスクロールバーを連動させる
    lb.configure(yscrollcommand=sb1.set)
    lb.configure(xscrollcommand=sb2.set)
    # gridでリストボックス、スクロールバーを画面上に配置
    lb.grid(row=0, column=0)
    sb1.grid(row=0, column=1, sticky=tk.NS)
    sb2.grid(row=1, column=0, sticky=tk.EW)

    # メインループ
    root.mainloop()


# ============================================
# プログラムの起点
# ============================================
if __name__ == '__main__':
    run()
