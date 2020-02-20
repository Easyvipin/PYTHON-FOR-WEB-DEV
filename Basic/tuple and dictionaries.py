#tupple
 #similar like lists but they cannot be mutable
number = (1, 2 , 3 )
#number[0]=3
print(number)
#error 'tuple' object does not support item assignment
#mailny used tuple in a situation where the data is permanent

#UNPACKING in tuple and lists
#similar to destructuring concept in javascript
x,y,z = number 
print (x,y,z)
#ERROR too many values to unpack (expected 3)
#unpack variable should be equal to no elements in tuple
even = [2 , 4 , 6 ]
v,i,p=even
print(v,i,p)

#DICTONARIES
#key value pairs
person = {
    "name" : "vipin" ,
    "lname" : "chandra",
    "city" : "ASR"
    }
#ACESSING
print(person["name"]) #vipin

#update
person["city"] = "jrc"
print(person)

#keys are CASE SENSITIVE
#print(person["NAME"]) #KEYerror
#important : no similar keys can be used in DIC

#get method
#dic_variable.get(key,defaultvalue)
last=person.get("mname","sharma")
print(last)

#program of numerical to words
words = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4": "four"
    }
user_input= input("Enter the No :  ")
output = ""
for each in user_input :
    output += words.get(each)
print(output)
