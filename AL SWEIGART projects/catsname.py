# Name your cats
cats = [ ]
while True :
    print(f"Enter your {str(len(cats) + 1 )} cat Name or enter nothing to stop")
    name = input ("Name here :  ")
    if name == "" :
        break
    cats.append(name)


print(cats)
#output
#Enter your 1 cat Name or enter nothing to stop
#Name here :  sweet
#Enter your 2 cat Name or enter nothing to stop
#Name here :  love
#Enter your 3 cat Name or enter nothing to stop
#Name here :  
['sweet', 'love']

#alternative method by not using a append() method
#cats= cats + [name]
#this will also work the same
