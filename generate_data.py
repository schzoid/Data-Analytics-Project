import pandas as pd
from datetime import datetime, timedelta
import random

start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 6, 30)

lines = {
    "Line A": {
        "base_production": 1100,
        "base_defect_rate": 0.015
    },

    "Line B": {
        "base_production": 1000,
        "base_defect_rate": 0.025
    },

    "Line C": {
        "base_production": 900,
        "base_defect_rate": 0.035
    }
}

shifts = {
    "Morning": 1.00,
    "Evening": 0.95,
    "Night": 0.88
}

products = {
    "P-101": 1.00,
    "P-102": 0.95,
    "P-103": 0.90,
    "P-104": 0.85,
}

data = []

current_date = start_date

while current_date <= end_date:
    for line_name, line_info in lines.items():
        for shift_name, shift_multiplier in shifts.items():

            product = random.choice(list(products.keys()))
            product_multiplier = products[product]
            downtime_minutes = random.randint(0, 90)
            downtime_multiplier = 1 - (downtime_minutes / 600)
            random_variation = random.uniform(0.95, 1.05)
            produced_units = int(
                line_info["base_production"]
                * shift_multiplier
                * product_multiplier
                * downtime_multiplier
                * random_variation
            )

            defect_rate = line_info["base_defect_rate"]

            if shift_name == "Night":
                defect_rate += 0.01

            if product == "P-104":
                defect_rate += 0.008

            defect_count = int(produced_units * defect_rate)

            row = {
                "Date": current_date,
                "Line": line_name,
                "Shift": shift_name,
                "Product": product,
                "Produced_Units": produced_units,
                "Defect_Count": defect_count,
                "Downtime_Minutes": downtime_minutes
            }
            data.append(row)

    current_date += timedelta(days=1)

df = pd.DataFrame(data)

for i in random.sample(range(len(df)), 15):
    df.loc[i, "Product"] = None

for i in random.sample(range(len(df)), 10):
    df.loc[i, "Line"] = df.loc[i, "Line"].lower()

for i in random.sample(range(len(df)), 5):
    df.loc[i, "Downtime_Minutes"] = -10

duplicates = df.sample(10)
df = pd.concat([df, duplicates], ignore_index=True)

print(df.head())
print()
print(df.shape)

df.to_excel("manufacturing_raw.xlsx", index=False)

print("'manufacturing_raw.xlsx' created")