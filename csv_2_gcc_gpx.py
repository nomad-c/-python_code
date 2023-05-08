
# Read in your CSV file and parse the data into a list of waypoints
with open("C:/Users/Czarny/Dropbox (Personal)/gpx/eksport/output.gpx", "w") as zapis:
    gpx = '<?xml version="1.0" encoding="utf-8"?>\n'
    gpx += '<gpx xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    gpx += 'mlns:xsd="http://www.w3.org/2001/XMLSchema"'
    gpx += ' version="1.0.1" creator="Groundspeak, '
    gpx += 'Inc. All Rights Reserved. http://www.groundspeak.com"'
    gpx += ' xsi:schemaLocation="http://www.topografix.com/GPX/1/0 '
    gpx += 'http://www.topografix.com/GPX/1/0/gpx.xsd '
    gpx += 'http://www.groundspeak.com/cache/1/0 '
    gpx += 'http://www.groundspeak.com/cache/1/0/cache.xsd"'
    gpx += ' xmlns="http://www.topografix.com/GPX/1/0">\n'
    gpx += "  <name>Geocaching GPX</name>\n"
    gpx += "  <desc>Geocaching GPX file created from a CSV file</desc>\n"
    gpx += "  <author>Python script</author>\n"
    gpx += "  <email>contact@geocaching.com</email>\n"
    gpx += "  <url>http://www.geocaching.com</url>\n"
    gpx += "  <urlname>Geocaching - High Tech Treasure Hunting</urlname>\n"
    gpx += "  <time>2010-10-10T22:54:31.1487819Z</time>\n"
    gpx += "  <keywords>cache, geocache</keywords>\n"
    gpx += '  <bounds minlat="0" minlon="0" maxlat="0" maxlon="0" />\n'
    numer = 0
    zapis.write(gpx)
    waypoints = []
    with open("C:/Users/Czarny/Dropbox (Personal)/gpx/plikbts2.csv", "r") as f:
        for line in f:
            lat, lon, name = line.strip().split(",")
            numer = numer + 1
            zapis.write('<wpt lat="')
            zapis.write(lat)
            zapis.write('" lon="')
            zapis.write(lon)
            zapis.write('">\n')
            gpx = " <time>2007-09-20T07:00:00Z</time>\n "
            gpx += "<name>"
            zapis.write(gpx)
            hex_string = hex(numer)[2:].upper()
            unikid = hex_string.zfill(8)
            zapis.write(unikid)
            gpx = "</name>\n"
            gpx += "<desc>"
            zapis.write(gpx)
            zapis.write(name)
            gpx = "</desc>\n"
            gpx += "<url></url>\n<urlname>"
            zapis.write(gpx)
            zapis.write(unikid)
            gpx = "</urlname>\n"
            gpx += (
                "<sym>Geocache Found</sym>\n<type>Geocache|Traditional Cache</type>\n"
            )
            gpx += '<groundspeak:cache id="'
            zapis.write(gpx)
            zapis.write(unikid)
            gpx = '" available="True" archived="False" xmlns:groundspeak'
            gpx += '="http://www.groundspeak.com/cache/1/0">\n'
            gpx += " <groundspeak:name>"
            zapis.write(gpx)
            zapis.write(unikid)
            gpx = "</groundspeak:name>\n"
            gpx += '<groundspeak:placed_by>PL</groundspeak:placed_by>'
            gpx += '\n<groundspeak:owner'
            gpx += ' id="1212141">Nomad</groundspeak:owner>'
            gpx += '\n<groundspeak:type>Traditional '
            gpx += 'Cache</groundspeak:type>\n<groundspeak:container>'
            gpx += 'Small</groundspeak:container>'
            gpx += '\n<groundspeak:difficulty>1.5</groundspeak:dif'
            gpx += 'ficulty>\n<groundspeak:terrain>3'
            gpx += '</groundspeak:terrain>\n<groundspeak:country>PL'
            gpx += ' </groundspeak:country>\n<groundspeak:state>'
            gpx += '\n</groundspeak:state>'
            gpx += '<groundspeak:short_description html="False">'
            gpx += '</groundspeak:short_description>'
            gpx += '<groundspeak:long_description html="False">'
            gpx += 'opis</groundspeak:long_description>'
            gpx += '<groundspeak:encoded_hints>Born2bwild</groundspeak:'
            gpx += 'encoded_hints><groundspeak:logs>'
            gpx += '<groundspeak:log id="130647008"><groundspeak:'
            gpx += 'date>2010-10-10T19:00:00Z</groundspeak:date>'
            gpx += '<groundspeak:type>Found it</groundspeak:type><groundspeak:finder '
            gpx += 'id="3479526">hokeycokey</groundspeak:finder>'
            gpx += '<groundspeak:text encoded="False">TFTC</groundspeak:text>'
            gpx += '</groundspeak:log></groundspeak:logs><groundspeak:travelbugs'
            gpx += ' /></groundspeak:cache>\n</wpt>\n'
            zapis.write(gpx)
    zapis.write("</gpx>")


print("It is done.")
