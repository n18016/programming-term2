#繰り返し坪数を調べるプログラム
while True:
    user = input("坪数は? ")           #
    if user == "" or user == "q": break # 修正点
    tubo = int(user)                   #
    m2 = tubo * 3.31
    s = "{0}坪は {1}平方メートルです".format(tubo. m2)
    print(s)
