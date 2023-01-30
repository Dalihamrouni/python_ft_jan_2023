# This is a comment  = will not be interpreted 

"""
MultiLine
 comment
"""
# ! Variables

# var student_name  = "Steve"
student_name = "Steve"

GLOBAL_VAR = "Hello"

#  numbers :

# age  = 39  #- Integer
rate = 3.14 #-Float

# print(student_name)
# print("My name is " + student_name  "my age is" +  age)

# print(f"My name is {student_name} my age is {age}")
# print(f"The Student name {student_name} and rate = {rate}")

#  Boolean
vote = True
is_admin = False
is_valid = None
# print(type(is_valid))
# * Composite
# - Lists  == Arrays in JS

#         0 1 2 3 4  
my_list = [10,-2,3,40,5]
names = ["alex", "sam", student_name]
# print(my_list[0])
# print(names[2])
my_list[0]= 100
# print(my_list[0])

names.append("Sarah")
# print(names)
# my_list.pop(3)
# print(my_list)

# print(len(my_list))
second_list = ["Tom", 28, True, 2.5,[77,9,False]]
# print(second_list)
my_list.sort()
# print(my_list)
# if age>18 :
#     print("Welcome To the Club")

#- Dictionaries == Objects in JS

student_dict = {'name': "Tom", 'age':45,'class':"python", 
'marks':[9.2,9.5,10],'is_admin':False,
 'is_happy':True}

# print(student_dict['marks'][1])

student_dict['city'] = "California"
# print(student_dict)

del student_dict['age']

# print(student_dict)

# - Tuples
# lists immutables ? cannot be changed 
tup = (1,2,3)
# print(tup)
# print(tup[1])
#! tup[0] = 100
tup2 = (2, True, names, student_dict)
# print(tup2)
student_dict['tuple'] = tup
# print(student_dict)
# age  = 18
# if age>18 :
#     print("Welcome To the Club")
# elif age<18 :
#     print("Hello")
# else :
#     print("😂😂")

if not student_dict['is_admin']:
    print("You are not Authorized")


if not student_dict['name'] == "Tom":
    print(f"Hello {student_dict['name']}")
else :
    print("Who are you ?")
