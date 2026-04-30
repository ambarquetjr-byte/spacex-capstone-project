import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

url = "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

tables = pd.read_html(StringIO(str(soup)))

print(f"Total tables found: {len(tables)}")

for i, table in enumerate(tables):
    print(i, table.shape)

df = tables[2]

print(df.head())
print(df.columns)

df.to_csv("spacex_wikipedia_data.csv", index=False)

print("Wikipedia launch data saved as spacex_wikipedia_data.csv")