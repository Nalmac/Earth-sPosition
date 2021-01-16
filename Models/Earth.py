class Earth():
    def __init__(self, date):
        """
        This object represents the Earth at any given date.
        """
        self.date = date
        self.mass = 5.9722 * 10**24 #In kilograms
        self.angular_speed = 2 * 10**(-7)
        self.coordinates = [] #In cartesian coordinates
        self.e = 0.06
    