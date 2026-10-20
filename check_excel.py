import pandas as pd

df = pd.read_excel("manufacturing_clean.xlsx")

print("First 5 rows")
print(df.head())

print("Dataset Shape")
print(df.shape)

print("Missing Values")
print(df.isnull().sum())

print("Duplicated Values")
print(df.duplicated().sum())

print()

print("Line Values")
print(df["Line"].value_counts())

print()

print("Invalid Downtime")
print(df[df["Downtime_Minutes"] < 0])