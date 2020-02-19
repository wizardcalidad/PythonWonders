for i in range(2,11):
    jprod = ''
    for j in range(1,i):
        jprod = jprod+str(j)
    print("{2} * 8 + {0} = {1}".format(i-1,(int(jprod)*8+(i-1)),jprod))


