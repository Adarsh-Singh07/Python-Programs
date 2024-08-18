#Variable
x = 5
y = "John"
print(x)
print(y)

#Casting (to specify the data type of variable)
x = str(3)
y = int(4)
z = float(7)
print(x,y,z)

#Get the data type
x = 5
y = 'John'
print(type(x))
print(type(y))

#Camel Case
myVariableName = "John"

#Pascal Case
MyVariableName = "John"

#Snake Case
my_variable_name = "John"

#Many Values to Multiple Variables
x,y,z = 1,2,3
print(x,y,z)

#One Value to Multiple Variables
x = y = z = 1
print(x,y,z)

#Unpacking (If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables)
fruits = ["apple", "banana", "orange"]
x,y,z = fruits
print(x,y,z)

#Global Variable and Local Variable
x = "awesome" #global

def func():
    x = "fantastic" #local
    print("Python is " +x)

func()

print("Python is " +x)

'''Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.'''

def func():
    global x
    x = "fantastic"

func()

print("Python is " +x)

#Also use the global keyword if want to change a global variable inside a function
x = "awesome"
def func():
     global x
     x = "fantastic"

func()

print("Python is " +x)

#Strings
a = "hello world"
print(a[1])

#String Length
a = "Hello, World"
print(len(a))

#Check String(to check if certain phrase or character is present in a string)
txt = "Mount Everest is the highest peak in the world"
print("HITMAN" in txt)
print("peak" in txt)
print("expensive" not in txt)

#using if
if "peak" in txt:
    print("Yes, 'peak' is present")

if "expensive" not in txt:
    print("No, 'expensive' is not present.")










