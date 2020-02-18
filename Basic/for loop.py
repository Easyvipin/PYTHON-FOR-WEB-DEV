#TOTAL COST
cost = [100,200,400,300,10]
total=0
for each in cost :
    total += each
print(total)
#1010

 #using of range
for item in range (2,10,2) :
    print(item)  
#2 4 6 8

#axis from one corndinate to another cordinate
# (x,y)=(0,0) to (x,y)=(4,4)
#nested loops
x=4
y=4
for xaxis in range(0,x+1) :
    for yaxis in range(0,y+1):
        print(f" ( { xaxis }, {yaxis}) ")
#(0,0) -----> (4,4)      
