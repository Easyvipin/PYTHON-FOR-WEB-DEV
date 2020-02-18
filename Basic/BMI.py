#BMI PROGRAM
name = input("Enter your name") 
weight = int(input("Enter your weight"))
height = int(input("Enter your  Hieght"))
#BMI FORMULA
BMI = weight  /  (height ** 2)
print(BMI)
if BMI < 25 :
    print(name + "is not overweight")
else :
    print(name + "is overweight")
