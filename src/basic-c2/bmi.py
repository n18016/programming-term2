# BMI判定プログラム
weight = float(input("体重(kg)は　? "))
height = float(input("身長(cm)は　? "))
# BMIの計算
height = height / 100 # m に直す
bmi = weight / (height * height)
#BMIの値に応じて結果を分岐
result = ""   # resultを空にしておく（初期化）
if bmi < 18.5:
    result = "痩せ型"
if (18.5 <= bmi) and (bmi < 25):
    result = "標準体重"
if (25 <= bmi) and (bmi < 30):
    result = "肥満（重）"
#結果を表示
print("BMI :",bmi)
print("判定:", result)
