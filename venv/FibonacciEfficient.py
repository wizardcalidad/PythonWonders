'''Recursive fibonacci that remembers previous values, it is more effcient that using just the recursive method'''
import time
def fibonacci (n):
    if n not in fibo_dict:
        fibo_dict [n]= fibonacci(n-1) + fibonacci(n-2)
    return fibo_dict[n]

fibo_dict = {}
fibo_dict[0] = 0
fibo_dict[1] = 1

fibo_val = input("calculate what fibonacci value: ")
fibo_val = int(fibo_val)
start = time.time()
print("fibonacci value of", fibo_val, "is", fibonacci(fibo_val))
print(f"fibonacci(n), took {time.time()-start} sec(s)")