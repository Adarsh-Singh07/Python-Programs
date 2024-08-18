'''Write a python program to find the list of words
that are longer than n from a given list of words.'''

word_list = ["Rohit", "Sharma", "Adarsh", "Singh", "Jasprit", "Bumrah", "Virat", "Kohli"]
value = int(input("Enter the value: "))

for i in word_list:
    if len(i) > value:
        print("The words which are greater than are", value, "are: ", i)
    else:
        print("NULL VALUE")



'''Write a program to create a new list from an existing list from removing all odd numbers.'''

num_list = [1,2,3,4,5,6,7,8,9,10]
new_list = []

for i in num_list:
               if (i % 2 == 0):
                   new_list.append(i)
print("Previous List: ", num_list)
print("New List: ", new_list)
