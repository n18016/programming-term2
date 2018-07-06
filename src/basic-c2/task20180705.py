# 買い物の支払いを求める
# 値段
bi_ll = 200
otumami = 100
yakitori = 80
# 個数
bi_ll1 = 2
otumami1 = 1
yakitori1 = 2
# 割引率
rate = 150
# 計算
goukei = (bi_ll * bi_ll1) + (otumami * otumami1) + (yakitori * yakitori1) - rate
# 結果を表示
print("買い物の合計は", goukei, "円" )
