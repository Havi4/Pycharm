print('oh my god, choose init num:')
num = eval(input())
result = False
while result == False:
    print('guess what i think?')
    answer = eval(input())

    if answer < num:
        print('too small')

    elif answer > num:
        print('too big?')

    elif answer == num:
        print('equal')
        result = True
