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
    
with open("StudentsPerformance.csv", "r") as student_file:
    file_list = student_file.readlines()

file_list.pop(0)
student_list = []

for student in file_list:
    student = student.strip()
    columns = student.split(",")
    student_list.append(Student(columns[0].strip('"'), float(columns[5].strip('"'))))

teacher = Teacher("Ms Mohamed", student_list)
print(teacher.class_average)
print(teacher.class_size)
    
    

        
