num = int(input("Please enter a number: "))
sum = 0
i =0;

while num != ".":
    if num % 2 == 0:
        sum = sum + num
    elif num % 2 == 1:
        print("Dont add to sum")
        break
    num = int(input("Please enter a number: "))
    i = i+1;
print("The sum is: ",sum)
