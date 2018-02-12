from random import choice
list = ['li', 'wang', 'heloo']
print(list[1])

list.append('ddd')

print('choose one side to shoot:')
print('left,center,right')
you = input()
print('you had choose ' + you)
direct = ['left', 'center', 'right']
com = choice(direct)
print('computer saved' + com)
if you != com:
    print('goal!')
else:
    print('ai')