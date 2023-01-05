fo1=open(r"C:\pythonpractice49\Day10\abc4.txt","r")
fo2=open(r"C:\pythonpractice49\Day10\abc4.txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("file coppied")
