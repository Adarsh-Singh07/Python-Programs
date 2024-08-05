#Fibonacci Series
N=int(input("Enter the Number"))
a=0
b=1
for i in range(0,N,1):
    print(a, end=" ")
    c= a+b
    a=b
    b=c
