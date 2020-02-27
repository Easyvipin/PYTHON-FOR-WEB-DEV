#mypet
pet = ["tom" , "rocky" , "dony" , "sky"]
def GuessPet () :
    name = input ("Guess my pet Name :  ")
    if name not in pet :
        print("No you're wrong !!! ")
        GuessPet()
    else :
        print(f"Yeah you're right {name} is one of  my pet name")
        

GuessPet()
