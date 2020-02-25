#class
class Person :
    def __init__ (self,name) :
        self.name=name
    def talk (self) :
        print(f" {self.name} is talking")

person_name = input("Enter your Name  :  ")
command = input("Type TALK to start talking ")
if command.upper()  == "TALK" :
    print("Started")
    person1 = Person(person_name)
    person1.talk()
else :
    print ("invalid command" )

    
        
