import random

goal_pos = 100


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
    input("サイコロを振ります。Enterキーを押してください。")
    dice_num = random.randint(1, 6)
    print(str(dice_num) + "の目が出ました。")
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


if __name__ == '__main__':
    print(get_event(1))

    print(get_event(13))

    print(get_event(37))

    print(get_event(49))
