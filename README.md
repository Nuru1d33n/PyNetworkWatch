# PyNetworkWatch

PyNetworkWatch is a lightweight Python-based Network Intrusion Detection System (NIDS) designed for real-time monitoring of small networks. It detects unauthorized access attempts, tracks device activity, and sends alert notifications to administrators, making it ideal for home and small office environments.

## Features

- **Device Detection**: Monitors the network for connected devices using ARP scanning.
- **Intrusion Detection**: Alerts administrators to unauthorized access attempts.
- **Logging**: Maintains a log of detected devices and their connection activities.
- **Email Notifications**: Sends real-time alerts via email when unauthorized devices are detected.
- **Lightweight**: Designed to run efficiently on minimal resources.

## Requirements

- Python 3.x
- Required packages:
  - `scapy`
  - `sqlite3` (built-in)
  - `smtplib` (built-in)
  - `email` (built-in)

You can install the required packages using pip:

```bash
pip install scapy python-nmap schedule psutil
```


### Next Steps

- Update the README with your contact information and any specific installation instructions.
- Create a `LICENSE` file if you want to open-source your project.
- Consider adding a `requirements.txt` file for easy package installation.

### Repository Structure Suggestion

Consider structuring your repository with the following folders and files:

Feel free to adjust the README content or repository structure as needed! If you have any further questions or need help with anything else, just let me know!
