from random import choice
score = [0, 0]
direction = ['left', 'center', 'right']
def kick():
    print('====You Kick====')
    print('please choose your direction:')
    print('left, right or right')
    you = input()
    print('you kicked:' + you)
    com = choice(direction)
    print('computer saved:' + com)
    if you == com:
        print('Goal!')
        score[0] += 1
    else:
        print('oh, no')
        score[1] += 1
    print('Score: %d(you)====%d(com)' %(score[0],score[1]))
for i in range(5):
    print('round === %d' %(i+1))
    kick()

if score[0] > score[1]:
    print('You win!')
else:
    print('Com Win')