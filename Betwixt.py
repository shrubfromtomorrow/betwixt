import pandas as pd
import random
from math import radians, cos, sin, asin, sqrt
data = pd.read_csv (r'concapEdited.csv')
df = pd.DataFrame(data, columns= ['CountryName','CapitalLatitude', 'CapitalLongitude'])

countryName = []
countryLatLon = {}
countryLat = {}
countryLon = {}
countryClose = {}
closestDis = []

for row in range(206):
    countryName.append(df.iloc[row, 0])
    countryLon[f"{df.iloc[row, 0]}"] = round(df.iloc[row, 2], 4)
    countryLat[f"{df.iloc[row, 0]}"] = round(df.iloc[row, 1], 4)
    countryLatLon[f"{df.iloc[row, 0]}"] = [round(df.iloc[row, 1], 4), round(df.iloc[row, 2], 4)]

################################################################################################

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
print(str(country2Lon), end="\n\n")

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
print(f"Distance Betwixt(tm): {str(distance)}", end="\n\n")

################################################################################################

middleLat = round((country1Lat + country2Lat) / 2, 4)
middleLon = round((country1Lon + country2Lon) / 2, 4)

middleLatRad = middleLat / 57.29577951
middleLonRad = middleLon / 57.29577951

for country in countryLatLon:
    countryLatRad = countryLatLon[country][0] / 57.29577951
    countryLonRad = countryLatLon[country][1] / 57.29577951
    difLat = middleLatRad - countryLatRad
    difLon = middleLonRad - countryLonRad
    A = sin(difLat / 2)**2 + cos(middleLatRad) * cos(countryLatRad) * sin(difLon / 2)**2
    C = 2 * asin(sqrt(A))
    R = 6378
    dis = C*R
    countryClose[dis] = country
    closestDis.append(dis)
# minLat = min(countryLats, key=lambda x:abs(x-middleLat))
# minLon = min(countryLons, key=lambda x:abs(x-middleLon))

sorted = sorted(closestDis, key=abs)


print(f"Middle: {str(middleLat)}", end=", ")
print(str(middleLon), end="\n\n")

print(countryClose[sorted[0]])
print(f"{countryLatLon[countryClose[sorted[0]]][0]}, {countryLatLon[countryClose[sorted[0]]][1]}")
