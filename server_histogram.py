from prometheus_client import start_http_server, Histogram
import random
import time

REQUEST_TIME = Histogram('request_duration_seconds', 'Request duration in seconds')

def handle_request():
    with REQUEST_TIME.time():
        time.sleep(random.random() * 0.3)

if __name__ == '__main__':
    # exposing metrics on port 8000
    start_http_server(8000)
    print("Serving metrics on :8000/metrics")
    while True:
        handle_request()
        time.sleep(0.2)
