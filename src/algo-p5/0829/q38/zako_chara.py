from enemy import Enemy


class ZakoChara(Enemy):
    def __init__(self, name):
        """
        コンストラクタ
        Parameters
        ----------
        name : str
            敵の名前
        Returns
        -------
        自分自身のインスタンス
        """
        super().__init__(name)
        self.hp = 10
        self.min_damage = 2
        self.max_damage = 4
        self.freq = 30
