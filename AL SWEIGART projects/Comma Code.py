#Comma Code
spam = ['apples', 'bananas', 'tofu', 'cats']
def  sentence ( spam ) :
    for i in range(len(spam)) :
        if i == len(spam) - 1:
            print(f" and {spam[i]}")
        else :
            print(f" {spam[i]} " , end = '')
sentence(spam)
 #output       
 #apples  bananas  tofu  and cats
