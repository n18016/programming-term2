import field_map

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
    print("現在位置は" + str(cur_pos) + "です。")
    event_nm = field_map.get_event(cur_pos)
    print(event_nm)


if __name__ == '__main__':
    print("すごろくゲーム、Start!!")

    while cur_pos < field_map.goal_pos:
        dice_num = field_map.shake_dice()
        go_forward(dice_num)
    print("ゴールしました。おめでとうございます!")
