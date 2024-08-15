# Write random numbers between 0 and 100 to a text file
import random

# Open the file
marks = open("marks.txt", "w")

# Number of students
n = 100

for i in range(n):
    marks.write(str(random.randrange(0, 101)))
    marks.write("\n")

marks.close()

# Display the marks to the screen
marks = open("marks.txt", "r")

marks_list = marks.readlines()
for mark in marks_list:
    print(mark.strip())

marks.close()

# Add in a new mark to the end of the file
new_mark = 89.0 # You change this to be a list and then add a for loop to add the marks to the text

with open("marks.txt", "a") as marks:
    marks.write("{:n}\n".format(new_mark))