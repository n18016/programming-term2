#  辞書型のデータ（メインメニューと価格）を変数に代入
main = {
    "DripCoffee":280, "ColdBrewCoffee":320, "CafeLatte":330, "SoyLatte":380, "Cappuccino":330, "CaramelFrappuccino":470, "MacchaCreamFrappuccino":470 }
# 辞書型のデータ（オプションと価格）を変数に代入
option = {
    "LowFatMilk":0, "NonFatMilk":0, "SoyMilk":50, "DeepCream":60, "WhipCream":70, "CaramelShrup":60, "ChocoSource":0, "DeCafe":50 }

for name, price in main.items():

    s = "注文内容は{0}金額は{1}円です。".format(name, price)
    print(s)
order_content = []
# メインメニュー選択
main_order = int(input("メインメニューを選んでください。"))
# まだ未完成です。
