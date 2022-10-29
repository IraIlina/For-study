#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class ComplexNumber(object):
    def __init__(self, a, b = 0):
        self.home = {0: a, 1: b}
        self.a = self.home[0]
        self.b = self.home[1]
        
    
    
    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return False

    
    
    def __getitem__(self, key):
        if key == 0:
            return self.a
        elif key == 1:
            return self.b
        else:
            raise IndexError("2 indexes!!!")
    
    def __setitem__(self, key, value):
        if key == 0:
            self.a = value
        elif key == 1:
            self.b = value
        else:
            raise IndexError("2 indexes!!!")

        

    def get_sopriazhonnoe(self):
        return ComplexNumber(self.a, -1 * self.b)
    
    
    def __abs__(self):
        return np.sqrt(self.a ** 2 + self.b ** 2)
    

    def get_phi(self):
        if self.a > 0 and self.b > 0:
            self.phi = np.arctan(self.b / self.a)

        elif self.a < 0 and self.b > 0:
            self.phi = np.pi - np.arctan(self.b / abs(self.a))

        elif self.a < 0 and self.b < 0:
            self.phi = np.pi + np.arctan(abs(self.b) / abs(self.a))

        elif self.a > 0 and self.b < 0:
            self.phi = 2 * np.pi - np.arctan(abs(self.b) / self.a)

        elif self.a == 0 and self.b > 0:
            self.phi = np.pi / 2

        elif self.a == 0 and self.b < 0:
            self.phi = -np.pi / 2

        elif self.a == 0 or self.a > 0 and self.b == 0:
            self.phi = 0

        elif self.a < 0 and self.b == 0:
            self.phi = np.pi

        return self.phi
    

    
    def complex_to_exp(self):
        if self.a == 0:
            raise Exception("can't change the form")
        return self.__abs__(), self.get_phi()

    def exp_to_complex(self):
        self.r, self.phi = self.a, self.b
        self.a = np.cos(self.phi) * self.r
        self.b = np.sin(self.phi) * self.r 
        return self.a, self.b
 

    
    def add(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def mul(self, other):
        return ComplexNumber(self.a * other.a - (self.b * other.b), self.a * other.b + self.b * other.a)

    def sub(self, other):
        return ComplexNumber(self.a - other.a, self.b - other.b)
    
    def div(self, other):
        return ComplexNumber((self.a * other.a + self.b * other.b) / (other.a**2 + other.b**2), 
                             (self.b * other.a - self.a * other.b) / (other.a**2 + other.b**2))
    
    
x = ComplexNumber(1,0)
y = ComplexNumber(1,5)
print(y[1])

