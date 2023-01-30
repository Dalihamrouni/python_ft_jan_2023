"""
for (var i =0; i < 11; i++){
    console.log(i)
}
"""

# for i in range(0,10+1, 2):
#     print(i)
# for i in range(100,0,-10):
#     print(i)

superheros = ["superman", "batman", "thor", "wonder woman", "walidman"]

"""
for( var i=0;i< superheors.length;i++){
    console.log(superhores[i])
}
"""
# for hero in superheros:
#     print(f"Using list iterator = {hero}")

# for i in range(len(superheros)):
#     print(f"Using range function = {superheros[i]}")

# for y in superheros[2]:
#     if y == "e":
#         print("This is e")
#     else:
#         print("Not Found")
# print("Not Found")

student_dict = {'name': "Tom", 'age':45,'class':"python", 
'marks':[9.2,9.5,10],'is_admin':False,
 'is_happy':True}


# for key in student_dict:
#     print("Key Only ",key )

# for val in student_dict.values():
#     print("Value Only",val)
# for key, value in student_dict.items():
#     print(value," --> ",key)

my_list = [hero for hero in superheros if len(hero)> 4]
# print(my_list)

# While Loop
x = 5 
while x > 0:
    print("Hello")
    x -= 1