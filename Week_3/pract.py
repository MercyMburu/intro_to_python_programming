import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/List_of_banks_in_Kenya"
response=requests.get(url)

if response.status_code==200:
    print("Success!")
else:
    print("Error,{response.status_code}")
    
soup=BeautifulSoup(response.text,"html.parser")
# print(soup)
item=soup.find("div",class_="mw-content-ltr mw-parser-output")
# print(item)
banks=item.find("ul")
# print(banks)

links=banks.find_all("li")

for link in links:
    print(link.text)
    try:
        names=link.find("a")
        print(names["href"])
    except TypeError:
        print("No link found!,Skip!!!")
        
    




