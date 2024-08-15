#Lists
fruits = ['apple','banana','orange']

fruits.append('grape')                  # to add one item at the end of the list
fruits.extend(['grape','pineapple'])    # to add multiples items at the end
print(fruits)

# Length of list
print(len(fruits))

# Creating Lists with range function
my_range = list(range(2, 11, 2))    # range function result not printable
print(my_range)

for even_num in my_range:
    print(even_num)

# insert item at specific location
fruits.insert(3,'blueberry')
print('Blueberry at index 3:',fruits)

# Changing a range of items
fruits[1:3] = ['kiwi','strawberry']
print('Change index 1 and 2:',fruits)

# Check types
print('Types:',type(fruits))

# Removing
removed_item = fruits.pop(2)
print('Removed index 2: is',removed_item)

fruits.remove("cherry")

#Deleting index 0
del fruits[0] # without the [0], the whole list is deleted
print(fruits)

#Clearing the list, it will be an empty list after this
fruits.clear()

#Sorting
print(fruits)
fruits.sort(reverse=True) # Reverse alphabetical
print('Reverse Alphabetical:',fruits)

#Looping 
fruits1 = ['apple','banana','orange']

#Same output for all the 3 loops below
for x in fruits1:
    print(x)

for i in range(len(fruits1)):
    print(fruits1[i])    

i = 0
while i < len(fruits1):
    print(fruits1[i])
    i = i + 1