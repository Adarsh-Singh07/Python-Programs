'''N=int(input("Enter the Higher Number"))
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
        print(i, end=" ")'''

'''for i in range(10,0,-1):
    print(num)'''

'''#Fibonacci Series
N=int(input("Enter the Number"))
a=0
b=1
for i in range(0,N,1):
    print(a, end=" ")
    c= a+b
    a=b
    b=c'''
'''#SquaresOFNumber
N=int(input("Enter the Number"))
squares= [num**2 for num in range(1, N)]
print(squares)
#Fibonacci
N=int(input("Enter the Number"))
a=0
b=1
while(N>0):
    print(a, end=" ")
    c= a+b
    a=b
    b=c
    N=N-1'''
N=int(input("Enter the Number", end=" "))
i=1
for i in range(1, N+1):
    for j in range(1,11):
               print("%4d"%(i*j), end=" ")
    print()
