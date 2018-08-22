import random

# 変数定義部
goal_pos = 100  # ゴールの位置

# 関数定義部
def shake_dice():
    """
    サイコロを振る
    Parameters
    ----------
    なし
    Returns
    -------
    int
        サイコロを振って出た目
    """
    # サイコロを振るため、Enterキーを入力待ちにする
    input("サイコロを振ります。Enterキーを押してください。")

    # 1〜6の任意の数字を取得する
    dice_num = random.randint(1, 6)

    # 出た目の数をコンソールに表示する
    print(str(dice_num) + "の目が出ました。")

    # 出た目を返す
    return dice_num

def get_event(target_cell):
    """
    止まったセルのイベントを取得する
    Parameters
    ----------
    target_cell : int
        止まったセル
    Returns
    -------
    str
        イベントの名称
    """
    if target_cell % 10 == 3:
        return "GoMoreForward"
    elif target_cell % 20 == 17:
        return "GoBack"
    elif target_cell % 100 == 49:
        return "GoBackToStart"
    else:
        return ""

# 以下メイン処理
if __name__ == '__main__':
    print(get_event(1))

    print(get_event(13))

    print(get_event(37))

    print(get_event(49))
