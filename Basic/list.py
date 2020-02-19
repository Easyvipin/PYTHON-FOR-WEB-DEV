#lists
#find a largest no in the list
no = [98,41,67,-123,100,41,56,78,54]
max_no = no[0]
for item in no :
    if max_no <= item :
        max_no =  item
    else :
        max_no = max_no
print(max_no)
#100


#2dlists
#2d lists extermely powerful and they have great use in Ai and machine learning.
matrix = [
    [ 2, 4, 6],
    [ 2, 3, 4],
    [ 6,7 , 8]
    ]
print(matrix)
# acessing inner elements
#list [ ] [ ] ---> syntax
print(matrix [ 0 ] [ 2 ] ) #6
print (matrix [ 0 ] , [ 2 ]) #[2, 4, 6] [2]
print ( matrix [ 0 ] [ : ]) #[2, 4, 6]
print( matrix [ : ] ) #[[2, 4, 6], [2, 3, 4], [6, 7, 8]]
print ( matrix [ : ] [ 1 ]) #[2, 3, 4]

#list methods
#to remove duplicates in the list
names = [ "vipin" , "john","mason" , "mohit", "john", "mason"]
unique=[ ]
for name in names :
    if name not in unique :
        unique.append(name)
        #append method add the element in the list from end
print(unique)
#['vipin', 'john', 'mason', 'mohit']

#insert method
#list.insert(index,value)
names.insert(2,"arvind")
print(names)
#It will no override the element instead it will move the index one step ahead of all the element
#['vipin', 'john', 'arvind', 'mason', 'mohit', 'john', 'mason']



#remove method
#list.remove(listitem)
names.remove("mason")
print(names)
# [ "vipin" , "john","arvind" , "mohit", "john", "mason"]

#pop method
#list.pop()
#it delete the no from end

#sort method for ascend sort
#reverse method for descend sort
marks=[34,56,21,67,43,27,89,56,90,29]
print(marks.sort())
#none
#output will be none because it make a change to the list only
print(marks)
#[21, 27, 29, 34, 43, 56, 56, 67, 89, 90]

#copy method
#this can be used to manipulate the important data by copying it.
copied_no=marks
print(copied_no)
[21, 27, 29, 34, 43, 56, 56, 67, 89, 90]

