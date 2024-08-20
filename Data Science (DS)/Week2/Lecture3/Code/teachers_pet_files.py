with open("StudentsPerformance.csv", "r") as student_file:
    file_list = student_file.readlines()

file_list.pop(0)
student_gender = []
student_score = []

for student in file_list:
    student = student.strip()
    columns = student.split(",")
    student_gender.append(columns[0])
    student_score.append(columns[5])

print(student_gender)
print(student_score)