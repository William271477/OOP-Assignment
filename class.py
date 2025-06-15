# activity1_class.py

class Student:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, my student ID is {self.student_id}, and I am studying {self.course}.")


student1 = Student("William Ndhlovu", "20250123", "Computer Science")
student1.introduce()
