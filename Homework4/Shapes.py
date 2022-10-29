#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"        


def dist(a, b):
    return ((b.get_y() - a.get_y()) ** 2 + (b.get_x() - a.get_x()) ** 2) ** 0.5



class Shape:
    def __init__(self, type = "Shape"):
        self._type = type

    def __str__(self):
        return (str(self._type) + "   Area: S = " + str(self.area()) + "   Perimeter: P = " +  str(self.perimeter()))
    
    
class Circle(Shape):
    def __init__(self, r, o, type = "Triangle"):
        super().__init__(type)
        self._point_r = r
        self._point_o = o
        self._radius = dist(self._point_r, self._point_o)
        
    def perimeter(self):
        return round(2 * 3.14 * self._radius, 2)
    
    def area(self):
        return round(3.14 * self._radius ** 2, 2)
        

class Triangle(Shape):
    def __init__(self, p1, p2, p3, type = "Triangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._side_1 = dist(self._point_1, self._point_2)
        self._side_2 = dist(self._point_2, self._point_3)
        self._side_3 = dist(self._point_3, self._point_1)
        
    def perimeter(self):
        return round(self._side_1 + self._side_2 + self._side_3, 2)
    
    def area(self):
        p = self.perimeter() / 2
        return round((p * (p - self._side_1) * (p - self._side_2) * (p - self._side_3)) ** 0.5, 2)
    
    
class Rectangle(Shape):
    def __init__(self, p1, p2, p3, p4, type = "Rectangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._point_4 = p4
        self._side_1 = dist(self._point_1, self._point_2)
        self._side_2 = dist(self._point_2, self._point_3)
        self._side_3 = dist(self._point_3, self._point_4)
        self._side_4 = dist(self._point_1, self._point_4)
        
    def perimeter(self):
        return round(self._side_1 + self._side_2 + self._side_3 + self._side_4, 2)
    
    def area(self):
        return round(self._side_1 * self._side_2, 2)
    

class Square(Rectangle):
    def __init__(self, p1, p2, p3, p4, type = "Square"):
        super().__init__(p1, p2, p3, p4, type)

        
class Rhomb(Shape):
    def __init__(self, p1, p2, p3, p4, type = "Rhomb"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._point_4 = p4
        self._side_1 = dist(self._point_1, self._point_2)
        self._side_2 = dist(self._point_2, self._point_3)
        self._side_3 = dist(self._point_3, self._point_4)
        self._side_4 = dist(self._point_1, self._point_4)
        self._side_5 = dist(self._point_1, self._point_3)
        self._side_6 = dist(self._point_2, self._point_4)
        
    def perimeter(self):
        return round(self._side_1 + self._side_2 + self._side_3 + self._side_4, 2)
    
    def area(self):
        return round(self._side_5 * self._side_6 / 2, 2)
    
    
    # def __str__(self):
    #     return " ".join([super().__str__(), self._point_1.__str__(), self._point_2.__str__(),
    #                      self._point_3.__str__()])


a = Triangle(Point(0,0), Point(1, 1), Point(2, 3))
print(a)

b = Rhomb(Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1))
print(b)


# In[ ]:




