def printPattern(ch,n):
    assert (n>0),'invalid'
    for i in range(n,0,-1):
        print(ch*i)

ch=input()
n=int(input())
try:
    printPattern(ch,n)
except AssertionError as ob:
    print(ob)
