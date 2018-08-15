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
    cur_pos = 0
    cur_pos += cells

dice_num = 1

print(str(dice_num) + "の目が出ました。")
go_forward(dice_num)
print("現在位置は" + str(cur_pos) + "です。")
