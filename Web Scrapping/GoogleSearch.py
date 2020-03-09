#im feeling lucky GOOGLE
import sys
from bs4 import BeautifulSoup
import requests
import webbrowser

 

#lets make it magical
search = ' '.join(sys.argv[1:])
response = requests.get(f"https://www.google.com/search?q={search}")
response.raise_for_status()
resobject = BeautifulSoup(response.text,"html.parser")

reslist = resobject.select(' .kCrYT >  a ')
for item in reslist[:5] :
    webbrowser.open("https://google.com/" + item.get('href'))
    
