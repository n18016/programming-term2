nums = list(range(1, 41))

num1 = lambda x : x % 3 == 0 or x // 10 == 3 or x % 10 == 3

print(list(filter(num1, nums)))
