# get history wait time data from https://queue-times.com/ API
# create a map


import requests
import json
# visualize wait times on a map
import folium
import webbrowser

base_url = "https://queue-times.com/parks/51/queue_times.json"


def get_wait_times():
    response = requests.get(base_url)
    data = json.loads(response.text)
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
        print(ride["name"])
        rideInfo.append(ride)
    return rideInfo
