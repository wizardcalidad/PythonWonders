s = 'ABC'
for x in s:
    for y in s:
        for z in s:
            if x!=y and x != z and y != z:
                print(x,y,z)