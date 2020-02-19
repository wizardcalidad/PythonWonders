
naira = int(input("Enter amount to convert in naira: "))
dollar = 1
pound = 1

if naira > 360:
    dollar = naira / 360
    pound = naira / 471
print(f'${dollar:.2f} {pound:.2f}pounds')