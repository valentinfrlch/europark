import folium
import webbrowser, os
import get as get
import rate as r


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
                id = line.split(',')[3].strip()
                wait_time = r.get_wait_time(id)
                folium.Marker(
                    location=[lat, lon], popup=name + "\ntime in line: " + wait_time).add_to(map)
            except Exception as e:
                pass
    # save the map as html
    map.save("index.html")
    # delete old information for next refresh
    os.remove("response.json")
    # open html file in browser
    webbrowser.open("index.html")




if __name__ == "__main__":
    data = get.get_wait_times()
    get.parse_wait_times(data)
    map(data)
