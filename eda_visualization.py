import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("spacex_cleaned_data.csv")

print(df.head())
print(df.columns)

if "success" in df.columns:
    sns.countplot(x="success", data=df)
    plt.title("Launch Success Count")
    plt.xlabel("Success")
    plt.ylabel("Count")
    plt.show()

if "flight_number" in df.columns and "success" in df.columns:
    sns.scatterplot(x="flight_number", y="success", data=df)
    plt.title("Flight Number vs Launch Success")
    plt.xlabel("Flight Number")
    plt.ylabel("Success")
    plt.show()

if "date_utc" in df.columns:
    df["year"] = pd.to_datetime(df["date_utc"]).dt.year
    yearly = df.groupby("year").size()

    yearly.plot(kind="bar")
    plt.title("Number of Launches by Year")
    plt.xlabel("Year")
    plt.ylabel("Launch Count")
    plt.show()