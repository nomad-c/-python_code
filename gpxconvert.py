import gpxpy.gpx
from datetime import datetime

# Read in your CSV file and parse the data into a list of waypoints
waypoints = []
with open('C:/Users/Czarny/Dropbox (Personal)/gpx/eksport/miejsca_o_clean.csv', 'r') as f:
    for line in f:
        lat, lon, name = line.strip().split(',')
        waypoint = gpxpy.gpx.GPXWaypoint(latitude=float(lat), longitude=float(lon), name=name)
        waypoint.type = 'Geocache'
        waypoint.sym = 'Geocache Found'
        waypoint.time = datetime(2001, 11, 23, 4, 56, 58)
        waypoint.cacheID = name
        waypoint.placed_by = 'Nomad'
        waypoint.owner = 'Nomad'
        waypoint.container = 'Regular'
        waypoint.difficulty = 2
        waypoint.terrain = 1.5
        waypoint.country = 'Poland'
        waypoint.state = 'Poland'
        waypoint.short_description = name
        waypoint.long_description = name
        waypoint.encoded_hints = 'OBEA GB OR JVAQ'
        waypoints.append(waypoint)

# Create a GPX object and add the waypoints to it
gpx = gpxpy.gpx.GPX()
for waypoint in waypoints:
    gpx.waypoints.append(waypoint)

# Write the GPX file to disk
with open('C:/Users/Czarny/Dropbox (Personal)/gpx/eksport/output.gpx', 'w') as f:
    f.write(gpx.to_xml())

print("It is done.")
