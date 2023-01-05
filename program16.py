def extract_SpecialCharecter(s):
    n_SpecialCharecter=0
    for i in s:
        if i in '0123456789':
            n_SpecialCharecter+=1
    return n_SpecialCharecter


str1=input()
a=extract_SpecialCharecter(str1)
print("no of SpecialCharecter in:'",str1,"' is",a)
