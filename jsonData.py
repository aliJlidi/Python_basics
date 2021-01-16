# working with data in json format 
import urllib.request
import json

def printResult(data):
    #use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    #access content
    if("title" in theJSON["metadata"]):
        print(theJSON["metadata"]["title"])

    #the number of events
    count = theJSON["metadata"]["count"]
    print(str(count) + " Events recorded")
    #for each event, print the place 
    for i in theJSON["features"]:
        print(i["properties"]["place"])







def main():
    #define a variable to hold the source URL
    #In this case we'll use the free data from a site
    #the last day data about earthquakes of 2.5 or more
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    #open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: "+ str(webUrl.getcode()))
    if(webUrl.getcode()==200):
        data = webUrl.read()
        printResult(data)
    else:
        print("Recieved error, cannot parse results")


if(__name__=="__main__"):
    main()