items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')
input_count = input()
price = "購入する{0}の個数は{1}です".format(item_name, input_count)
print(price)
count = int(input_count)
total_price = items[item_name] * count
total = "支払金額は{0}円です".format(total_price)
print(total)
