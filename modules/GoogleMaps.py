class GoogleMaps:
    lat = '0.0'
    long = '0.0'

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def get_maps_url(self):
        """
        Returns a url to google maps with pin on the specified lat long co-ordinates
        :return:
        :rtype: str
        """
        return 'http://maps.google.com/maps?z=12&t=m&q=loc:' + str(self.lat) + '+' + str(self.long)
