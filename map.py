import folium
import webbrowser
import get as get


def map(data):
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
    map.save("index.html")
    # open html file in browser
    webbrowser.open("index.html")


if __name__ == "__main__":
    data = get.get_wait_times()
    get.parse_wait_times(data)
    map(data)
