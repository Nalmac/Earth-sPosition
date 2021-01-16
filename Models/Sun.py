class Sun():
    def __init__(self, date):
        """
        This object represents the sun at any given date.
        """
        self.date = date
        self.mass = 1.9885 * 10**30 #Still in kilograms
        self.coordinates = [] #Hopefully one day this will be filled