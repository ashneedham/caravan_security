from modules.Gps import Gps
from modules.GoogleMaps import GoogleMaps
from modules.Sms import Sms
import os

def getMessage():
    number = os.environ['SMS_1_NUMBER']

    # Are there any decoded parts?
    numparts = int(os.environ['DECODED_PARTS'])

    if numparts:
        # Get all text parts
        text = ''
        for i in range(0, numparts):
            varname = 'DECODED_%d_TEXT' % i
            if varname in os.environ:
                text = text + os.environ[varname]
    else:
        text = os.environ['SMS_1_TEXT']

    text = text.decode('UTF-8')
    return number, text

def handleCommand(text, number):

    if text.lower().strip() == 'where are you':
        gpsObj = Gps()
        latLong = gpsObj.getCurrentLocation()
        mapObj = GoogleMaps(latLong['lat'], latLong['long'])
        modem = Sms()
        modem.sendSMS(mapObj.getMapsUrl(), number)

        del gpsObj
        del mapObj
        del modem


number, text = getMessage()
handleCommand(text, number)