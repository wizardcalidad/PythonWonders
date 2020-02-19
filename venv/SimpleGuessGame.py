import random
rand = random.randint(0,100)
print("Hi-Lo Number Guessing Game: between 0 and 100 inclusive.")
guess = int(input("Please guess a number between 0 and 100: "))
print()
count = 0

while 0 <= guess <= 100:
    if guess > rand:
        print("Your guess is too high")
    elif guess < rand:
        print("Your guess is too low")
    else:
        print("You've guessed it right!", guess)
        break
    guess = int(input("Please guess a number between 0 and 100: "))

else:
    print("You're an early quitter! The correct guess is: ", rand)



    #count = count + 1

