fo=open(r"C:\pythonpractice49\Day9\abc2.txt","w+")
inpstr=input('Enter text:')
fo.write(inpstr)
inpstr=input('Enter text:')
fo.write(inpstr)

fo.close()
print("Text written to file")
