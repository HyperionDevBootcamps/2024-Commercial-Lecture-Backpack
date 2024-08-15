# Create a simple program which accepts the marks of a number of students
# and performs various functions on the dataset using for and while loops.

# Use a list to just store the marks of the students
# num_students = int(input("How many students in the class? "))
# marks = []

# for i in range(num_students):
#     mark = float(input("Enter a mark: "))
#     marks.append(mark)

# print(marks)

# Use a dictionary to store the names of the students and their marks
print("Enter the names and marks of your students, when done say 'done'.")
marks_dict = {}
user_input = input("Enter the name of a student: ")

while ((user_input.lower()) != "done"):
    name = user_input
    mark = float(input("Enter the mark of the student: "))
    marks_dict[name] = mark
    user_input = input("Enter the name of a student: ")

print(marks_dict)


# Calculate the average of the entered marks
# To get a list of values from a dictionary
marks = list(marks_dict.values())

# sum() function to add all elements together (alternatively use a for loop)
average = sum(marks) / len(marks)
print("Your class average is: {}".format(average))


# Display an ordered list of marks
# If you use a list, this will be simple. Just use the sort() function
# For a dictionary, its a little more complicated
print("Your class marks in order are: ")
sorted_marks = marks_dict.copy()

while (len(sorted_marks) != 0):
    # the min function can take a key parameter which is what is used to sort the list by value instead of key
    min_key = min(sorted_marks, key=sorted_marks.get)
    print("{:10} -> {:5}".format(min_key, sorted_marks[min_key]))
    sorted_marks.pop(min_key)



# Adjust the marks by a set amount (grade on a curve)
# For example, each element has to be multiplied by 0.5
