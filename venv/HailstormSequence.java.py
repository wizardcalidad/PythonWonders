num = int(input("Enter any number: "))
i = 1
while num !=1:
    if num % 2 == 0:
        num = num / 2
       # print(num, "is even")
    else:
        num = (num * 3) + 1
       # print(num, "is odd")
    print(num,",", end='')
    i +=1

else:
    print()
    print("Sequence is",i,"numbers long")