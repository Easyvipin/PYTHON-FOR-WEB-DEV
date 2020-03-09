#using beautiful soup to find the name of course provided by w3schools.com

import requests , bs4
response = requests.get('https://www.w3schools.com/')
response.raise_for_status()
w3school = bs4.BeautifulSoup(response.text,features="html.parser")
reslist = w3school.select('.w3-container h4')
print(len(reslist))
for item in reslist :
    print(item.getText())
#8
#HTML and CSS
#JavaScript
#Server Side
#Programming
#Web Building
#XML Tutorials
#References
#Exercises
