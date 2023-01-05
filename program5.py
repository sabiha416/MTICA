def div(a,b):
    assert( isinstance(a,int) or isinstance(a,float)),\
            'first Argument should be either Integer or float'
    assert( isinstance(b,int) or isinstance(b,float)),\
            'second Argument should be either Integer or float'       
    assert (b!=0),"Division by zero is not defined"
    return a/b

try:
    print (div(55,0))
except AssertionError as obj:
    print(obj)
try:
    print (div(20,3))
except AssertionError as obj:
    print(obj)
try:
    print (div('hello',20))
except AssertionError as obj:
    print(obj)
try:
    print (div(20,'hello'))
except AssertionError as obj:
    print(obj)
