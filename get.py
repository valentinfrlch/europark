# get history wait time data from https://queue-times.com/ API

import requests
import json

base_url = "https://queue-times.com/parks/51/queue_times.json"


def get_wait_times():
    response = requests.get(base_url)
    data = json.loads(response.text)
    return data


def parse_wait_times(data):
    rides = []
    rideInfo = []
    for item in data["lands"]:
        #append rides to rides list
        rides.append(item["rides"])
    for ride in rides:
        #append wait times to wait_times list
        # read ride as json object
        ride = json.dumps(ride[0])
        ride = json.loads(ride)
        ride_time = ride["wait_time"]
        ride_id = ride["id"]
        rideInfo.append([ride_id, ride_time])
    return rideInfo

print(parse_wait_times(get_wait_times()))