from modules.Gps import Gps
from modules.GoogleMaps import GoogleMaps
from modules.Sms import Sms
import os
import config


def get_message():
    sender_number = os.environ['SMS_1_NUMBER']

    # Are there any decoded parts?
    numparts = int(os.environ['DECODED_PARTS'])

    if numparts:
        # Get all text parts
        msg_text = ''
        for i in range(0, numparts):
            varname = 'DECODED_%d_TEXT' % i
            if varname in os.environ:
                msg_text = msg_text + os.environ[varname]
    else:
        msg_text = os.environ['SMS_1_TEXT']

    msg_text = msg_text.decode('UTF-8')
    return sender_number, msg_text


def handle_command(msg_text, sender_number):
    stripped_text = msg_text.lower().strip()

    if stripped_text == 'where are you':
        gpsobj = Gps()
        latlong = gpsobj.get_current_location()
        mapobj = GoogleMaps(latlong['lat'], latlong['long'])
        modem = Sms()
        modem.send_sms(mapobj.get_maps_url(), sender_number)

        del gpsobj
        del mapobj
        del modem


def validate_senders_number(senders_number):
    return senders_number in config.settings['allowed_numbers']


number, text = get_message()
if validate_senders_number(number):
    handle_command(text, number)
