class Rectangle:
    pi=27/7
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculateArea(self):
        temp=self.length*self.width
        return temp
    def calculatePerimeter(self):
        temp=2*(self.length + self.width)
        return temp
    
l=int(input())
w=int(input())
try:
    ob=Rectangle(l,w)
    area=ob.calculateArea()
    peri=ob.calculatePerimeter()
    print('area of rectanle is',area)
    print('perimeter of Rectangle is',peri)
except AssertionError as obj:
    print(obj)

