#!/usr/bin/env python3

def print_fibonacci(length):
    #0,1,1,2,3,5
    if length == 0:
        print([])
        return None
    elif length == 1:
        print([0])
        return None
    elif length >= 2:
        fib = [0,1]
        for i in range(length-2):
             fib.append(fib[i] + fib[i+1])
        print(fib)
    return None