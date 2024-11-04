# Manages all interactions with the SQLite database, including creating tables, inserting logs, and querying for device information. This module encapsulates the database logic and allows other modules to interact with the database without needing to know the details.

import sqlite3

def initialize_database():
    conn = sqlite3.connect('network_logs.db')
    cursor = conn.cursor()

    # Create devices table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mac_address TEXT UNIQUE NOT NULL,
        ip_address TEXT,
        device_name TEXT,
        status TEXT CHECK(status IN ('authorized', 'unauthorized')) NOT NULL,
        last_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
        first_seen DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create logs table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create alerts table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id INTEGER,
        alert_message TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (device_id) REFERENCES devices(id)
    )
    ''')

    # Create user behavior table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_behavior (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        action TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()

# Call this function to initialize the database at the start of your application
initialize_database()
