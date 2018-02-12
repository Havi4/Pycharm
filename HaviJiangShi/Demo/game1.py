import re
from random import randint
isRight = False
computeNum = randint(1, 10)
fileManager = open('gameScore.txt','r')
scoreArr = fileManager.read().split()
fileManager.close()
totalGameCount = int(scoreArr[0])
totalGameCount += 1
fastGuessCount = int(scoreArr[1])
totalGuessCount = int(scoreArr[2])
currentGuessCount = 0
print(scoreArr)
while not isRight:
    inputString = eval(input('please input your num:'))
    if re.match(r'[+-]?d+$', inputString):
        inputNum = eval(inputString)
    else:
        input('please to input number:')
    currentGuessCount += 1
    if inputNum > computeNum:
        print('your num is big!')
    elif inputNum < computeNum:
        print('your num is litter!')
    else:
        print('good job! congratulations!')
        break
if totalGameCount == 1:
    fastGuessCount = currentGuessCount
elif currentGuessCount < fastGuessCount:
    fastGuessCount = currentGuessCount
totalGuessCount = totalGuessCount + currentGuessCount
result = '%d %d %d' %(totalGameCount,fastGuessCount,totalGuessCount)
print(result)
fileManager = open('gameScore.txt','w')
fileManager.write(result)
fileManager.close()


