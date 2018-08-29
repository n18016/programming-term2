from enemy import Enemy


class BossChara(Enemy):
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
        self.hp = 200
        self.min_damage = 8
        self.max_damage = 13
        self.freq = 10
