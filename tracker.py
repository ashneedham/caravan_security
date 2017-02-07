from modules.Gps import Gps
from modules.GoogleMaps import GoogleMaps
from modules.Sms import Sms
import sys

print('Booting GPS...')
gpsObj = Gps()
latLong = gpsObj.get_current_location()
print(latLong)
mapObj = GoogleMaps(latLong['lat'], latLong['long'])
print(mapObj.get_maps_url())
modem = Sms()
print('Sending SMS...')
modem.send_sms(mapObj.get_maps_url(), '07846347904')
del gpsObj
del mapObj
del modem
sys.exit()
