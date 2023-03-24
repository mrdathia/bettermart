# import pandas as pd
# import pymongo as pymongo
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_absolute_error
#
# # Step 1: Collect data
# data = pd.read_xlsx('filteredData.xlsx')
#
# # Step 2: Data preparation
# # Remove duplicates, handle missing values, and convert categorical variables into numerical ones.
#
#
# # Step 3: Feature engineering
# # Create new features based on historical prices, weather data, and other external factors.
#
#
# # Step 4: Model selection
# model = RandomForestRegressor()
#
# # Step 5: Model training
# X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# model.fit(X_train, y_train)
#
# # Step 6: Model evaluation
# y_pred = model.predict(X_test)
# mae = mean_absolute_error(y_test, y_pred)
# print('Mean Absolute Error:', mae)
#
# # Step 7: Model deployment
# new_data = pd.read_csv('new_data.csv')
# predictions = model.predict(new_data)
#
#
#
# client = pymongo.MongoClient("mongodb+srv://bettermartAdmin1:<password>@bettermart.bpsssw1.mongodb.net/?retryWrites=true&w=majority")
# db = client.test


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

