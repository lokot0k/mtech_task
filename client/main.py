from config import Settings
import threading

from generator import generate_log_line
from helpers import writer
from worker import Worker


def main():
    settings = Settings()
    lock = threading.Lock()
    write_to_file = writer(settings.LOG_FILE)
    for i in range(settings.THREADS_AMOUNT):
        t = Worker(lock, generate_log_line, write_to_file,
                   settings.REQUEST_DELAY_LIMIT, settings.URL)
        t.start()

    while True:
        pass


if __name__ == "__main__":
    main()
