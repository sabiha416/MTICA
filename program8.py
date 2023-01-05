import time

inpNum =int(input("Enter a no: "))
start=time.time()
for i in range(inpNum):
    print("i=",i,"^2=",i*i)
print("Time taken by loop:",
      (time.time()-start)*100000)
