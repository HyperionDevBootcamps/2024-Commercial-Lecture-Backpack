# 1. Syntax Error Example

def calculate_average(numbers)
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print(f"The average is: {result}")

# Explanation:
# This code contains a syntax error.
# The function definition is missing a colon ':' after the parameter list.
# It should be: def calculate_average(numbers):
# Python uses the colon to indicate the start of a new code block.
# Without the colon, Python cannot correctly interpret the function definition.
# This will raise a SyntaxError when you try to run the code.
# The error will be detected by Python before the program starts executing.

# 2. Runtime Error Example

def divide_numbers(a, b):
    return a / b

num1 = 10
num2 = 0
result = divide_numbers(num1, num2)
print(f"The result of division is: {result}")

# Explanation:
# This code will cause a runtime error.
# When we try to divide num1 (10) by num2 (0), it will raise a ZeroDivisionError.
# Division by zero is mathematically undefined and not allowed in Python.
# This error occurs during program execution, not during compilation.
# The program will crash with a ZeroDivisionError when it tries to perform 10 / 0.

# 3. Logical Error Example

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temp_f = 100
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F is equal to {temp_c}°F")

# Explanation:
# This code contains a logical error.
# The conversion formula is correct, and the function will run without any errors.
# However, the print statement incorrectly labels both temperatures as °F.
# It should say "°C" for the Celsius temperature.
# This mistake in the output formatting is a logical error.
# The program runs without crashes but provides misleading information.
# Correct output should be: "100°F is equal to 37.77777777777778°C"