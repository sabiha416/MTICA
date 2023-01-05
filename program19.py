class Number:
    def __init__(self,num):
        self.num=num
    def calculateFactorial(self):
        if self.num==0:
            return 1
        res=1
        for i in range(1,self.num +1):
            res *=i
            return res
    def checkEvenOdd(self):
        if self.num%2==0:
            return "Even"
        else:
            return "Odd"
    def sumOfDidits(self):
        if self.num<0:
            self.num=abs(self,num)
        temp=str(self.num)
        t=0
        for i in temp:
            t+=int(i)
        return t
        
    
inp=int(input())
obj=Number(inp)
print('factorial of ',inp,'is',obj.calculateFactorial())
print(inp,"is",obj.checkEvenOdd())
print('sum Of Digits of',inp,'is',obj.sumOfDidits())

   

