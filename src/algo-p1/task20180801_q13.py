# 変数
apple_price = 200
money = 1000
input_count = input("購入するりんごの個数を入力してください:")
count = int(input_count)
total_price = apple_price * count
# 出力
print("購入するりんごの個数は" + str(count) + "個です")
print("支払金額は" + str(total_price) + "円です")
# 条件判断
if money > total_price:
    print("りんごを", count, "個買いました。残金は", money - total_price, "円です")
if money == total_price:
    print("りんごを", count, "個買いました。財布が空になりました")
if money < total_price:
    print("お金が足りません。りんごを買えませんでした")
