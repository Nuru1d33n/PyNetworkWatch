import sqlite3
from datetime import datetime

class Logger:
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_filename) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS devices (
                    id INTEGER PRIMARY KEY,
                    ip TEXT,
                    mac TEXT,
                    name TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    def log_device(self, ip, mac, device_name="Unknown"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sqlite3.connect(self.db_filename) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO devices (ip, mac, name, timestamp)
                VALUES (?, ?, ?, ?)
            """, (ip, mac, device_name, timestamp))
            conn.commit()

    def fetch_devices(self):
        with sqlite3.connect(self.db_filename) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ip, mac, name, timestamp FROM devices ORDER BY timestamp DESC")
            return cursor.fetchall()
