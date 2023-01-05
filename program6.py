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




for i in range(3):
    inpNum=int(input())
    print(printDay(inpNum))
