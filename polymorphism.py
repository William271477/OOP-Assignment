
class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

class Cat(Animal):
    def speak(self):
        print("The cat meows.")

# Polymorphism in action
def make_animal_speak(animal):
    animal.speak()

# Create instances
dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Outputs: The dog barks.
make_animal_speak(cat)  # Outputs: The cat meows.
