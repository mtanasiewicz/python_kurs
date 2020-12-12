class Student:
    students_list = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.students_list.append(self)

    @classmethod
    def students_count(cls):
        print(len(Student.students_list))


student_1 = Student('Marian', 15)
student_2 = Student('Michał', 18)

Student.students_count()
