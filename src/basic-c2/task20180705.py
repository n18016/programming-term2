# 買い物の支払いを求める
# 値段
beer = 200
otumami = 100
yakitori = 100
# 個数
beer_n = 2
otumami_n = 1
yakitori_n = 2
# 割引率
rate = 0.2
# 割引
point_off = 150
# 計算
beer_sum = beer * beer_n
otumami_sum = otumami * otumami_n
yakitori_sum = yakitori * yakitori_n * (1 - rate)
goukei = beer_sum + otumami_sum + yakitori_sum - point_off
# 結果を表示
print("買い物の合計は", goukei, "円" )
