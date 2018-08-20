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

    if event_nm == "GoMoreForward":
        go_more_forward(2)
    if event_nm == "GoBack":
        go_back(3)
    if event_nm == "GoBackToStart":
        go_back_to_start()


def go_more_forward(cells):
    """
    出た目の分さらに前に進む
    Parameters
    ----------
    cells : int
        進むマス目の数
    Returns
    -------
    なし
    """
    print("イベント発生！", cells, "マスさらに進みます。")

    go_forward(cells)


def go_back(cells):
    """
    出た目の分後ろに戻る
    Parameters
    ----------
    cells : int
        戻るマス目の数
    Returns
    -------
    なし
    """
    print("イベント発生！", cells, "マス後ろに戻ります。")
    go_forward(cells * -1)


def go_back_to_start():
    """
    出た目の分後ろに戻る
    Parameters
    ----------
    なし
    Returns
    -------
    なし
    """
    global cur_pos
    print("イベント発生！振り出しに戻ってしまいます！")
    go_forward(cur_pos * -1)


if __name__ == '__main__':
    print("すごろくゲーム、Start!!")

    while cur_pos < field_map.goal_pos:
        dice_num = field_map.shake_dice()
        go_forward(dice_num)
    print("ゴールしました。おめでとうございます!")
