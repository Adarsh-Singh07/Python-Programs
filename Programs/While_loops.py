#To check whether the program is prime or not
n = int(input("Enter the number: "))

i = 2
f = False

while (i<n//2):
     if(n%i==0):
          f = True
          break
     i += i
if (f==0):
     print(n,"is a prime number")
else:
     print(n,"is not a prime number")

#To check to a certain  range
n1=int(input())
n=int(input())
for num in range(n1,n+1):
    if num>1:
        
        d=2
        flag = False
        while d * d <= num:
            if(num%d==0):
                flag = True
                break
            d=d+1
    if flag==False:
        print(num,end=' ')

#To print reverse
for num in range(10,0,-1):
    print(num)
print("------------------------------------------")

for num in range(2,51):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print(num, end = " ")
print("\n------------------------------------------")

#To print sqaures
squares = [i**2 for i in range(1,11)]
print(squares)

#Table
for i in range(2,11):
 for j in range(1,11):
     print("%-3d"%(i*j), end=' ')
 print()

