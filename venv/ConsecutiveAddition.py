X = int(input("Enter a number: "))
sumOfX = 0
i = 0

for i in range(X+1):
    sumOfX = sumOfX + i
    if sumOfX % X == 0:
        print(sumOfX)

