from random import choice
score_you = 0
score_com = 0
direction = ['left', 'center', 'right']

for i in range(5):
    print('=====round %d--you kick =====', i+1)
    print('choose which side to shoot:')
    print('left, center, right')
    you = input()
    print('you had kick' + str(you))
    if you == 'EOF':
        break
    com = choice(direction)
    print('you had choose' + com)
    if you != com:
        print('Goal')
        score_you += 1
