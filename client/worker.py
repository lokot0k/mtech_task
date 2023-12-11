import random
import threading
import time

import requests
from requests import RequestException


class Worker(threading.Thread):
    def __init__(self, lock, data_generator, write_method, delay, url):
        super().__init__()
        self.daemon = True
        self.lock = lock
        self.data_generator = data_generator
        self.write = write_method
        self.delay = delay
        self.url = url

    def run(self):
        while True:
            time.sleep(random.randint(0, self.delay) / 1000)
            data = self.data_generator()
            self.make_request(data)
            self.lock.acquire()
            self.write(data)
            self.lock.release()

    def make_request(self, data):
        body = {'log': data}
        try:
            requests.post(self.url, json=body)
        except RequestException as e:
            print("Service is unavailable:", e)
