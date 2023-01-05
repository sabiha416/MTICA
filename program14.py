def extract_Digit(s):
    n_Digit=0
    for i in s:
        if i in '0123456789':
            n_Digit+=1
    return n_Digit


str1=input()
a=extract_Digit(str1)
print("no of vowels in:'",str1,"' is",a)
