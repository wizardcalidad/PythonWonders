the_max = int(input("Enter your maximum value of range"))
the_sum = 0
extra = 0

for number in range(1, the_max):
    if (number % 2==0) & (number % 3 != 0):
        the_sum =the_sum + number
    else:
        extra = extra + 1
print(the_max)
print(extra)