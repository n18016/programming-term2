#  辞書型のデータ（メインメニューと価格）を変数に代入
main = {
    "DripCoffee":280, "ColdBrewCoffee":320, "CafeLatte":330, "SoyLatte":380, "Cappuccino":330, "CaramelFrappuccino":470, "MacchaCreamFrappuccino":470 }
# 辞書型のデータ（オプションと価格）を変数に代入
option = {
    "LowFatMilk":0, "NonFatMilk":0, "SoyMilk":50, "DeepCream":60, "WhipCream":70, "CaramelShrup":60, "ChocoSource":0, "DeCafe":50 }

menu_v = []
menu_f = []

while True:
    user_main = input("メインメニューを入力してください")
    if user_main in main:
        menu_v.append(user_main)
        print("メインメニューを承りました")
        break
    elif user_main == 'q' or user_main == '':
        print("注文をキャンセルします")
    else:
        print("選択したメニューはありません")
