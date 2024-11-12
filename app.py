import os
import threading
from flask import Flask, render_template, jsonify, request
from core.alert import AlertManager
from core.logger import Logger
from core.network_monitor import NetworkMonitor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
DB_FILENAME = 'network_activity.db'

# Set up secret key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24))

# Initialize Logger and AlertManager
logger = Logger(DB_FILENAME)
alert_manager = AlertManager()
network_monitor = NetworkMonitor(logger, alert_manager)

# Background thread to monitor network
def start_network_monitor():
    network_monitor.start_monitoring()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/devices', methods=['GET'])
def get_logged_devices():
    devices = logger.fetch_devices()
    return jsonify(devices)

# Disconnect device API
@app.route('/api/disconnect_device', methods=['POST'])
def disconnect_device():
    data = request.get_json()
    device_ip = data.get("ip")
    device_mac = data.get("mac")
    
    # Attempt to disconnect the device using the network monitor
    success = network_monitor.disconnect_device(device_ip, device_mac)
    
    return jsonify({"success": success})


# Deauthentication route
@app.route('/api/deauth_device', methods=['POST'])
def deauth_device():
    data = request.get_json()
    target_mac = data.get("mac")
    bssid = data.get("bssid")  # BSSID of the access point (usually known or discovered)

    # Attempt to deauth the device
    success = network_monitor.deauth_device(target_mac, bssid)
    
    return jsonify({"success": success})

    
if __name__ == '__main__':
    # Start network monitor in a separate thread
    monitor_thread = threading.Thread(target=start_network_monitor)
    monitor_thread.daemon = True
    monitor_thread.start()
    app.run(debug=True)
