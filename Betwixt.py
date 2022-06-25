#
# countryLocs = {"england": 0, "italy": 1000, "libya": 2000}
#
# class England:
#     def __init__(self, location):
#         self.location = countryLocs["england"]
# class Italy:
#     def __init__(self, location):
#         self.location = countryLocs["italy"]
# class Libya:
#     def __init__(self, location):
#         self.location = countryLocs["libya"]
#
# def average(country1loc, country2loc):
#     result = (country1loc + country2loc) / 2
#     return result
#
# print(str(average(countryLocs["england"], countryLocs["libya"])))
#
# if average(countryLocs["england"], countryLocs["libya"]) == countryLocs["italy"]:
#     print("nice")

import pandas as pd
import random
from math import radians, cos, sin, asin, sqrt
data = pd.read_csv (r'concapEdited.csv')
df = pd.DataFrame(data, columns= ['CountryName','CapitalLatitude', 'CapitalLongitude'])
# print (df)

countryName = []
countryLat = {}
countryLon = {}

for row in range(206):
    countryName.append(df.iloc[row, 0])
for row in range(206):
    countryLat[f"{df.iloc[row, 0]}"] = round(df.iloc[row, 1], 4)
for row in range(206):
    countryLon[f"{df.iloc[row, 0]}"] = round(df.iloc[row, 2], 4)

# country = countryName[0]
# print(countryName[0])
# print(str(countryLat[f"{country}"]), end=", ")
# print(str(countryLon[f"{country}"]))

country1 = random.choice(countryName)
country2 = random.choice(countryName)

country1Lat = countryLat[country1]
country1Lon = countryLon[country1]

country2Lat = countryLat[country2]
country2Lon = countryLon[country2]

print(country1)
print(str(country1Lat), end=", ")
print(str(country1Lon), end="\n\n")

print(country2)
print(str(country2Lat), end=", ")
print(str(country2Lon))

country1LatRad = country1Lat / 57.29577951
country2LatRad = country2Lat / 57.29577951

country1LonRad = country1Lon / 57.29577951
country2LonRad = country2Lon / 57.29577951

dlat = country2LatRad - country1LatRad
dlon = country2LonRad - country1LonRad

a = sin(dlat / 2)**2 + cos(country1LatRad) * cos(country2LatRad) * sin(dlon / 2)**2
c = 2 * asin(sqrt(a))
r = 6378
distance = c*r
print(str(distance))

#
# countryLat = {"England": 51.5, "Italy": 41.9}
# countryLon = {"England": 0.1, "Italy": 12.5}
#
# englandLat = countryLat["England"] / 57.29577951
# englandLon = countryLon["England"] / 57.29577951
#
# italyLat = countryLat["Italy"] / 57.29577951
# italyLon = countryLon["Italy"] / 57.29577951
#
# dlon = italyLon - englandLon
# dlat = italyLat - englandLat
# a = sin(dlat / 2)**2 + cos(englandLat) * cos(italyLat) * sin(dlon / 2)**2
#
# c = 2 * asin(sqrt(a))
#
# r = 6371
#
# Distance = c*r
#
# print(str(Distance))
