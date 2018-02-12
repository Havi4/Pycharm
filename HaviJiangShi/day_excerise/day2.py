from random import randint
range(1,100)
print(range)
for i in range(1,100):
    print(i)

num = 18
print('my age is', num)
num = 3.333
print('you and you is', num)

name = 'lili'
score = 74
print('%s is %d',(name,score))

print('123')
a = '123'
if a:
    print('this val is not null')

def sayHello():
    print('Hello python')

sayHello()

def sayhellos(someone):
    print('this is one' + someone)

sayhellos('li wen qiang')

def plus(num1, num2):
    print(num1 + num2)

def isEqual(num1 , num2):
    if num1 < num2:
        print("too small")
        return False
    elif num1 > num2:
        print("too big")
        return False
    elif num1 == num2:
        print("bingo")
        return True

num3 = randint(1, 100)
print('guess what i think')
bingo = False
while bingo == False:
    answer = eval(input())
    bingo = isEqual(answer, num3)

def func(x,y):
    if y >= 0:
       if x >= 0:
           print(1)
       else:
           print(2)
    else:
        if x < 0:
            print(3)
        else:
            print(4)
