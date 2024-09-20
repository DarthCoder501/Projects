import requests

api_key = "889148d3ef4b204583816c60dfceb4ac"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter City Name: ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
x = response.json()

if x["cod"] == "404":
  print("City Not Found")
  exit()
else:
  y = x["main"]
  temp = y["temp"] - 273.15
  tempF = (temp * 9 / 5) + 32
  print("Temperature:", round(tempF, 2))
