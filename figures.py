from typing import Tuple, List
import numpy as np
from math import sqrt

class Point:
    def __init__(self, x: float , y: float):
        self.x = x
        self.y = y

#not the best place to implement any functions but ok
#TODO: find a better place for this shit
def distance(a: Point, b: Point)->float:
    return sqrt(a.x*b.x + a.y*b.y)



class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end



class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def cirCircle(self):
        (x1, y1), (x2, y2), (x3, y3) = self.a, self.b, self.c
        A = np.array([[x3-x1,y3-y1],[x3-x2,y3-y2]])
        Y = np.array([(x3**2 + y3**2 - x1**2 - y1**2),(x3**2+y3**2 - x2**2-y2**2)])
        
        if np.linalg.det(A) == 0:
            return False
        
        Ainv = np.linalg.inv(A)
        X = 0.5*np.dot(Ainv,Y)
        x,y = X[0],X[1]
        r = sqrt((x-x1)**2+(y-y1)**2)
        
        return (x,y),r


class Circle:
    def __init__(self, o: Point, r: float):
        self.o = o
        self.r = r
        
    def isInCircle(self, p: Point)->bool:
        if distance(self.o, p) <= self.r:
            return True
        else:
            return False

