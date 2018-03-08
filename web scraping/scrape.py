
import requests
import pandas
import collections
from bs4 import BeautifulSoup
import datetime
import arsenal

# Take the required inputs

rankDate = input("Provide date: ")
rankRange = input("To get ATP rankings of all players possible, type range '1-5000'\nProvide range: ")

# Generate the desired URL depending on the inputs

if rankDate == "" and rankRange == "":
    url = arsenal.generateURL()
elif rankDate == "":
    url = arsenal.generateURL(arsenal.currentDate(), rankRange)
elif rankRange == "":
    url = arsenal.generateURL(rankDate)
else:
    url = arsenal.generateURL(rankDate, rankRange)
print(url)

r = requests.get(url)
c = r.content
soup = BeautifulSoup(c, "html.parser")

# Grabbing all the dates

date_list = []
all = soup.find("ul", {"data-value":"rankDate"}).find_all("li")
for each in all:
    date_list.append(each.text.replace("\t","").replace("\n","").replace("\r","").replace(".","-"))
# print(date_list)

if arsenal.isDateValid(rankDate, date_list) == False:
    print("No ATP rankings released on this date!")
else:
    # Grabbing all the column names
    print("Grabbing all the columns...")
    record = {}
    all = soup.find("table", {"class":"mega-table"})
    thead = all.find_all("div", {"class":"sorting-label"})
    for each in thead:
        record[each.text.replace("\t","").replace("\r","").replace("\n","")] = ""
    # print(record)

    # Grabbing all the player data as requested
    classes = ["rank-cell", "move-cell", "country-cell", "player-cell", "age-cell", "points-cell", "tourn-cell", "pts-cell", "next-cell"]
    tbody = all.find("tbody").find_all("tr")
    for r,c in zip(record, classes):
        print("Grabbing " + c + "...")
        temp = []
        for row in tbody:
            try:
                temp.append(row.find("td", {"class":c}).text.replace("\n","").replace("\r","").replace("\t",""))
            except:
                pass
        record[r] = temp

    # Grabbing country codes
    print("Grabbing country codes...")
    country = []
    all = soup.find_all("div", {"class":"country-item"})
    for each in all:
        img = each.find("img")
        country.append(img.get("alt"))
    record["Country"] = country
    # print(record)
    record = collections.OrderedDict(record)

    df = pandas.DataFrame(record)
    df.to_csv("ATP rankings.csv")
    print("Done :) Output data exported to ATP rankings.csv file")
