import gpxpy.gpx
from datetime import datetime
import math

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

# Split waypoints into chunks of 1000 or less
waypoint_chunks = [waypoints[x:x+1000] for x in range(0, len(waypoints), 1000)]

# Create a GPX object for each chunk of waypoints and write it to a file
for i, chunk in enumerate(waypoint_chunks):
    gpx = gpxpy.gpx.GPX()
    for waypoint in chunk:
        gpx.waypoints.append(waypoint)
    file_name = f"C:/Users/Czarny/Dropbox (Personal)/gpx/eksport/output_{i+1}.gpx"
    with open(file_name, 'w') as f:
        f.write(gpx.to_xml())
    print(f"File '{file_name}' created")

print("It is done.")# Write your code here :-)
