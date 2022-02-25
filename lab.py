import requests
import sys
url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

querystring = {"lat":"52.22","lon":"21.01"}
key=sys.argv[1]
headers = {
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
    'x-rapidapi-key': key
    }

class Weather:
    def __init__(self):
        self.test=""
        self.baza=[]
        self.lines=0


    def list(self):
        base=self.baza

        with open("logi.txt", "r") as file:
            for line in file:

                line=line.strip()
                if line == "\n":
                    continue
                print(line)
                base.append(line)
            print(base)
        return base
    def check(self, date):
        baza=self.list()
        for i in range(len(baza)):
            if baza[i] == date:
               return True



    def check2(self, response):
        with open("test.txt", "r") as file:
            self.test = file.readline()
        if self.test!=response:
            with open("test.txt", "w") as file:
                file.write(response.text)
            return False
    def action(self, response, date):
        data=response.json()
        for i in range(len(data["data"])):
            if date in data["data"][i]["timestamp_local"]:
                if "snow" or "rain" in data["data"][i]["weather"]["description"]:
                    with open("logi.txt", "a") as fp:
                        self.baza.append(date)
                        for i in range(len(self.baza)):
                            fp.write(self.baza[i])
                            fp.write("\n")

                    print("bedzie padac")

                break
print("podaj date")
date=str(input())
sc=Weather()
baza=sc.list
print(date, "c1")
if sc.check(date):
    print("wczytane")
    print("bedzie padac")
    quit()

else:
    response = requests.request("GET", url, headers=headers, params=querystring)
    sc.check2(response)
    sc.action(response, date)










