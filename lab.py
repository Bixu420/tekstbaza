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
        self.baza={}
        self.lines=0


    def list(self):
        base=self.baza

        with open("logi.txt", "r") as file:
            for line in file:

                line=file.readline().strip()
                line1=file.readline().strip()
                if line == "\n":
                    continue
                print(line)
                base[line]=line1
            print(base)
        return base
    def check(self, date, base):
        baza=[]
        if date in base.keys():
            baza = [date, base[date]]
            return baza
        else:
            return False






    def check2(self, response):
        with open("test.txt", "r") as file:
            self.test = file.readline()
        if self.test!=response:
            with open("test.txt", "w") as file:
                file.write(response.text)
            return False
    def action(self, response, date, base):
        data=response.json()
        for i in range(len(data["data"])):
            ciag=data["data"][i]["weather"]["description"]
            if date in data["data"][i]["timestamp_local"]:
                if "snow" in ciag or "rain" in ciag:

                    with open("logi.txt", "a") as fp:
                        base[date]="bedzie padac"
                        fp.write("\n")
                        fp.write(date)
                        fp.write("\n")
                        fp.write("bedzie padac")

                    print("bedzie padac")
                    print(base)
                    break
                else:
                    with open("logi.txt", "a") as fp:
                        base[date]="nie bedzie padac"
                        fp.write("\n")
                        fp.write(date)
                        fp.write("\n")
                        fp.write("nie bedzie padac")
                    print("nie bedzie padac")
                    print(base)

                    break
        return base
    def items(self,lol):

        return lol.items()
    def items2(self, base):
        return base.items()


print("podaj date")
date=str(input())
sc=Weather()
base=sc.list()
print(date, "c1")
check=sc.check(date, base)
if check is False:
    response = requests.request("GET", url, headers=headers, params=querystring)
    sc.check2(response)
    lol=sc.action(response, date, base)
    for x, y in sc.items(lol):
        print(x, y)

else:
    print(check[0], check[1])
    for x, y in sc.items2(base):
        print(x, y)
















