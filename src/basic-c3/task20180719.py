# 四則計算プログラム
print("四則計算プログラムです。")

# 足し算を行うための関数を定義
def add(a, b):
    '''足し算を行う関数'''
    return a + b
# 引き算を行うための関数を定義
def sub(a, b):
    '''引き算を行う関数'''
    return a - b
# 掛け算を行うための関数を定義
def mul(a, b):
    '''掛け算を行う関数'''
    return a * b
# 割り算を行うための関数を定義
def div(a, b):
    '''割り算を行う関数'''
    return a / b
# 四則計算
print("四則計算のプログラムです。")
while True:
    parameter1 = input("第１パラメータを入力してください>>>")
    num1 = float(parameter1)
    break
    except ValueError:
        print("入力が間違っています。数値を入力してください。")

while True:
    parameter2 = input("第２パラメータを入力してください。")
    num2 = float(parameter2)
    break
    except ValueError:
        print("入力が間違っています。")

while True:
    user = input("演算方法を入力してください>>>")
    if user == "+":
        add = parameter1 + parameter2
        print(add)
        break
    if user == "-":
        sub = parameter1 - parameter2
        print(sub)
        break
    if user == "*":
        mul = parameter1 * parameter2
        print(mul)
        break
    if user == "/":
        div = parameter1 / parameter2
        print(div)
        break
    else:
        print("入力が間違っています。")
