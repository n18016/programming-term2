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
        self.min_damage = 2
        self.max_damage = 4
        self.freq = 30

    def attack(self, player):
        """
        敵を攻撃する
        Parameters
        ----------
        player : Player
            プレイヤーのオブジェクト
        Returns
        -------
        bool
            True:プレイヤーがまだ生きている、False:プレイヤーが死んでしまった
        """
        damage = self.min_damage
        print(self.name + "のこうげき!")
        player.hp -= damage

        if player.hp > 0:
            print(player.name + "は" + str(damage) + "のダメージを受けた!" + player.name + "のHPは" + str(player.hp) + "です。")
            return True
        else:
            print(player.name + "は" + str(damage) + "のダメージを受けた!" + player.name + "のHPは0です。")
            return False
