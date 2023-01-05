def checkpalindram():
    b=input()
    if b==b[::1]:
        return 'yes'
    else:
        return 'no'
inp=input("enter a number:")
print(checkpalindram())
