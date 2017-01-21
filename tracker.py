from modules.Gps import Gps
from modules.GoogleMaps import GoogleMaps
import sys

print('Booting GPS...')
gpsObj = Gps()
latLong = gpsObj.getCurrentLocation()
print(latLong)
mapObj = GoogleMaps(latLong['lat'], latLong['long'])
print(mapObj.getMapsUrl())
del gpsObj
del mapObj
sys.exit()