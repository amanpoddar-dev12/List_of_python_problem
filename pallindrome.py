from tkinter import N


n=int(input("enter a number="))
temp=n 
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if(temp==rev):
    print("PALLINDROME")
else:
    print("NOT PALLINDROME")