import get as get
import json
# sort rides by wait time


def sort_rides(rides):
    """
    Sort rides by wait time
    """
    sort = sorted(rides, key=lambda ride: ride["wait_time"])
    # return only the names
    names_sort = [ride["name"] for ride in sort]
    return names_sort


print(sort_rides(get.parse_wait_times(get.get_wait_times())))
