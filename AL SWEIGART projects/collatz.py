#Write a function named collatz() that has one parameter named number. If
#number is even, then collatz() should print number // 2 and return this value.
#If number is odd, then collatz() should print and return 3 * number + 1.
#Then write a program that lets the user type in an integer and that keeps
#calling collatz() on that number until the function returns the value 1. 

def collatz(number) :
    value = 0 
    if number % 2 == 0 :
        print(number // 2)
        value = number // 2 
    elif number % 2 == 1 :
        print (3 * number + 1)
        value = 3 * number + 1
    else :
        print ("Enter the no greator than 0")
    return value


No = int(input("Enter the number"))
while No  != 1 :
    if No == 0 :
        print("enter the no greator than 0")
        break
    print(No)
    No = collatz(No)

#output

#Enter the number5
#5
#16
#16
#8
#8
#4
#4
#2
#2
