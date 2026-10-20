import os
import pandas as pd
from sqlalchemy import create_engine, inspect, text
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()
password = os.getenv("PG_PASSWORD")

if not password:
    raise ValueError("PG_PASSWORD environment variable not set")

df = pd.read_excel("data_quality_summary.xlsx")

database_url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password=password,
    host="localhost",
    port="5432",
    database="manufacturing_db",
)

engine = create_engine(database_url)

with engine.connect() as conn:
    if inspect(conn).has_table(table_name="data_quality_summary", schema="public"):
        conn.execute(text(f"DELETE FROM public.data_quality_summary"))
        df.to_sql(
            "data_quality_summary",
            con=conn,
            schema="public",
            if_exists="append",
            index=False,
        )

print("Data quality report loaded successfully")
print(f"Rows loaded: {len(df)}")