# Write random numbers between 0 and 100 to a text file
import random

# Open the file
marks = open("marks.txt", "w")

# Number of students
n = 20

for i in range(20):
    marks.write(str(random.randrange(0, 101)))
    marks.write("\n")

marks.close()

# Display the marks to the screen

# Add in a new mark to the end of the file