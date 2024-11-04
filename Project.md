## Suggested Project Structure

PyNetworkWatch/
│
├── main.py                   # Entry point of the NIDS, starts the monitoring
├── requirements.txt          # List of required packages
├── README.md                 # Project overview and instructions
├── LICENSE                   # License information
│
├── network_monitor.py        # Contains functions for network monitoring and device detection
├── alert.py                  # Handles alert notifications (e.g., email alerts)
├── logger.py                 # Manages logging of detected devices and activities
├── behavior_analysis.py       # Analyzes user behavior and identifies anomalies (optional)
└── database.py               # Manages SQLite database interactions



### File Descriptions

1. **`main.py`**
   * This will be the entry point of your application. It will import necessary functions from other modules and coordinate the overall functionality, such as starting the network monitor, logging, and alerting.
2. **`network_monitor.py`**
   * Contains functions for monitoring the network, such as sniffing packets, detecting connected devices, and checking for unauthorized access attempts.
   * You can use the Scapy library here for packet manipulation.
3. **`alert.py`**
   * This module will handle sending alerts (like email notifications) when an unauthorized device is detected. It will include functions to set up the SMTP connection and format the alert messages.
4. **`logger.py`**
   * Responsible for logging device activities and any detected anomalies. This module will interact with the SQLite database to store relevant data for analysis later.
5. **`behavior_analysis.py` (optional)**
   * If you choose to implement user behavior analysis, this module can contain functions that analyze user activity patterns and detect any anomalies based on predefined criteria.
6. **`database.py`**
   * Manages all interactions with the SQLite database, including creating tables, inserting logs, and querying for device information. This module encapsulates the database logic and allows other modules to interact with the database without needing to know the details.
