import random


class Enemy:
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
        self.name = name
        # TODO:元々のコンストラクタをZakoCharaクラスにそのままコピーした後で、以下の値全てに1を代入するよう変更してください。
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
        # ダメージを最小〜最大の範囲でランダムに取得
        damage = random.randint(self.min_damage, self.max_damage)

        is_critical = False  # 「つうこんのいちげき」かどうか
        # 1/(self.freq)の確率で「かいしんのいちげき」を出す
        rand_num = random.randint(1, self.freq)
        if rand_num % self.freq == 0:
            is_critical = True

        # 敵のターンのメッセージ表示
        print(self.name + "のこうげき!")

        # つうこんのいちげきの場合、ダメージを倍にする
        if is_critical:
            print("つうこんのいちげき!!")
            damage *= 2

        # プレイヤーにダメージを与える
        player.hp -= damage

        if player.hp > 0:
            print(player.name + "は" + str(damage) + "のダメージを受けた!" + player.name + "のHPは" + str(player.hp) + "です。")
            return True
        else:
            print(player.name + "は" + str(damage) + "のダメージを受けた!" + player.name + "のHPは0です。")
            return False
