#beautiful soap

import requests, bs4
res=requests.get('https://www.lipsum.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,features="html.parser")
elems = noStarchSoup.select('.de')

#pass the string containing the html tags
#this BeautifulSoap function returns an object
#this is the element i was looking for
#<a class="de" href="http://de.lipsum.com/">Deutsch</a>
print(elems) #[<a class="de" href="http://de.lipsum.com/">Deutsch</a>] >>list recieved
print(type(elems)) #<class 'bs4.element.ResultSet'>
print(len(elems)) # 1 cause only one tag belong to the class ".de"
print(elems[0].getText()) #  Deutsch >>> getText() can be used to retrieve the innerHtml or innertext
print(str(elems[0])) #<a class="de" href="http://de.lipsum.com/">Deutsch</a>
print(elems[0].attrs) # {'class': ['de'], 'href': 'http://de.lipsum.com/'} 

