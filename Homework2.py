#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
        

    def set_a(self, number):
        self.a = number
        return self.a

    def set_b(self, number):
        self.b = number
        return self.b

    def get_sopriazhonnoe(self):
        return Complex(self.real, -1 * self.imag)

    def get_module(self):
        self.m = np.sqrt(self.real ** 2 + self.imag ** 2)
        return self.m

    def get_phi(self):
        if self.a > 0:
            self.phi = np.arctan(self.b / self.a) * 180 / np.pi

        elif self.a < 0 and self.b > 0:
            self.phi = (np.arctan(self.b / self.b) + np.pi) * 180 / np.pi

        elif self.a < 0 and self.b < 0:
            self.phi = (np.arctan(self.b / self.a) - np.pi) * 180 / np.pi

        elif self.b == 0:
            self.phi = 0

        elif self.a == 0:
            self.phi = 90

        return self.phi
          
            
        
    def complex_to_exp(self):
        self.r = (self.a**2 + self.b**2)**0.5

        if self.a > 0 and self._b > 0:
            self.phi = np.arctan(self.b/self.a)

        if self.a < 0 and self.b > 0:
            self.phi = np.pi - np.arctan(self.b/abs(self.a))

        if self.a < 0 and self.b < 0:
            self.phi = np.pi + np.arctan(abs(self.b)/abs(self.a))

        if self.a > 0 and self.b < 0:
            self.phi = 2 * np.pi - np.arctan(abs(self.b)/self.a)

        if self.a == 0 and self.b > 0:
            self.phi = np.pi/2

        if self.a == 0 and self.b < 0:
            self.phi = - np.pi / 2

        if self.a == 0 and self.b == 0:
            self.phi = 0

        if self.a > 0 and self.b == 0:
            self.phi = 0

        if self.a < 0 and self.b == 0:
            self.phi = np.pi
            
            return self.r, self.phi

    def exp_to_complex(self):
        if self._r == 0:
            self.a, self.b = 0, 0
        else:
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


# 1) ООП (объектно-ориентированное программирование) - методология программирования, основанная на представлении программы в виде совокупности взаимодействующих объектов, каждый из которых является экземпляром определённого класса, а классы образуют иерархию наследования. В процедурном программировании все идет одним текстом без разделения похожих частей, возможны повторения. 
# В функциональном программировании рассматривается вычисление как оценка математических функций и избегает переменных состояний и изменяемых данных. А также избегаются повторы в коде.
# 2) Инкапсуляции заключается в различении методов и переменных (составляют объект, к ним пользователь может обращаться) и компоненты, к которым пользователь не может обращаться (private). В Python инкапсуляция условная (возможно, что private может обратиться к переменным). Перед названием private переменных в начале ставится нижнее подчеркивание.
# 3) Переменные - поле, функции - методы.
# 4) Создание экземпляра класса начинается вызовом конструктора класса, который выделяет память под наш объект, связывает переменную и объект класса, а продолжает инициализатор, который принимает аргументы конструктора для инициализации созданного объекта, кладет значение в параметры класса.

