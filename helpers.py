import json
import folium


def distance(p1, p2):
    # return the distance between two points in meters
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# create area polygon from list of coordinates


def read_areas():
    #read ids from file
    with open('regions.json') as f:
        data = json.load(f)
        # get the coordinates for the children
        for item in data:
            # parse the item json
            item = json.dumps(item)
            print(item)
            for child in item["children"]:
                print(child)


def create_area(coords):
    # create area polygon from list of coordinates
    return folium.Polygon(coords)

