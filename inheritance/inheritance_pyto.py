class Animal:

    def __init__(self,name:str,type:str,age:int):
        self.name=name
        self.type=type
        self.age=age


    def eat(self):
        print("i am eating")
    def sleep(self):
        print("i am sleeping")

        

class Dog(Animal):

    def __init__(self,name:str,type:str,age:int,bread:str):
        super().__init__(name,type,age)
        self.breed=bread
     

    def bark(self):
        print("i am barking")

    def display(self):
        print(f"Name: {self.name}, type: {self.type}, age: {self.age}, breed: {self.breed}")

dog=Dog("Buddy","Domestic",5,"Golden Retriever")
dog.eat()
dog.sleep()
dog.bark()
dog.display()


