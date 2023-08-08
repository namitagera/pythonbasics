
class Robot_dog:
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val

    def bark(self):
        print("Woof")

# main program 
my_dog = Robot_dog("Spot", "Pug")
print(my_dog.name)
print(my_dog.breed)

my_dog.bark()        