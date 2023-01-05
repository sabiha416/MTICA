fo=open(r"C:\pythonpractice49\Day10.txt","a")
for i in range(5):
    inpstr=input("Enter string:")
    fo.write(inpstr+'\n')
fo.close()
print(" written to file")

