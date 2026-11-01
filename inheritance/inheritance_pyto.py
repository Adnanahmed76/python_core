class Animal:

    def __init__(self,name:str,type:str):
        self.name=name
        self.type=type

    def eat(self):
        print("i am eating")
    def sleep(self):
        print("i am sleeping")

class Dog(Animal):
    def bark(self):
        print("i am barking")

dog=Dog("Buddy","Domestic")
dog.eat()
dog.sleep()
dog.bark()

