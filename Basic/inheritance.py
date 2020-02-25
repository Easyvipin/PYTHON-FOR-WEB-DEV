#inheritance

class person :
    def  __init__(self,fname,lname) :
        self.fname=fname
        self.lname=lname
    def introduction (self) :
        print (f"my name is {self.fname ,  self.lname} ")


class student(person) :
    def __init__(self,fname,lname,class_no) :
        super().__init__(self,fname,lname)
        self.class_no=class_no
    def about (self) :
        print(f"{self.fname} study in {self.class_no} th class")

person1 = student("vipin","chandra","8")
person1.introduction()
person1.about()
