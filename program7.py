def printDay(dn):
    if (dn==1):
        return "MONDAY"
    elif(dn==2):
        return "TUESDAY"
    elif(dn==3):
        return "WEDNESDAY"
    elif(dn==4):
        return "THURSDAY"
    elif(dn==5):
        return "FRIDAY"
    elif(dn==6):
        return "SATURDAY"
    elif(dn==7):
        return "SUNDAY"
    
    else:
        return "invalid"

def printDay1(dn):
    mn=''
    if (dn==1):
        mn = "MONDAY"
    if(dn==2):
        mn = "TUESDAY"
    if(dn==3):
        mn = "WEDNESDAY"
    if(dn==4):
        mn = "THURSDAY"
    if(dn==5):
        mn = "FRIDAY"
    if(dn==6):
        mn = "SATURDAY"
    if(dn==7):
        mn = "SUNDAY"
    
    return mn
import time
for i in range(7):
    inpNum=int(input())
    start=time.time()
    print(printDay(inpNum))
    print((time.time()-start)*100000)
    start=time.time()
    print(printDay1(inpNum))
    print((time.time()-start)*100000)
