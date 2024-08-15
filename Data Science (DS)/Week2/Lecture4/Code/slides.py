class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark
        self.studying = False

    def study(self):
        self.studying = True
        print("{} is studying. Please do not disturb."
              .format(self.name))

student1 = Student("Zahra", 24, 89)
student1.study()


class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def calculate_average (cls, num_list):
        num_sum = sum(num_list)
        n = len(num_list)
        return (num_sum/n)

result = MathUtils.calculate_average([89, 23, 43, 60, 9, 10])
print(result)

result = MathUtils.add(5, 7)
print(result)

