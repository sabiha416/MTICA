def printSeriesDecreasing(ch,n):
    assert isinstance(ch,str),"first argument should be string"
    assert isinstance(n,int),"second argument should be string"

    for i in range(n,0,-1):
        print(ch*i)
    return None



inpch=input("Enter a charecter:")
inpNum=int(input("Enter a no:"))

print('-'*40)
try:
    print(printSeriesDecreasing(inpch,inpNum))
except AssertionError as obj:
    print(ob)
