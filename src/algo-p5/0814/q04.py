goal_pos = 10
cur_pos = 0


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
print("すごろくゲーム、Start!!")

while cur_pos < goal_pos:
    dice_num = 1
    print(str(dice_num) + "の目が出ました。")
    go_forward(dice_num)
    print("現在位置は" + str(cur_pos) + "です。")
print("ゴールしました。おめでとうございます")