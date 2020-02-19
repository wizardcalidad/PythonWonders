score = input("Enter Score between 0.0 and 1.0: ")
try:
    score = float(score)

    try:
        if score >=0.0 and score <=1.0:

            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >= 0.7:
                print("C")
            elif score >= 0.6:
                print("D")
            else:
                print("F")
    except ValueError:
        print("Score should be between 0 and 1")
        quit()
except ValueError:
    print("The score entered is not a float")
    quit()