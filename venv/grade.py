percent = float(input("What is your percentage?: "))
if 90 <= percent < 100:
    print("you received an A+")
elif 80 <= percent < 90:
    print("you received an A")
elif 70 <= percent < 80:
    print("You received a B+")
elif 60 <= percent < 70:
    print("You received a B")
elif 50 <= percent < 60:
    print("You recieved a C")
elif 40 <= percent < 50:
    print("You received a D")
elif 35 <= percent < 40:
    print("You received an E")
else:
    print("You received a F")