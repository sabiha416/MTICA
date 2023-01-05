def count_Consonent(s):
    n_Consonent=0
    for i in s:
        if i in 'bcdfghjkl':
            n_Consonent+=1
    return n_Consonent


str1=input()
a=count_Consonent(str1)
print("no of Consonent in:'",str1,"' is",a)
