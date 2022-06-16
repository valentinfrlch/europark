# get history wait time data from https://queue-times.com/ API
#create a map


import requests
import json
# visualize wait times on a map
import folium, webbrowser

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

def map(rideInfo=0):
    # create a map
    coords = (48.265, 7.7219845)
    map = folium.Map(location=coords, zoom_start=16)
    # save the map as html
    map.save("map.html")
    # open html file in browser
    webbrowser.open("map.html")


map()
#print(parse_wait_times(get_wait_times()))