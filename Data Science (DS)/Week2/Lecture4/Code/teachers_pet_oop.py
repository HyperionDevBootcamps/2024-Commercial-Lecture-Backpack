# Create a Student and Teacher class
# Integrate it into our Teacher's Pet program

class Student:
    def __init__(self, g, s):
        self.gender = g
        self.score = s
    
    def print_student (self):
        print("{} -> {}".format(self.gender, self.score))


class Teacher:
    def __init__(self, name, student_list):
        self.name = name
        self.students = student_list
        self.class_average = self.calculate_average()
        self.class_size = len(self.students)

    def calculate_average(self):
        sum = 0

        for student in self.students:
            sum = sum + student.score 

        return sum / len(self.students)
    
    def calculate_range(self):
        class_min = 101
        class_max = -1

        for student in self.students:
            if student.score > class_max:
                class_max = student.score
            elif student.score < class_min:
                class_min = student.score

        return class_max - class_min
        



print("Welcome to Teacher's Pet!")
teacher_name = input("What is your name: ")
filename = input("Please enter the name of the file containing the students' information: ")

with open(filename, "r") as student_file:
    file_list = student_file.readlines()
    print("File opened.")

file_list.pop(0)
student_list = []

for student in file_list:
    student = student.strip()
    columns = student.split(",")
    student_list.append(Student(columns[0].strip('"'), float(columns[5].strip('"'))))

teacher = Teacher(teacher_name, student_list)

print("Welcome {}. Here are some options: ".format(teacher_name))
print("1. Calculate class average.")
print("2. Show class size")
print("3. Calculate class mark range.")

option = input("Please enter the number of your choice.")

if option == "1":
    print(teacher.class_average)
elif option == "2":
    print(teacher.class_size)
else:
    print(teacher.calculate_range())
    
    

        
