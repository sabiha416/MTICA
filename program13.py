##string=input()
##
##ans=[i for i in string if i not in 'AEIOUaeio']
##print(ans)


string='''practice problem for list comprehension in python.'''

ans=[i for i in string if i not in 'AEIOUaeio']
print(''.join(ans))
