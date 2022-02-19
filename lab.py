import requests
import sys

print("podaj date")
date=input()
url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

querystring = {"lat":"52.22","lon":"21.01"}
key=sys.argv[1]
headers = {
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
    'x-rapidapi-key': key
    }


with open("test.txt", "r") as file:
    if file.readline() == "":
        response = requests.request("GET", url, headers=headers, params=querystring)
        with open("test.txt", "w") as file:
            file.write(response.text)
            print("nadpis")
    else:
        with open("test.txt", "r") as file:
            response=file.readline()

data=response.json()
for i in range(len(data["data"])):
    if date in data["data"][i]["timestamp_local"]:
        if "snow" or "rain" in data["data"][i]["weather"]["description"]:
            print("bedzie padac")

        break