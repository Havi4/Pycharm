try:
    f = open('tess.txt','r')
    f.close()
except:
    print('file not found')