from re import I


i=1
s=0
n=int(input("enter a nummber="))
while(i<n):
    if(n%i==0):
        s=s+i
    i+=1
if(s==n):
    print("perfect number")
else:
    print("not perfect number")