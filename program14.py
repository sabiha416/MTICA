
string='''
practice problem for list comprehension in python.
'''




##WordList=string.split(' ')
##ans=[i for i in WordList if len(i)==3]
##print(*ans)

WordList=string.split(' ')
ans=[i for i in WordList if len(i.strip('\n'))==8]
print(*ans)
