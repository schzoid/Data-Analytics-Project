import pandas as pd

raw_df = pd.read_excel("manufacturing_raw.xlsx")
clean_df = pd.read_excel("manufacturing_clean.xlsx")

valid_lines = ["Line A", "Line B", "Line C"]

raw_records = len(raw_df)
clean_records = len(clean_df)

duplicate_rows = raw_df.duplicated().sum()
missing_products = raw_df["Product"].isna().sum()

invalid_lines = (
    ~raw_df["Line"].isin(valid_lines)
).sum()

invalid_downtime = (
    raw_df["Downtime_Minutes"] < 0
).sum()

removed_rows = raw_records - clean_records

quality_report = pd.DataFrame([{
    "raw_records": raw_records,
    "clean_records": clean_records,
    "duplicate_rows": duplicate_rows,
    "missing_products": missing_products,
    "invalid_lines": invalid_lines,
    "invalid_downtime": invalid_downtime,
    "removed_rows": removed_rows,
}])

print(quality_report)

assert clean_df.duplicated().sum() == 0
assert clean_df["Product"].isna().sum() == 0
assert (clean_df["Downtime_Minutes"] < 0).sum() == 0
assert (~clean_df["Line"].isin(valid_lines)).sum() == 0

quality_report.to_excel("data_quality_summary.xlsx", index=False)
print("Successfully Created!")

