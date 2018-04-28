class Dictionary:
    def __init__(self):
        self.random = []
        # ランダム辞書ファイルオープン
        rfile = open('dictionary/random.txt', 'r', encoding='utf_8')
        # 各行を要素としてリストに格納
        r_lines = rfile.readlines()
        rfile.close()

        # 末尾の改行と空白文字を取り除いて
        # インスタンス変数（リスト）に格納
        self.random = []
        for line in r_lines:
            str = line.rstrip('\n')
            if str != '':
                self.random.append(str)

        # 破道辞書格納ようのインスタンス構築
        self.hadou = []
        # 破道辞書をオープン
        hfile = open('dictionary/hadou.txt', 'r', encoding='utf_8')
        # 各行を要素とするリストを取得
        h_lines = hfile.readlines()
        hfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        self.hadou=[]
        for line in h_lines:
            str = line.rstrip('\n')
            if str != '':
                self.hadou.append(str)


        # ランダム辞書格納ようのインスタンス構築
        self.noguti = []
        # ランダム辞書をオープン
        nfile = open('dictionary/Noguti.txt', 'r', encoding='utf_8')
        # 各行を用佐とするリストを取得
        n_lines = nfile.readlines()
        nfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        self.noguti=[]
        for line in n_lines:
            str = line.rstrip('\n')
            if str != '':
                self.noguti.append(str)

        # 抽選見せよう辞書格納ようのインスタンス構築
        self.tyuusenn = []
        # 抽選見せよう辞書をオープン
        tfile = open('dictionary/tyuusenn.txt', 'r', encoding='utf_8')
        # 各行を用佐とするリストを取得
        t_lines = tfile.readlines()
        tfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        self.tyuusenn = []
        for line in t_lines:
            str = line.rstrip('\n')
            if str != '':
                self.tyuusenn.append(str)

        # 抽選詐欺辞書格納ようのインスタンス構築
        self.ttyuusenn = []
        # 抽選詐欺辞書をオープン
        ttfile = open('dictionary/tyuusenn1.txt', 'r', encoding='utf_8')
        # 各行を用佐とするリストを取得
        tt_lines = ttfile.readlines()
        tfile.close()
        # 末尾の改行と空白文字を取り除いてインスタンス変数に格納
        self.ttyuusenn = []
        for line in tt_lines:
            str = line.rstrip('\n')
            if str != '':
                self.ttyuusenn.append(str)

        # パターン辞書オープン
        pfile = open('dictionary/pattern.txt', 'r', encoding='utf_8')
        # 各行を要素としてリストに格納
        p_lines = pfile.readlines()
        pfile.close()
        # 末尾の改行と空白文字を取り除いて
        # インスタンス変数（リスト）に格納
        self.new_lines = []
        for line in p_lines:
            str = line.rstrip('\n')
            if str != '':
                self.new_lines.append(str)
        # 辞書型のインスタンス変数を用意
        self.pattern = {}
        # 一行をタブで切り分けて辞書オブジェクトに格納
        # ’pattern’キー　：正規表現のパターン
        # 'phrases'キー　:応答列
        for line in self.new_lines:
            ptn, prs = line.split('\t')
            self.pattern.setdefault('pattern', []).append(ptn)
            self.pattern.setdefault('phrases', []).append(prs)

