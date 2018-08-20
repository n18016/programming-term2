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
