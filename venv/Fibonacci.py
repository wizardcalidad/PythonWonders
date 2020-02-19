'''It depends on the fibonacci results for the two previous values in the sequence, the sequence are 0,1,1,2,3,5,8,13,21,34,55,89,144..'''
import time
n = input("Enter a fibonacci position: ")
n = int(n)
def fibonacci (n):
    if n== 0 or n == 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
start = time.time()
print(f"fibonacci value of", n, "is", fibonacci(n))
print(f"fibonacci(n), took {time.time()-start} sec(s)")