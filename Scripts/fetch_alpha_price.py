import requests
import pyodbc
import time

API_KEY = '3LZ4T1R70FJHAUK9'
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=PRAVEENLAPTOP\\SQLEXPRESS;'
    'DATABASE=FinSight_DB;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

symbols = ['AAPL', 'MSFT', 'ETH', 'AMZN', 'GOOGL', 'NVDA', 'FXAIX', 'XRP', 'DOGE', 'SILVER']

manual_assets = {
    'XRP': 0.65,
    'DOGE': 0.075,
    'SILVER': 34.09
}
for symbol in symbols:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    try:
        price = float(data['Global Quote']['05. price'])
        print(f'{symbol} price fetched: {price}')
    except Exception as e:
        if symbol in manual_assets:
            price = manual_assets[symbol]
            print(f'{symbol} manual price used: {price}')
        else:
            print(f'Skipping {symbol}, no price found.')
            continue  # Skip inserting if no fallback
     
    # Insert price into DB
    cursor.execute('''
        INSERT INTO Market_Data (asset_symbol, current_price, timestamp)
        VALUES (?, ?, GETDATE())
    ''', (symbol, price))

    conn.commit()
    time.sleep(12)

conn.close()
