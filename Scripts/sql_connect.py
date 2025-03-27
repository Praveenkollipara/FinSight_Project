import pyodbc

# Change the SERVER name to your system's SSMS server name
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=PRAVEENLAPTOP\\SQLEXPRESS;'
    'DATABASE=FinSight_DB;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()
print(" Connected to SQL Server Successfully!")

conn.close()
