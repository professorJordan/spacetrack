from skyfield.api import load, wgs84
'''
stations_url = 'http://celestrak.org/NORAD/elements/stations.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')
'''

#This retrieves the TLE for a satellite with a given catalog number n in a list
n = 27844
url = 'https://celestrak.org/NORAD/elements/gp.php?CATNR={}'.format(n)
filename = 'tle-CATNR-{}.txt'.format(n)
#add argument reload=True once a day only!
satellites = load.tle_file(url, filename=filename)
print(satellites)

for satellite in satellites:
    #prints the TLE epoch
    print('epoch:', satellite.epoch.utc_jpl())

    #generating satellite position at current date / time
    ts = load.timescale()
    geocentric = satellite.at(ts.now())
    print(geocentric.position.km)

    #generate latitude & longtiude of satellite
    lat, lon = wgs84.latlon_of(geocentric)
    print(satellite.name, 'Latitude:', lat.degrees, 'Longitude:', lon.degrees)
   
    #get elevation of satellite & display in meters
    elevation_m = wgs84.height_of(geocentric)
    print(satellite.name, 'elevation in meters:', elevation_m.m)

    #Return geographic  position of satellite
    geo_position  = wgs84.geographic_position_of(geocentric)
    print(satellite.name, geo_position)
