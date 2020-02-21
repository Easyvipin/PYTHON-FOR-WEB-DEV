#exception
try :
    fav_no = int(input(" Enter your fav no : "))
    print(fav_no)
except ValueError :
    print("invalid input ")

#finally
    #used to perform something even try raise an error or not
try :
    fav_no = int(input(" Enter your fav no : "))
    print(fav_no)
except ValueError :
    print("invalid input ")
finally :
    print("program finished")
#5
#program finished
    #finally basically used to clean up the resources in the program


#raise
#raise your own exception acc to your need and handle that  exception acc to your purpose
no = [1,3,4,6,-1,0,2]

for each in no :
    try:
        if each < 0 :
            raise ValueError
        else :
            print(each)
    
    except ValueError :
         print("no should not be less than 0")
        
