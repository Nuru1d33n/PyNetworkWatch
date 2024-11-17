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

# ARP spoofing route
@app.route('/api/arp_spoof', methods=['POST'])
def arp_spoof():
    data = request.get_json()
    target_ip = data.get("ip")
    target_mac = data.get("mac")
    gateway_ip = data.get("gateway_ip")

    # Attempt ARP spoofing
    success = network_monitor.arp_spoof(target_ip, target_mac, gateway_ip)
    
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
