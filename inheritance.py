class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

# Child class inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        # Overrides the parent method
        print(f"My name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}.")

# Create an instance
student = Student("William", 20, "20250123")
student.introduce()
