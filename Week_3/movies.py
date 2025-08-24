import requests
from bs4 import BeautifulSoup

url="https://www.netflix.com/tudum/top10"
response=requests.get(url)

if response.status_code==200:
    print("Execution Successful")
else:
    print("Error",{response.status_code})
    
soup=BeautifulSoup(response.text,"html.parser")

items=soup.find_all("th")
print(items)
for i in items:
    print(i.text.strip())
    


