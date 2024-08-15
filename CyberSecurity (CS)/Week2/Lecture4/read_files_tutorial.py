filename = "minutes_spents.txt"  # Define the filename where the data will be stored.
new_items = ["car", '8', '11', '13']  # Create a list of items to be written to the file.

# new_items = ["car\n", '8\n','11\n', '13\n']  # An alternative list where each item includes a newline character.

# Uncomment the following block to read the entire content of the file:
# data = open(filename, "r")  # Open the file in read mode.
# content = data.read()  # Read the entire content of the file into a string.
# # content = data.readlines()  # Alternatively, read the content line by line into a list.
# print(content)  # Print the content of the file.
# data.close()  # Close the file.

# Uncomment the following block to append a new line to the file using 'a+' mode:
# with open(filename, mode="a+") as data:  # Open the file in append mode.
#     data.write("tub\n")  # Write the string "tub\n" to the file.

# Uncomment the following block to append multiple items to the file:
# with open(filename, mode="a+") as data:  # Open the file in append mode.
#     data.writelines(new_items)  # Write the list of new items to the file.

# Uncomment the following block to read the file line by line:
# with open(filename, mode="r") as data:  # Open the file in read mode.
#     # content = data.read()  # Optionally read the entire file content into a string.
#     content = data.readlines()  # Read the file line by line into a list.
#     print(content)  # Print the list of lines.

# Uncomment the following block to read each line and perform a division operation:
# with open(filename, 'r') as file:  # Open the file in read mode.
#     for line in file:  # Iterate over each line in the file.
#         num = int(line.strip())  # Convert the line to an integer after stripping whitespace.
#         result = 1 / num  # Calculate the reciprocal of the number.
#         print(result)  # Print the result.

# The following block uses a try-except structure to handle potential errors during file processing:
try:
    with open(filename, 'r') as file:  # Open the file in read mode.
        for line in file:  # Iterate over each line in the file.
            character = line.strip()  # Strip any whitespace characters from the line.
            num = int(character)  # Attempt to convert the stripped line to an integer.
            result = 1 / num  # Calculate the reciprocal of the number.
            print(result)  # Print the result.
except ValueError as e:  # Handle the case where the line cannot be converted to an integer.
    print(f"Error: '{character}' is not a valid number.")  # Print an error message.
except ZeroDivisionError as e:  # Handle division by zero.
    print(f"Error: Cannot divide by zero ({character}).")  # Print an error message.
except FileNotFoundError:  # Handle the case where the file does not exist.
    print(f"Error: The file '{filename}' was not found.")  # Print an error message.
except IOError as e:  # Handle other I/O errors.
    print("Error: An I/O error occurred while reading the file.")  # Print a generic I/O error message.
