import datetime

import requests
from requests import RequestException


class DataProvider:
    def __init__(self, url: str):
        self.url = url
        self.date_from = datetime.datetime.fromtimestamp(0)

    def fetch_data(self):
        try:
            resp = requests.get(url=self.url,
                                params={
                                    'date_from': self.date_from,
                                })
            self.date_from = datetime.datetime.now()
        except RequestException as e:
            print('Can\'t fetch data:', e)
            return None

        return str(resp.json())
