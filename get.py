# get history wait time data from https://queue-times.com/ API
# create a map


import requests
import json
# visualize wait times on a map
import folium
import webbrowser
import time, os

base_url = "https://queue-times.com/parks/51/queue_times.json"


def get_wait_times():
    files = os.listdir()
    # if there is no file called response.json, get new data
    if "response.json" not in files:
        response = requests.get(base_url)
        # save the data as a json file with timestamp as filename
        with open("response.json", "w") as f:
            json.dump(response.json(), f)
            data = json.loads(response.text)
    else:
        with open("response.json", "r") as f:
            data = json.load(f)
    return data


def parse_wait_times(data):
    lands = []
    rides = []
    rideInfo = []
    for item in data["lands"]:
        # append rides to rides list
        lands.append(item["rides"])

    # collect all rides in one list
    for item in lands:
        for i in item:
            rides.append(i)
    for ride in rides:
        ride = json.dumps(ride)
        ride = json.loads(ride)
        rideInfo.append(ride)
    return rideInfo
