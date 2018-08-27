class Enemy:
    def __init__(self, name):
        """
        コンストラクタ
        Parameters
        ----------
        name : str
            プレイヤーの名前
        Returns
        -------
        自分自身のインスタンス
        """
        self.name = name
        self.hp = 10
        self.min_damege = 2
        self.maxdamege = 4
        self.freq = 20
