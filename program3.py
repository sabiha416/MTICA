def findFrequency(s):
    FrequencyDict=dict()
    for i in s:
        if i in FrequencyDict:
            FrequencyDict[i]+=1
        else:
            FrequencyDict[i]=1
    return FrequencyDict
def formatOutput(d):
    for i in sorted(d):
        print(i,d[i])
    


n=int(input())
for i in range(n):
    inpstr=input()
    formatOutput(findFrequency(inpstr))
