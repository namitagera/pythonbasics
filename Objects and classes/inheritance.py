class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print("My name is", self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print("New position", self.position)

    def eat(self):
        print("I'm hungry")

class Robot_dog(Robot):

    def noise(self):
        print("Woof")
    
    def eat(self):
        super().eat()
        print("I like fruit")
    

# Main program

my_robot_dog = Robot_dog("Bud")
my_robot_dog.walk(10)
my_robot_dog.noise()
my_robot_dog.eat()
