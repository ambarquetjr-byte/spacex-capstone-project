import requests
import pandas as pd

url = "https://api.spacexdata.com/v4/launches"

response = requests.get(url)
data_json = response.json()

data = pd.json_normalize(data_json)

print(data.head())
print(data.columns)

data.to_csv("spacex_api_data.csv", index=False)

print("SpaceX API data saved as spacex_api_data.csv")