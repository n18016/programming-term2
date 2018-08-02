# リストを生成
nums = [13600, 14500, 16000, 11111, 11667]

TAX_RATE = 8

x8 = lambda x : int(round(x * (1 + TAX_RATE / 100), -1))

print(list(map(x8, nums)))
