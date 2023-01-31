student_1 = {
    'first_name':"John", 'last_name':"Wick",
    'age':45
}
student_2 = {
    'first_name':"Jack", 'last_name':"Sparrow",
    'age':50
}
student_3 = {
    'first_name':"Mary", 'last_name':"Lee",
    'age':37
}
# - Class =  template or blueprint to create new objects
# - Objects = are instances of a class
#! Exmaple class: Human
# ! Objects : Putin Trump
class Student:
    # Constructor
    def __init__(self,fn,ln,a):
        # - Attributes -- Values
        self.first_name = fn
        self.last_name = ln
        self.age = a

    # Methods = what the class can do
    def increase_age(self):
        self.age +=1
        return self

    def print_info(self):
        print(f"Student fullname is {self.first_name} {self.last_name} and he is {self.age} old !")
        return self

john = Student("John","Wick",45)
# print(john.first_name, john.last_name, john.age)

# - Chaining methods

john.increase_age().increase_age().increase_age()
# print(john.first_name, john.last_name, john.age)
john.print_info().increase_age().print_info().increase_age().increase_age().print_info()