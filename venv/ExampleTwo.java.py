#for the_char in 'hello, how are you':
 #   print(the_char)

number = int(input('Please enter a number to check'))
divisor = 1
sum = 0
while divisor < number:
    if number % divisor == 0:
        sum = sum + divisor
    divisor = divisor + 1
if number== sum:
    print(number, "is perfect")
elif number>sum:
    print(number, "is deficient")
elif number<sum:
    print(number,"is abundant")
else:
    print(number,"is not perfect")

