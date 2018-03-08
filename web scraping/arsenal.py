import requests
import pandas
import collections
from bs4 import BeautifulSoup
import datetime

# rankDate in YYYY-MM-DD format
# rankRange in x-y format

# Grab the current date for which the latest rankings are released.
def currentDate():
    url = "http://www.atpworldtour.com/en/rankings/singles" # The default URL for ATP rankings
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    temp = soup.find("div", {"class":"dropdown-label"})
    temp = temp.text.replace("\t","").replace("\r","").replace("\n","").replace(".","-")
    return temp


# Generate the required URL depending on the date & range.
def generateURL(rankDate=currentDate(), rankRange="0-100"): # Use default values if no arguments are passed.
    url = "http://www.atpworldtour.com/en/rankings/singles?rankDate=%s&rankRange=%s" % (rankDate, rankRange)
    return url

# Check if the ATP rankings are released on this date.
def isDateValid(rankDate, date_list):
    if rankDate == "":  # Use default rankDate value (2018-03-05)
        return True
    if rankDate in date_list:
        return True
    else:
        return False
