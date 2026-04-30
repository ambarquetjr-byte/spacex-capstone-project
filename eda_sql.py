import pandas as pd
import sqlite3

df = pd.read_csv("spacex_cleaned_data.csv")

conn = sqlite3.connect("spacex.db")

df.to_sql("SPACEXTBL", conn, if_exists="replace", index=False)

query1 = """
SELECT *
FROM SPACEXTBL
LIMIT 20;
"""

query2 = """
SELECT COUNT(*)
FROM SPACEXTBL;
"""

print("First 20 records:")
print(pd.read_sql(query1, conn))

print("Total records:")
print(pd.read_sql(query2, conn))

conn.close()