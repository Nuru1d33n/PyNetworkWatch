import sqlite3

conn = sqlite3.connect("network.db")

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS network(ip)")
