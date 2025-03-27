import yfinance as yf
import pyodbc

# Fetch live data for AAPL
ticker = yf.Ticker('AAPL')
price = ticker.info['regularMarketPrice']

print(f" Live Price of AAPL: {price}")

# Insert into Market_Data table
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=PRAVEENLAPTOP\\SQLEXPRESS;'
    'DATABASE=FinSight_DB;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()
cursor.execute('''
    INSERT INTO Market_Data (asset_symbol, current_price)
    VALUES (?, ?)
''', ('AAPL', price))

conn.commit()
print(" Live Market Price Inserted Successfully!")

conn.close()
