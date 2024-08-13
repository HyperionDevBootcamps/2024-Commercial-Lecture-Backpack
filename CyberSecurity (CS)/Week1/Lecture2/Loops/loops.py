"""
---------------------------------------------------------------------------
Task 1 --> For Loop

Create a symmetrical 2D Pyramid using only spaces and asterisks.

---------------------------------------------------------------------------

Task 2 --> While Loop

Write a program that asks the user to enter numbers continuously until they
enter 0.

The program should then calculate the sum and average of all entered numbers,
excluding the 0.

Enter a number (or '0' to stop): 5
Enter a number (or '0' to stop): 10
Enter a number (or '0' to stop): 3
Enter a number (or '0' to stop): 0

Sum:
Average:
---------------------------------------------------------------------------
"""


# For Loop:

# Propmt user for the amount lines for pyramid
# Use for loop to print pyramid

lines = int(input("Enter the size of the pyramid:"))
asterisk = ""

for i in range(lines):
    asterisk += "*"
    print(asterisk)

"""
asterisk = ""

1
asterisk --> "*"
print above

2
asterisk --> "**"
print above


3
asterisk --> "***"
print above




*
**
***
****
*****
****
***
**
*
"""




# While

# Condition for while loop?
# user_input = int(input("Enter a number (or '0' to stop): "))
# sum_numbers = user_input
# amount_numbers = 1

# while user_input != 0:
#     user_input = int(input("Enter a number (or '0' to stop): "))

#     if user_input != 0:
#         amount_numbers += 1
#         sum_numbers += user_input

# print("Amount of numbers: ", amount_numbers)
# print("Sum of all numbers excluding 0: ", sum_numbers)

# average = sum_numbers/amount_numbers
# print("Average ", average)
