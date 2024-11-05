from flask import Flask, render_template
import sqlite3
import threading
from core.network_monitor import NetworkMonitor
from core.logger import Logger
from core.alert import AlertManager

app = Flask(__name__)
DB_FILENAME = 'network_activity.db'

def get_logged_devices():
    with sqlite3.connect(DB_FILENAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT ip, mac, name, timestamp FROM devices ORDER BY timestamp DESC")
        devices = cursor.fetchall()
    return devices

@app.route('/')
def home():
    devices = get_logged_devices()
    return render_template('index.html', devices=devices)

def start_network_monitor():
    logger = Logger(DB_FILENAME)
    alert_manager = AlertManager()
    network_monitor = NetworkMonitor(logger, alert_manager)
    network_monitor.start_monitoring()

if __name__ == '__main__':
    monitor_thread = threading.Thread(target=start_network_monitor)
    monitor_thread.daemon = True
    monitor_thread.start()
    app.run(debug=True)
