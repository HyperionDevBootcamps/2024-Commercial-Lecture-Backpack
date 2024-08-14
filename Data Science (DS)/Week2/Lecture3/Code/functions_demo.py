# FUNCTIONS
import math

# Example of a function with input and output
# ax^2 + bx + c = 0
# Produces at most two x values
def calculateQuadraticEquation (a, b, c):
    num = math.sqrt(pow(b, 2) - (4 * a * c))
    den = 2 * a
    x1 = (-b + num) / den
    x2 = (-b - num) / den
    return [x1, x2]

# Example of a function which doesn't return a value
def welcomeMessage(name):
    print('Welcome to our Lecture ' + name)

# Example of a function which doesn't have input
def getRandomNumber():
    num = int(input("Enter a random number: "))
    return num

# Function which calculates the sum of two numbers
def calculateSum(a, b = 3):
    return a + b


sum1 = calculateSum(800982390, 247332) # 801229722
sum2 = calculateSum(sum1, 3)   # 801229725

sum3 = calculateSum(8613493847941) # set b to something in the function
print(sum3)

print(sum1) 
print(sum2)

print(calculateQuadraticEquation(1, 2, -5))
xs = calculateQuadraticEquation(10, 3, -8)
x1 = xs[0]
x2 = xs[1]
print(x1)
print(x2)

welcomeMessage("Zahra")
num = getRandomNumber()