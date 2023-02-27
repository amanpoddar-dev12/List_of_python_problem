a=str(input("enter string to check:"))
a=a.casefold()

if (a==a[::-1]):
    print("yes,this is  pallindromme:")
else:
    print("no,this is not a pallindrome:")