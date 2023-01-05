
def printDetail(Name,marks=40,Age=18):
    print("Name:",Name)
    print("Marks:",Marks)
    print("Age:",Age)
    return None

##printDetail()#error
##printDetail('sabiha')
printDetail('sabiha',87)
printDetail(87,'sabiha')


printDetail(marks=87,name='sabiha')#Keyword argument
