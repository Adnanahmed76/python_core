class student:
    # methods and annotation annotation is used to share information about the function and its parameters
    def __init__(self,name:str,age:int,gender:str):
        self.name=name
        self.age=age
        self.gender=gender

    # methods
    def display(self)->None:
        print(f"My name Is {self.name}, age is {self.age} and gender is {self.gender}")
        print("this is the diplay functions")

    def get_age(self)-> int:
        return self.age



s1=student("Alam",30,"Male")
print(s1.get_age())
s1.display()
# s1.set_info("Adam",20,"male")
# s1.display()
