import pandas as pd

df = pd.read_csv("spacex_api_data.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

falcon1_id = "5e9d0d95eda69955f709d1eb"

data_falcon9 = df[df["rocket"] != falcon1_id].copy()

print("Number of Falcon 9 launches:", data_falcon9.shape[0])

data_falcon9.to_csv("spacex_cleaned_data.csv", index=False)

print("Cleaned Falcon 9 data saved as spacex_cleaned_data.csv")