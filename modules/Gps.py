import gps
import threading

class Gps(threading.Thread):
    currentLat = '0.0'
    currentLong = '0.0'
    gpsd = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.gpsd = gps.gps("localhost", "2947")
        self.gpsd.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        # pprint.pprint(self.gpsd)
        self.running = True  # setting the thread running to true
        self.run()

    def run(self):
        while self.running:
            try:
                report = self.gpsd.next()

                if report['class'] == 'TPV':
                    if hasattr(report, 'lat') and report['lat'] != '0.0':
                        self.currentLat = report['lat']
                    if hasattr(report, 'lon') and report['lon'] != '0.0':
                        self.currentLong = report['lon']

                if self.currentLat != '0.0' and self.currentLong != '0.0':
                    self.gpsd = None
                    self.running = False

            except KeyError:
                pass

            except KeyboardInterrupt:
                quit()

            except StopIteration:
                self.gpsd = None

    def getCurrentLocation(self):
        return {'lat': self.currentLat, 'long': self.currentLong}

    def stop(self):
        if self.gpsd is not None:
            self.gpsd = None
