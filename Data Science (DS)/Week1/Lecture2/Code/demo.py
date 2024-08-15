# Create a list []
names = ["Zahra", "Jeff", "Alice", "Bob"]
names = []


# Add, access, remove elements in a list
names.append("Zahra")
names.append("Jeff")
names.append("Alice")

print(names[2])

names.pop(0)


# Create a dictionary {}
names_dict = {"Zahra": 24, "Jeff": 18, "Alice": 10}


# Add, access, remove elements in a list
names_dict["Bob"] = 52
print(names_dict["Alice"])
names_dict.pop("Bob")


# Create a while loop
done = True

while (done):
    if (input("Hi\n") == "Hi"):
        done = False


# Create a for loop
for i in names:
    print(i)



# [] - lists
# {} - dictionaries
# [] - indexing
# () - maths, functions