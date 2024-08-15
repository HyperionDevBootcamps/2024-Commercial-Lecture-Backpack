# FUNCTIONS
import math

# Syntax of a user-defined function
def functionName(parameter1, parameter2): 
    # function block containing statements
    # which accomplishes a specific task 
    result = "Output"
    return result


# Function which calculates the sum of two numbers
def calculateSum(a, b):
    return a + b


sum1 = calculateSum(800982390, 247332) # 801229722
sum2 = calculateSum(sum1, 3)   # 801229725

print(sum1) 
print(sum2)

# FILES
# Reading 
file = open('file.txt', 'r')
file.read()
file.close()

# Writing
file = open('file.txt', 'w')
file.write("Hello World!")
file.close()

# Appending
file = open('file.txt', 'a')
file.write("\nThis is a new line.")
file.close()

# Creating and destroying a file object 
# Implicitly using with statement
with open('filename.txt', 'r') as file:
    content = file.read()

# Explicitly using open and close
file = open('filename.txt', 'r')
content = file.read()
file.close()


