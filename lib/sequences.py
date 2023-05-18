#!/usr/bin/env python3

def print_fibonacci(lenght):
    fib_list = []
    a,b = 0,1

    for _ in range(lenght):
        fib_list.append(a)
        a,b = b, a + b


    print(fib_list)  
