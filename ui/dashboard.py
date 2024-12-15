# ui/dashboard.py
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def fetch_latest_data():
    """Fetch the latest market data from the database."""
    conn = sqlite3.connect("data/market_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM market_data ORDER BY timestamp DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route("/")
def dashboard():
    data = fetch_latest_data()
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)