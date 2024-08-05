n=int(input("Enter the Number"))
i=2
f=0
while(i<=n//2):
    if(n%%i==0):
        f=1
        break
    i=i+1
if(f):
    print("The Number is Not prime")
else:
    print("The Number is prime")

