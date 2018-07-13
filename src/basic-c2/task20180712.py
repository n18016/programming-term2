# 九九のプログラム計算
# 掛けられる数
str_line = ""
str_line = str_line + "|".rjust(3)
# 掛ける数
for x in range(1, 10):
    str_line = str_line + str(x).rjust(3)
print(str_line)
# 線
str_line = ""
str_line = str_line +  "--" "+" + "-" * 27
print(str_line)
# 計算内容
for x in range(1, 10):
    str_line = ""
    str_line = str_line + str(x).rjust(2) + "|"
    for y in range(1, 10):
        cross_result = x * y
        str_line = str_line + str(cross_result).rjust(3)
    print(str_line)
