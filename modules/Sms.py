import gammu.smsd
import threading


class Sms(threading.Thread):
    modem = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.modem = gammu.smsd.SMSD('/etc/gammu-smsdrc')

    def send_sms(self, text, number):
        message = {
            'Text': text,
            'SMSC': {'Location': 1},
            'Number': number,
        }
        self.modem.InjectSMS([message])

    def stop(self):
        if self.modem is not None:
            self.modem = None
