def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は', hands[player_hand], 'を出しました')
print('じゃんけんをはじめます')
player_name = input('名前を入力してください:')
print("何を出しますか？(0: グー, 1: チョキ, 2: パー)")
player_hand = int(input('数字で入力してください:'))

if player_name == '':
    print_hand(player_hand)
else:
    print_hand(player_hand, player_name)
