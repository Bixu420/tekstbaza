import requests
import sys
import datetime
from datetime import date

today = datetime.date.today()


url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"

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
    def check(self, date1, base):
        baza=[]
        if date1 in base.keys():
            baza = [date1, base[date1]]
            return baza
        else:
            return False
    def check3(self, date1, today):
        date1=date1.split("-")
        year=int(date1[0])
        month=int(date1[1])
        today1=int(date1[2])
        d0=date(year, month, today1)
        delta=d0-today
        if delta.days>16:
            return False
        return True









    def check2(self, response):
        with open("test.txt", "r") as file:
            self.test = file.readline()
        if self.test!=response:
            with open("test.txt", "w") as file:
                file.write(response.text)
            return False
    def action(self, response, date1, base):
        data=response.json()

        for i in range(len(data["data"])):
            ciag=data["data"][i]["weather"]["description"]
            if date1 in data["data"][i]["timestamp_local"]:
                if "snow" in ciag or "rain" in ciag:

                    with open("logi.txt", "a") as fp:
                        base[date1]="bedzie padac"
                        fp.write("\n")
                        fp.write(date1)
                        fp.write("\n")
                        fp.write("bedzie padac")

                    print("bedzie padac")
                    print(base)
                    break
                else:
                    with open("logi.txt", "a") as fp:
                        base[date1]="nie bedzie padac"
                        fp.write("\n")
                        fp.write(date1)
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

print("podaj date1")
if len(sys.argv)==3:
    date1=sys.argv[2]
else:

    date1 = str(today + datetime.timedelta(days=1))

sc=Weather()
base=sc.list()
print(date1, "c1")
if sc.check3(date1, today) is False:
    print("nie wiem")
    quit()
check=sc.check(date1, base)
if check is False:
    response = requests.request("GET", url, headers=headers, params=querystring)
    sc.check2(response)
    lol=sc.action(response, date1, base)
    for x, y in sc.items(lol):
        print(x, y)

else:
    print(check[0], check[1])
    for x, y in sc.items2(base):
        print(x, y)
















