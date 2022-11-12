#!/usr/bin/env python
# coding: utf-8

# In[8]:


def fibo_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a ### или b, тогда будет генерироваться, начиная с 1
        a, b = b, a + b

for i in fibo_generator(10):
    print(i)

