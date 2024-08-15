# Ask the user what their name is and greet them
print("Hello")
name = input("What is your name? ")

print("Hello " + name)

# Ask them what their favourite colour is and react accordingly
colour = input("What is your favourite colour? ")
print("I really like Blue.")
print("I guess " + colour + " is cool too.")


# Ask them how tall they are and react accordingly
height = input("How tall are you? ")
height = float(height)
#int(height)
#str(height)
#bool(height)
#eval(height)

if (height < 2):
    print("Wow, you are short!")
else:
    print("You can probably reach the heighest shelves :P")

# Ask them how old them are and calculate what grade they are in
age = input("How old are you? ")
age = int(age)

if (age < 7):
    print("Nearly time to start school!")
elif (age <= 18):
    grade = age - 6
    print("You must be in grade " + str(grade))
else:
    print("Wow you are old!")