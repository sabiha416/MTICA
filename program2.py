months={1:'january',2:'febrauary',3:'march',4:'april',5:'may',6:'june',7:'july',8:'august',9:'september',10:'october',11:'november',12:'december',}

n=int(input())

for count in range(n):
    mn=int(input())
    if mn>=1 and mn<=12:
        print(months[mn])
    else:
        print("invalid")
