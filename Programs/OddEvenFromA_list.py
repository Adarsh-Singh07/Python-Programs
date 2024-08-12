number=[]
N= int(input("Enter The list length"))
for i in range(N+1):
    
    number.append(int(input("Enter The Number")))
num = []
for j in number:
    if j % 2==0:
        num.append(j)

print(number)
print(num)
