import pandas as pd

df = pd.read_csv("users.csv")
# print(df)

# zobrazi 2 riadky
print(df.head(2))


df = pd.read_csv("data.csv")

df.head()
df.tail()
df.shape
df.columns
df.info()
df.describe()

# Výber stĺpca:
df[["name", "age"]]

# Riadok
df.iloc[0]

# Filtrovanie
df[df["age"] > 25]

# Viac podmienok
df[(df["age"] > 25) & (df["salary"] > 2000)]

# Štatistiky
df["salary"].mean()
df["salary"].sum()
df["salary"].min()
df["salary"].max()

# Nový stĺpec
# df["new_column"] = ...

# TODO Filtering + transformations
df[df["age"] > 25]

print(df[["name", "salary"]])

df.sort_values("salary")

df["salary_usd"] = df["salary"] * 1.17

# groupby()
df.groupby("department")["salary"].mean()

# TODO Cleaning data
# missing values
# duplicates
# incorrect types
# strings
# dates
# NaN

df.isna().sum()
df.dropna()
df.fillna(0)
df.drop_duplicates()
df["date"] = pd.to_datetime(df["date"])