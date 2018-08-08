money = 1000
items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print("財布には", money, "円入っています")
    print(item_name + 'は１個' + str(items[item_name]) + '円です')
    input_count = input('購入する' + item_name + 'の個数を入力してください:')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')

    count = int(input_count)
    total_price = items[item_name] * count
    print('支払金額は' + str(total_price) + '円です')

    if money > total_price:
        a = "{0}を{1}個買いました".format(item_name, input_count)
        print(a)
        money = money - (items[item_name] * count)
    else:
        b = "お金が足りません。{0}を買えませんでした。".format(item_name)
        print(b)
