import time

from config import Settings
from data_provider import DataProvider
from helpers import writer


def main():
    settings = Settings()
    write_to_file = writer(settings.DIRECTORY, settings.FILE_NAME)
    provider = DataProvider(settings.URL)
    while True:
        time.sleep(settings.REQUEST_DELAY / 1000)
        data = provider.fetch_data()
        if data:
            write_to_file(data)


if __name__ == '__main__':
    main()
