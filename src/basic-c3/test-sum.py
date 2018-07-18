# あるクラスの国語テストの点数をリストに代入
points = [88, 76, 67, 43, 79, 80, 91]

# テストの合計を求める
sum_v = 0
for i in points:  # 繰り返しの範囲にリストを指定
    sum_v += i
    print(i,"点を足して合計は", sum_v)

# 平均を求める
ave_v = sum_v / len(points)     # 平均　= 合計　/ 点数の数
print("平均点は", ave_v, "点")
