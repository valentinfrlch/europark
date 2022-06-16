# get history wait time data from https://queue-times.com/ API

import requests
import json

base_url = "https://queue-times.com/parks/51/queue_times.json"


def get_wait_times():
    response = requests.get(base_url)
    data = json.loads(response.text)
    return data


def parse_wait_times(data):
    wait_times = []
    for item in data:
        wait_times.append(item['wait_time'])
    return wait_times
