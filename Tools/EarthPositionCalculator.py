from Models.Earth import Earth
from math import cos, sin

class EarthPositionCalculator():
    def __init__(self, earth_a, earth_b):
        """
        This object will do all the calculation we need to fill the coordinates of our Earth object.
        """
        self.earth_b = earth_b if isinstance(earth_b, Earth) else Earth(0)
        self.date = earth_b.date - earth_a.date
        self.sun_distance = 1.496 * 10**8
    
    def locate(self):
        coordinates = [
            cos(self.earth_b.angular_speed * self.date) * self.sun_distance,
            sin(self.earth_b.angular_speed * self.date) * self.sun_distance,
            0
        ]

        return coordinates