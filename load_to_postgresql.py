import os
import pandas as pd
from sqlalchemy import create_engine, inspect, text
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()
password = os.getenv("PG_PASSWORD")

if not password:
    raise ValueError("PG_PASSWORD environment variable not set")

df = pd.read_excel("manufacturing_clean.xlsx")
df.columns = df.columns.str.strip().str.lower()

database_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password=password,
    host="localhost",
    port=5432,
    database="manufacturing_db"
)

engine = create_engine(database_url)

with engine.begin() as conn:
    if inspect(conn).has_table("production_data", schema="public"):
        conn.execute(
            text("DELETE FROM public.production_data")
        )

        df.to_sql("production_data", con=conn, schema="public", if_exists="append", index=False)

print("Production data loaded successfully")
print(f"Rows loaded: {len(df)}")