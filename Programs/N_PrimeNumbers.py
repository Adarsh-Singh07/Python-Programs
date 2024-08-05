N=int(input("Enter the Higher Number"))
n= int(input("Enter the Lower Range"))
for i in range(n,N+1):
    f=0
    j=2
    while(j<=i//2):
        if(i%j==0):
            f=1
            break
        j=j+1
    if(f==0):
        print(i, end=" ")

