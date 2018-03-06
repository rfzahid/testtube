# rankDate in YYYY-MM-DD format
# rankRange in x-y format

# Generate the required URL depending on the date & range.
def generateURL(rankDate, rankRange):
    url = "http://www.atpworldtour.com/en/rankings/singles?rankDate=%s&rankRange=%s" % (rankDate, rankRange)
    return url

# Check if the ATP rankings are released on this date.
def isDateValid(rankDate, date_list):
    if rankDate in date_list:
        return True
    else:
        return False
