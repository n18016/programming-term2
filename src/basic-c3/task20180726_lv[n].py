import random
cur_x = 0

while cur_x < 10:
    shake_dice = random.randint(1, 6)
    cur_x = cur_x + shake_dice
    input("サイコロを振ってください")
    print(shake_dice, "がでました。", "現在位置は", cur_x, "です。")
print("おめでとうございます、ゴールしました！")
