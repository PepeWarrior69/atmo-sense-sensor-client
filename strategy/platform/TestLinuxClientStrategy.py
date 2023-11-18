from strategy.platform import PlatformClientStrategy
import socket

from strategy.sensor import TestSensorStrategy

class TestLinuxClientStrategy(PlatformClientStrategy):    
    @property
    def mac(self):
        try:
            # Get the MAC address on Linux
            with open(f'/sys/class/net/eth0/address') as file:
                mac_address = file.read().strip()
            return mac_address
        except Exception as e:
            print(f"Error getting MAC address on Linux: {e}")
            return None
    
    @property
    def ip(self):
        try:
            host_name = socket.gethostname()
            ip_address = socket.gethostbyname(host_name)
            
            return ip_address
        except socket.error as e:
            print(f"Error getting IP address: {e}")
            return None
        
    def add_connected_sensors(self):
        for _ in range(5):
            self.sensors.append(
                TestSensorStrategy()
            )
    
    