import numpy as np

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
        return Complex(self.a, -1 * self.b)

    def get_module(self):
        self.r = np.sqrt(self.a ** 2 + self.b ** 2)
        return self.r

    def get_phi(self):
        if self.a > 0 and self.b > 0:
            self.phi = np.arctan(self.b/self.a)

        elif self.a < 0 and self.b > 0:
            self.phi = np.pi - np.arctan(self.b/abs(self.a))

        elif self.a < 0 and self.b < 0:
            self.phi = np.pi + np.arctan(abs(self.b)/abs(self.a))

        elif self.a > 0 and self.b < 0:
            self.phi = 2 * np.pi - np.arctan(abs(self.b)/self.a)

        elif self.a == 0 and self.b > 0:
            self.phi = np.pi/2

        elif self.a == 0 and self.b < 0:
            self.phi = - np.pi / 2

        elif self.a == 0 and self.b == 0:
            self.phi = 0

        elif self.a > 0 and self.b == 0:
            self.phi = 0

        elif self.a < 0 and self.b == 0:
            self.phi = np.pi

        return self.phi
          
            
        
    def complex_to_exp(self):
        return self.get_module(), self.get_phi()

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


# 1) ООП (объектно-ориентированное программирование) - методология программирования, основанная на представлении программы в виде совокупности взаимодействующих объектов, каждый из которых является экземпляром определённого класса, а классы образуют иерархию наследования. 
# В процедурном программировании все пишеться одним текстом без разделения похожих частей, возможны повторения. 
# В функциональном программировании используются функции (в которые можно включить повторяющиеся части кода, и использовать их именно через вызов функции). То есть при функциональном программировании избегаются повторы и подменяемые части в коде. В нем нет классов и объектов, которые есть в ООП.
# 2) Инкапсуляции скрывает составляющие объект данные (методы и переменные) внутри класса, то есть предотвращает прямой доступ пользователя к деталям реализации. В Python инкапсуляция условная (есть возможность у пользователя обратиться к переменным).
# Для реализации инкапсуляции в Python перед названием переменных ставят нижнее подчеркивание.
# 3) Переменные - поле, функции - методы.
# 4) Создание экземпляра класса начинается вызовом конструктора класса, который выделяет память под наш объект, связывает переменную и объект класса. А продолжает инициализатор, который принимает аргументы конструктора для инициализации созданного объекта, кладет значение в параметры класса.

