goal_pos = 10
cur_pos = 0


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
    dice_num = 1
    print(str(dice_num) + "の目が出ました。")
    return dice_num


def go_forward(cells):
    """
    前に進む
    Parameters
    ----------
    cells : int
        進むマス目の数
    Returns
    -------
    なし
    """
    global cur_pos
    cur_pos += cells
    print("現在位置は" + str(cur_pos) + "です。")
print("すごろくゲーム、Start!!")

while cur_pos < goal_pos:
    dice_num = 1
    go_forward(dice_num)
print("ゴールしました。おめでとうございます！")
