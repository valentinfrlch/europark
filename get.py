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


def map():
    # create a map
    coords = (48.265, 7.7219845)
    map = folium.Map(location=coords, zoom_start=16)
    # add markers from coords.json to the map
    with open('coords.txt') as f:
        lines = f.readlines()
        for line in lines:
            try:
                name = line.split(',')[0]
                lat = line.split(',')[1].strip()
                lon = line.split(',')[2].strip()
                print(name, lat, lon)
                folium.Marker(location=[lat, lon], popup=name).add_to(map)
            except Exception as e:
                pass
    # save the map as html
    map.save("map.html")
    # open html file in browser
    webbrowser.open("map.html")


map()
