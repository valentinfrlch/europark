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


def color_rate(wait_time):
    time = int(wait_time)
    if time <= 15:
        return "green"
    elif time <= 30:
        return "orange"
    else:
        return "red"


def icon_rate(wait_time):
    time = int(wait_time)
    if time <= 10:
        return "fa-solid fa-circle-1"
    elif time <= 20:
        return "fa-solid fa-circle-2"
    elif time <= 30:
        return "fa-solid fa-circle-3"
    elif time <= 40:
        return "fa-solid fa-circle-4"
    elif time <= 50:
        return "fa-solid fa-circle-5"
    elif time <= 60:
        return "fa-solid fa-circle-6"
    elif time <= 70:
        return "fa-solid fa-circle-7"
    elif time <= 80:
        return "fa-solid fa-circle-8"
    elif time <= 90:
        return "fa-solid fa-circle-9"
    else:
        return "fa-solid fa-circle-10"
