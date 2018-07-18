# for 構文で enumerate()を使う
fruits = ["Apple","Orange","Banana"]
for i , v in enumerate(fruits):
    print(i, v)

0 Apple
1 Orenge
2 Banana

# enumerate()の動作確認する
list(enumerate(fruits))
[(0, 'Apple'),(1, 'Orange'), (2, 'Banana')]
