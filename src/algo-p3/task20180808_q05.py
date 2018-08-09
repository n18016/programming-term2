def print_hand(hand, name='ゲスト'):
    print(name + 'は' + hand + 'を出しました')
print('じゃんけんをします')
player_name = input('なまえをにゅうりょくしてください:')

if player_name == '':
    print_hand('グー')
else:
    print_hand('グー', player_name)
