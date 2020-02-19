num = int(input("Enter an integer: "))
count =0

while num>0:
    if num % 2 ==0:
        num = num
    elif num % 3 == 0:
        num = num
    else:
        num = num - 1
    count = count + 1

print("Count is: ", count)
print("Number is: ", num)