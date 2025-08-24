import requests

api_key="182e33a88033d08bab31334d5899e901"
lat=1.29
lon=36.82
url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response=requests.get(url)
# print(response.json())

data=response.json()

# cordinates=data['coord']
# print(cordinates)
# print("longitudes: ",cordinates['lon'])
# print("latitude: ",cordinates['lat'])
# print("Name: ",data['name'])
print(data["main"])