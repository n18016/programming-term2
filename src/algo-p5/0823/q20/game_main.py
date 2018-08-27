import field_map
from player import Player

# 以下メイン処理
if __name__ == '__main__':
    # 開始メッセージを表示
    print("すごろくゲーム、Start!!")

    # プレイヤーの名前を取得する
    p_name = input("プレイヤーの名前を教えてください>> ")

    # Playerクラスのオブジェクトを作成
    hero = Player(p_name)

    # ゲームからの呼びかけメッセージを表示
    print("やあ、" + hero.name + "!旅をはじめよう!")

    # ゴールに到達するまで繰り返す
    while hero.cur_pos < field_map.goal_pos:
        hero.choose_action_in_field()

    # ゴール到達のメッセージを表示
    print("ゴールしました。おめでとうございます!")
