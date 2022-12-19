#!/usr/bin/env python
# coding: utf-8

# In[27]:


import time
from functools import lru_cache

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return wrapper

def recursion_fib(n):
    if n == 1 :
        return 0
    elif n == 2:
        return 1
    else:
        return recursion_fib(n - 1) + recursion_fib(n - 2)

@time_decorator
def recursion(n):
    return recursion_fib(n)


@lru_cache(maxsize=None)
def  recursion_Iru(n):
    return recursion_fib(n)

@time_decorator
def recursion_fib_Iru(n):
    return recursion_Iru(n)

def cycle_fib(n):
    a = 0
    b = 1
    if n == 1:
        return a
    if n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b

@time_decorator
def cycle(n):
    return cycle_fib(n)

@lru_cache(maxsize=None)
def  cycle_Iru(n):
    return cycle_fib(n)

@time_decorator
def cycle_fib_Iru(n):
    return cycle_Iru(n)

print('c lru_cache:')
print ('рекурсия', '-', recursion_fib_Iru(20))
print ('циклы', '-', cycle_fib_Iru(20))
print('без lru_cache:')
print ('рекурсия', '-', recursion(20))
print ('циклы', '-', cycle(20))

