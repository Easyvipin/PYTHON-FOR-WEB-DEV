
#GUESS GAME
print("WELCOME TO GUESS GAME ")
print("3 chance to go")
secret_no=5
chances=0
no=0
while no != secret_no and chances < 3 :
    no = int(input("Guess the no:   " ))
    chances+= 1
    if  no == secret_no :
        print(f" {no} is the right guess ")
        print("""
               you won the GAME!!!
""")
        break
    else :
        print( "Wrong guess")
else :
    print("out of chances")
        
