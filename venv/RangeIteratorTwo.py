for i in range(2,11):#(11,1, -1):
    num = ''
    for j in range(1,i):
        num = num +str(j)
    num = int(num)
    ans = num * 9 + i
   # print(num, 'x', 9, '+', i, '=', ans)
   # print(f'{num} x 9 + {i} = {ans}')
    print(f'{num:>10} x 9 + {i} = {ans}')
