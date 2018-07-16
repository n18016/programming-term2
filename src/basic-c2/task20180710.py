# 自分が絶対に勝てないプログラム
print("じゃんけんをしましょう")
jan_ken = int(input("何を出すか数字を入力してください。1:グー、2:チョキ、3:パー"))

#変数
error = "CPUが{0}を出しました。あなたの負けです。"
#判定
if jan_ken == 1:
    print(error.format("パー"))
elif jan_ken == 2:
    print(error.format("グー"))
elif jan_ken == 3:
    print(error.format("チョキ"))
else:
    print("入力が不正です。終了します。")
