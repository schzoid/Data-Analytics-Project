import pandas as pd

df = pd.read_excel("manufacturing_raw.xlsx")
df["Line"] = df["Line"].str.strip().str.title()

df = df.drop_duplicates()
df = df.dropna(subset=["Product"])

df = df[df["Downtime_Minutes"] >= 0]

df["Good_Units"] = df["Produced_Units"] - df["Defect_Count"]

df["Defect_Rate"] = (df["Defect_Count"] / df["Produced_Units"]) * 100

df["Production_Efficiency"] = (df["Good_Units"] / df["Produced_Units"]) * 100

df.to_excel("manufacturing_clean.xlsx", index=False)


