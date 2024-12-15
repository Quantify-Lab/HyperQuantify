# data/live_data_collector.py
import requests
import time
import sqlite3

API_URL = "https://api.hyperliquid.com"
DB_PATH = "data/market_data.db"

def fetch_market_data():
    """Fetch market data from Hyperliquid API."""
    response = requests.get(f"{API_URL}/market-data")
    return response.json()

def store_data(data):
    """Store fetched data into an SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS market_data (
            timestamp TEXT,
            symbol TEXT,
            price REAL,
            volume REAL
        )
    """)
    for item in data:
        cursor.execute("""
            INSERT INTO market_data (timestamp, symbol, price, volume)
            VALUES (?, ?, ?, ?)
        """, (item['timestamp'], item['symbol'], item['price'], item['volume']))
    conn.commit()
    conn.close()

def collect_data(interval=10):
    """Periodic task to fetch and store market data."""
    while True:
        data = fetch_market_data()
        store_data(data)
        time.sleep(interval)

if __name__ == "__main__":
    collect_data()