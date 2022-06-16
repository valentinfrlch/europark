from turtle import color
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
                # add marker to the map with color based on wait time
                color = r.color_rate(wait_time)
                icon = r.icon_rate(wait_time)
                map.add_child(folium.Marker(location=[
                              lat, lon], popup=name + "\ntime in line: " + wait_time + "min", icon=folium.Icon(color=color, icon="8", prefix="fa-solid", icon_color="white")))
            except Exception as e:
                print(e)
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
