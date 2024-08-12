#Write A Script to Display the output of list of N numbers that if any one is prime ,, if list contains All Non- prime then Find the Sum of all the Numbers and If sum is prime then output is False
number=[]
N= int(input("Enter The list length: "))
for i in range(N):
    
    number.append(int(input(f"Enter The Number {i+1}: ")))
count = 0
NonPrime= []
for i in number:
    j=2
    while(j<=i//2):
        if i % j ==0:
            NonPrime.append(i)
            break
        else:
            j= j+1
        if j == i/2:
            print("False Statement as at least one of the given numbers is a Prime Number")
            break
Sum =0
for i in NonPrime:
    Sum = i + Sum
k=2 
while(k<=Sum//2):
    if Sum % k ==0:
        print(Sum, " is the total sum of the list, as none of the given elements of the List are Prime ")
        break
    else:
        k= k+1

if k >= Sum//2:
    print("False Statement as even if none of the given elements of the List are Prime but sum of those numbers is Prime")
    
