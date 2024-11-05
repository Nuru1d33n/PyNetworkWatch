# main.py
from core.network_monitor import NetworkMonitor
from core.alert import AlertManager
from core.logger import Logger


def main():
    # Database filename
    db_filename = 'network_activity.db'

    # Initialize logger and alert manager
    logger = Logger(db_filename)
    alert_manager = AlertManager()

    # Start network monitoring
    network_monitor = NetworkMonitor(logger, alert_manager)
    network_monitor.start_monitoring()


if __name__ == "__main__":
    main()
