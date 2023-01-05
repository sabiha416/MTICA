def Factorial(num):
    assert(isinstance(num,int)),"factorial not defined for non integers"
    assert(num>=0),"factorial of negative is not defined!"
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)
try:
    print(Factorial(-45))
except Exception as obj:
    print(obj)
try:
    print(Factorial(4.9))
except Exception as obj:
    print(obj)
try:
    print(Factorial(45))
except Exception as obj:
    print(obj)

try:
    print(Factorial('today'))
except Exception as obj:
    print(obj)
