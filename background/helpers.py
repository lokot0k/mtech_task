import os
import time


def wait_for_file_release(lockfile: str) -> bool:
    is_acquired = False
    while os.path.exists(lockfile):
        time.sleep(0.1)
    try:
        os.open(lockfile, os.O_CREAT | os.O_EXCL)
        is_acquired = True
    finally:
        return is_acquired


def writer(directory: str, filename: str):
    full_name = os.path.join(directory, filename)
    lock_name = full_name + '.lock'
    data_accumulation = []  # accumulate the data which weren't wroted in file

    def write_to_file(data: str):
        data_accumulation.append(data + '\n')
        if wait_for_file_release(lock_name):
            with open(full_name, 'a+') as file:
                file.writelines(data_accumulation)
            data_accumulation.clear()
            os.remove(lock_name)

    return write_to_file
