# === Introduction to Lists

# Creating a list with various data types
example_list = [1, "apple", 3.14, [5, 6, 7]]

# Accessing elements by index
print("Element at index 0:", example_list[0])  # Output: 1
print("Element at index 1:", example_list[1])  # Output: "apple"

# Accessing elements using negative indices
print("Last element:", example_list[-1])       # Output: [5, 6, 7]
print("Second to last element:", example_list[-2]) # Output: 3.14

# Demonstrating mutability
example_list[1] = "orange"  # Modifying an element
print("Modified list:", example_list)  # Output: [1, "orange", 3.14, [5, 6, 7]]

# === Iteration with Lists

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

# Summing numbers in a list
total_sum = 0
for number in numbers:
    total_sum += number
print("Sum of numbers:", total_sum)  # Output: 15

# Finding the maximum value in a list
max_value = numbers[0]
for number in numbers:
    if number > max_value:
        max_value = number
print("Maximum value:", max_value)  # Output: 5

# Transforming list items: Squaring each number
squared_numbers = []
for number in numbers:
    squared_numbers.append(number ** 2)
print("Squared numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# === Introduction to Dictionaries

# Creating a dictionary to map student names to their grades
grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92
}

# Accessing values using keys
print("Alice's grade:", grades["Alice"])  # Output: 90

# Adding a new key-value pair
grades["David"] = 88
print("Updated grades:", grades)  # Output: {'Alice': 90, 'Bob': 85, 'Charlie': 92, 'David': 88}

# Modifying an existing value
grades["Bob"] = 95
print("Modified grades:", grades)  # Output: {'Alice': 90, 'Bob': 95, 'Charlie': 92, 'David': 88}

# === Iteration with Dictionaries 

# Iterating over dictionary keys
print("Student names:")
for student in grades.keys():
    print(student)

# Iterating over dictionary values
print("\nStudent grades:")
for grade in grades.values():
    print(grade)

# Iterating over dictionary items (key-value pairs)
print("\nStudents and their grades:")
for student, grade in grades.items():
    print(f"{student}: {grade}")

# Modifying dictionary values based on conditions
# Example: Add 5 bonus points to students with grades below 90
for student in grades:
    if grades[student] < 90:
        grades[student] += 5
        # Above is same as => grades[student] = grades[student] + 5
print("\nGrades after bonus points:", grades)
# Output: {'Alice': 90, 'Bob': 95, 'Charlie': 92, 'David': 93}

