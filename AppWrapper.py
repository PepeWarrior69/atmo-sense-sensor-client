from threading import Thread
from time import sleep

from app import App

class AppWrapper:
    def __init__(self):
        self.sensor_app = App()
        self.thread = None
        self.state = "INACTIVE"
    
    def app_thread_worker(self, endpoint_url: str, platform: str):
        self.sensor_app = App()
        self.sensor_app.main(endpoint_url, platform, False)
        self.state = "ACTIVE"
        
        while self.state == "ACTIVE":
            sleep(1)
        
    def start(self, endpoint_url: str, platform: str):
        self.thread = Thread(target=self.app_thread_worker, args=(endpoint_url, platform,))
        self.thread.start()
        
        while self.state == "INACTIVE":
            sleep(0.01)
        
    def stop(self):
        if not self.sensor_app or self.state == "INACTIVE" or not self.thread:
            return
        
        self.sensor_app.cleanup()
        self.state = "INACTIVE"
        self.thread.join()
        self.thread = None
        self.sensor_app = None
