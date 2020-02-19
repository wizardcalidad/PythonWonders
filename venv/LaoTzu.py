# The journey of a thousand miles begins with a step

def take_step (n):
    if n==1:    #base case
        return "Easy"
    else:
        this_step = "step(" + str(n) + ")"
        previous_steps = take_step(n-1) #recursive steps
        return this_step + " + " + previous_steps

print(take_step(10))
