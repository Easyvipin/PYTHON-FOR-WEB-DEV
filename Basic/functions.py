#funtions

#syntax
#def function_name( ) :

def greet_user () :
    print("Hello user")
    print("Welcome to this program")

greet_user()

#Hello user
#Welcome to this program

#parameter

def full_name(fname,lname) :
    print(f' my First name is {fname }')
    print(f' last name is {lname} ' )

full_name("vipin","chandra")

# my First name is vipin
 # last name is chandra
 # IMPORTANT parameter should be in orderd and no of paramter should be equal to arguements

 #return
 # As default a function in python return "NONE"
 
print(full_name("vipin","chandra"))
# my First name is vipin
 # last name is chandra
#none


def full_name1 (fname,lname) :
    return fname + " " + lname

name= full_name1 ("vipin","chandra")
print(name)
