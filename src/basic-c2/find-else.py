# for 構文で　else を記述する場合
#　食材の一覧
#foodstuff = ["Banana", "Mango" ,"fish", "carrot", "cabbage"]
foodstuff = ["Banana", "fish", "carrot", "cabbage"]
#マンゴーがないか確認する
for food in foodstuff:
    if food == "Mango":
        print("マンゴーが入っています")
        break
else:
    print("ありません")
