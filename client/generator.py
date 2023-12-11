import random

from helpers import gen_random_word


def generate_log_line():
    ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))
    http_method = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
    uri = f'https://domain.com/example/{gen_random_word(random.randint(1, 5))}'
    http_status_code = random.randint(200, 500)
    log_line = f"{ip_address} {http_method} {uri} {http_status_code}\n"
    return log_line
