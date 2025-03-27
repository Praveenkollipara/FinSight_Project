import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=PRAVEENLAPTOP\\SQLEXPRESS;'
    'DATABASE=FinSight_DB;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Insert simulated live market price for AAPL
cursor.execute('''
    INSERT INTO Market_Data (asset_symbol, current_price)
    VALUES (?, ?)
''', ('AAPL', 180.25))  # Example price

conn.commit()
print("Market Data Inserted Successfully!")

conn.close()
