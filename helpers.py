import json


def distance(p1, p2):
    # return the distance between two points in meters
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# create area polygon from list of coordinates
def create_area(coords):
    #read ids from file
    with open('regions.json') as f:
        data = json.load(f)
        # get the coordinates for the children
        for item in data:
            children = []
            for child in item["children"]:
                children.append()
            