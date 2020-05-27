import csv
import json
import urllib.request

handle = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson")
data = handle.read()
eData = json.loads(data)

def makeDataList(dataName):
    with open("sig_week.csv", 'r') as inFile:
        dataList = []

        csvReader = csv.reader(inFile)
        titles = next(csvReader)

        colNum = 0
        while colNum < len(titles) and titles[colNum] != dataName:
            colNum = colNum + 1

        if colNum == len(titles):
            print("Error:", dataName, "not found.")
        else:
            for line in csvReader:
                dataList.append(float(line[colNum]))
    return dataList


def makeMagList(earthquakeData):

    magList = []

    earthquakes = earthquakeData.get('features')

    for i in range(len(earthquakes)):
        earthquake = earthquakes[i]
        properties = earthquake.get('properties')
        mag = properties.get('mag')
        magList.append(mag)
    return magList

def places(earthquakeData):

    placeList = []

    earthquakes = earthquakeData.get('features')

    for i in range(len(earthquakes)):
        earthquake = earthquakes[i]
        properties = earthquake.get('properties')
        place = properties.get('place')
        magList.append(place)
    return placeList

def filewriter():
       earthquakes = earthquakeData.get('features')
       with open("eq.csv", 'w') as outFile:
             for i in range(len(earthquakes)):
                 earthquake = earthquakes[i]
                 properties = earthquake.get('properties')
                 place = properties.get('place')
                 mag = properties.get('mag')
                 txtreport=outFile.write("A" + str(mag) + "magnitude earthquake recorded" + place + "\n")