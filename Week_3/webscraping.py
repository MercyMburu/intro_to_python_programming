# import requests

# url="https://quotes.toscrape.com/"
# response=requests.get(url)
# # print(response)

# url="https://quotes.toscrape.com/"
# response=requests.get(url)
# status=response.status_code
# print(response.status_code)

import requests
from bs4 import BeautifulSoup

url="https://quotes.toscrape.com/"
response=requests.get(url)
print(response)

if response.status_code==200:
    print('successful')
else:
    print("error: {response.status_code}")
    
# soup=BeautifulSoup(response.text,"html.parser")
# one=soup.find("div",class_="quote")
# print(one)

soup=BeautifulSoup(response.text,"html.parser")
# one=soup.find("div",class_="tags")
# print(one.text)

one=soup.find("div",class_="tags")

    
links=one.find_all("a",class_="tags")
# for link in links:
#     print(link.text)
    # print(link['href'])
    
# quotes=soup.find_all("span",class_="text")
# for quote in quotes:
#     print(quote.text)
    
authors=soup.find_all("small",class_="author")
for author in authors:
    print(author.text)