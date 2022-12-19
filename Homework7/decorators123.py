#!/usr/bin/env python
# coding: utf-8

# In[22]:


def reverse_args(foo):   
    def wrapper (*args):
        a = []
        for x in args:
            a.append(x)
        a.reverse()
        return (foo(*a))
    return wrapper


def print_args (foo):
    def wrapper (*args):
        foo(*args)
        print(*args)
    return wrapper

def exception(foo):
    def wrapper (*args):
        try:
            foo(*args)
        except Exception:
            print ("error")
    return wrapper


@reverse_args
def foo_1(*args):
    print(*args)

@print_args
def foo_2(*args):
    print(sum(args))

    
@exception    
def foo_3 (*args):
    print(args[0]*args[1])



foo_1( 1, 2, 3, 4, 5, "adv")
foo_2( 1, 2, 3, 4, 5)
foo_3( 'a', 'b')

