##keys=['Ten','twenty','thirty']
##values=[10,20,30]
##d=dict()
##for i,j in zip(keys,values):
##    d[i]=j
##print(d)
##


##dict1={'Ten': 10, 'twenty': 20, 'thirty': 30}
##dict2={'thirty': 30, 'fourty': 40, 'fifty': 50}
##
##dict3={**dict1,**dict2}
##print(dict3)



dict1={'Ten': 10, 'twenty': 20, 'thirty': 30}
dict2={'thirty': 30, 'fourty': 40, 'fifty': 50}

dict3=dict1.copy()
dict3.update(dict2)
print(dict3)
print(dict3)
