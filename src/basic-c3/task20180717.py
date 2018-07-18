import random
# リスト
fruits = ["Apple", "Banana", "Mango", "Orange"]
collar = ["red", "yellow", "green", "pink"]
condition = ["良いです", "普通です", "悪いです"]
# ランダム
a = random.choice(fruits)
b = random.choice(collar)
c = random.choice(condition)

d = "今日は{0}を食べると調子が{2}だけどラッキーカラーは{1}。".format(a, b, c)
# 出力
print(d)
