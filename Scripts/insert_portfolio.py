import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=PRAVEENLAPTOP\\SQLEXPRESS;'
    'DATABASE=FinSight_DB;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Insert one portfolio entry (Apple Stock Example)
cursor.execute('''
    INSERT INTO Portfolio (asset_type, asset_symbol, quantity, buy_price, purchase_date)
    VALUES (?, ?, ?, ?, ?)
''', ('Stock', 'AAPL', 10, 150, '2024-12-15'))

conn.commit()
print("Portfolio Data Inserted Successfully!")

conn.close()
