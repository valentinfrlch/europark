# return wait time for requested id

from get import get_wait_times
import get as get


def get_wait_time(id):
    data = get.get_wait_times()
    parsed = get.parse_wait_times(data)
    # get the item in parsed that has the requested id
    for item in parsed:
        if item["id"] == id:
            return item["wait_time"]
