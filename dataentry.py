import pandas as pd
from geopy.geocoders import Nominatim

import http

geolocator = Nominatim(user_agent="bettermart")

data = pd.read_excel('filteredData1.xlsx')
#
latitude = list(data["latitude"])
date = list(data["date"])
longitude = list(data["longitude"])
#
# res = {i: {"date": date[i], "latitude": latitude[i], "longitude": longitude[i]} for i in range(len(latitude))}
#
# print(res)

"A9SCBHEF4SHU75SWVQJDV8RST&contentType=json"
print("started")
pincodes=list(range(len(latitude)))
for i in range(len(latitude)):
    pincodes[i] = (geolocator.reverse(f"{latitude[i]},{longitude[i]}")).raw["address"]["postcode"]
    print(f"{i}:  {latitude[i]},{longitude[i]}: {pincodes[i]}")
# pincodes = [(geolocator.reverse(f"{latitude[i]},{longitude[i]}")).raw["address"]["postcode"] for i in
#             range(len(latitude))]
print(pincodes)
print("ended")
data["pincode"] = pincodes
