
largest = -1
smallest = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print('Invalid input')
        continue

    if num > largest:
        largest = num

    if smallest is 0:
        smallest = num
    if num < smallest:
        smallest = num




print("Maximum", largest)
print("Minimum", smallest)