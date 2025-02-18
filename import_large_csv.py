import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="Aaru@111",  
    database="FreelanceDB"
)
cursor = conn.cursor()

# Read CSV in chunks (for large files)
chunksize = 5000  
for chunk in pd.read_csv("large_data.csv", chunksize=chunksize):
    data = [tuple(row) for row in chunk.values]
    sql = "INSERT IGNORE INTO users (id, name, age, email) VALUES (%s, %s, %s, %s)"
    cursor.executemany(sql, data)  # Batch insert

conn.commit()
cursor.close()
conn.close()

print("✅ Large CSV imported successfully!")
