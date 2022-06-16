# return wait time for requested id

from multiprocessing.connection import wait
from get import get_wait_times
import get as get


def get_wait_time(id):
    if type(id) == str:
        id = int(id)
    data = get.get_wait_times()
    parsed = get.parse_wait_times(data)
    # get the item in parsed that has the requested id
    for item in parsed:
        if item["id"] == id:
            wait_time = str(item["wait_time"])
            return wait_time
