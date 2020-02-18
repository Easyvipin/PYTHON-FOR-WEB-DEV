#simulation game
#instructions
print("Type START to start the game >>>>")
print("Type STOP to stop the game >>>>")
print("Type QUIT to quit the game >>>>")
print("type HELP to know >>>>")
status=""
command=""
while command != "QUIT" :
    command=input("COMMAND: ").upper();
    if command == "START":
        if status == "START" :
            print ("GAME ALREADY STARTED")
        else :
            status=command
            print("GAME STARTED")
    elif command == "STOP" :
        if status == "STOP" :
            print("Game stopped")
        else :
            status=command
            print("GAME STOPPED")
    else :
        print("Type START to start the game >>>>")
        print("Type STOP to stop the game >>>>")
        print("Type QUIT to quit the game >>>>")
else :
     print("QUIT THE GAME")
