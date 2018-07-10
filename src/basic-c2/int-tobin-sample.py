# 変数の初期化
source_num = 100
target_num = source_num
sho = target_num
amari = 0

# 割られる数
devided_by = 2

# 結果
result_str = ""

# 商が1になるまで割り続ける
while sho > 1:
    sho = target_num // devided_by
    amari = target_num % devided_by
    target_num = sho
    result_str = str(amari) + result_str

result_str = str(sho) + result_str
print("2進数に変換した結果は", result_str, "です。")

