import sqlite3

DB_FILENAME = 'network_activity.db'

def update_database():
    with sqlite3.connect(DB_FILENAME) as conn:
        cursor = conn.cursor()
        # Add the `device_name` column if it doesn't already exist
        cursor.execute("ALTER TABLE devices ADD COLUMN device_name TEXT")
        conn.commit()
    print("Database updated successfully. `device_name` column added.")

if __name__ == '__main__':
    update_database()
