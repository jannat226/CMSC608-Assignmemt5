import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to MySQL
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Run a sample query
query = "SELECT * FROM Customers LIMIT 5"
df = pd.read_sql(query, conn)

# Print results
print(df)

conn.close()
