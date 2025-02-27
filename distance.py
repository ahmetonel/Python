import math

x1=int(input("X1: "))
y1=int(input("Y1: "))
x2=int(input("X2: "))
y2=int(input("Y2: "))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, p2):
        return math.sqrt((self.x - p2.x) ** 2  + (self.y - p2.y) ** 2 )


point1 = Point(x1,y1)
point2 = Point(x2,y2)

print("iki nokta arasindaki mesafe: ")
print(point1.distance(point2))

#Ahmet ONEL                                                          
