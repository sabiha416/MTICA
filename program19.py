def extract_Vowel(s):
    n_Vowel=0
    for i in s:
        if i in 'aeiou':
            n_Vowel+=1
    return n_Vowel


str1=input()
a=extract_Vowel(str1)
print("no of Vowel in:'",str1,"' is",a)
