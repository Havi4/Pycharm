position = (1, 2)
geeks = ('Sheldon', 'Leonard', 'Rajesh', 'Howard')
for name in geeks:
    print(name)

for name in geeks[:2]:
    print(name)

subGeeks = geeks[1:2]
print(subGeeks)

def getPostion(n):
    return (n/2, n*2)
x,y = getPostion(50)
print('%d:%d' %(x,y))