# 買い物の支払いを求める
# 値段
beer = 200
otumami = 100
yakitori = 80
# 個数
beer_n = 2
otumami_n = 1
yakitori_n = 2
# 割引率
rate = 0.2
# 割引
point_off = 150
# 計算
goukei = (beer * beer_n) + (otumami * otumami_n) + (yakitori * yakitori_n) - point_off
# 結果を表示
print("買い物の合計は", goukei, "円" )
