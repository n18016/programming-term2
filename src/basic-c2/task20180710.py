# 自分が絶対に勝てないプログラム
print("じゃんけんをしましょう")
jan_ken = int(input("何を出すか数字を入力してください。1:グー、2:チョキ、3:パー"))

#変数
rock = "CPUがグーを出しました。あなたの負けです。"
scissors = "CPUがチョキを出しました。あなたの負けです。"
paper = "CPUがパーを出しました。あなたの負けです。"
error = "入力が不正です。終了します。"
#判定
if jan_ken == 1:
    print(rock.format("パー"))
elif jan_ken == 2:
    print(scissors.format("グー"))
elif jan_ken == 3:
    print(paper.format("チョキ"))
else:
    print(error)
