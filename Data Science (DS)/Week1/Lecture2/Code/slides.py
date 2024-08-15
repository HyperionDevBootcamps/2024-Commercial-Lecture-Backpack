my_list = [1, "two", "buckle", True]

print(my_list[0])  # 1
print(my_list[3])  # True

my_list.append("three")
my_list.insert(0, "zero")

my_list.remove("zero")
my_list.pop(3)

# my_list.sort()
my_list.reverse()

string = "hello"
print(string[0]) # h

string.find("h")


my_dict = {"name": "Zahra", "age": 24}
my_dict = dict(name = "Zahra", age = 24)

my_name = my_dict["name"]

my_dict["bday"] = "13 November"

my_dict.pop("bday")

condition = True
sequence = []

while (condition):
    # Block of code to repeat
    pass

for loop_variable in sequence:
    # Block of code to repeat
    pass


range(20)       # [0 .. 19]
range(1, 20)    # [1 .. 19]
range(1, 2, 20) # [1, 3, 5, .. 19]

