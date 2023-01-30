# function : squence of instuctions
#  could take parametres
#!  all Function Always RETURN SOMTHING even it's NONE

"""
function sayHi(name){
    console.log(`Hi ${name}`)
}
"""
def say_hi(name):
    return(f"Hi {name}")
    print(f"Hi {name}")
    

# !Invoke the function

# say_hi("Alex")

def multiply(*args):  #- a and b are parameters
    print(args)
    a = 1
    for i in args:
        a = a*i
    print(a)
    return(a)
# multiply(5,9) #- 9 and 5 arguments 

# multiply(9,5,8,8,9,41,3,5,33,1,6,3,41,3,5,33,41,3,5,33,41,3,5,33)

def say_my_fullname(**kwargs):
    print(f" Your fullname is {kwargs['first_name']} {kwargs['last_name']}")
    # print(kwargs)
    # return f" Your fullname is {first_name} {last_name}"

say_my_fullname(last_name="Trump", first_name="Donald")
