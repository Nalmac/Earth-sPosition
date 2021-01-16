import matplotlib.pyplot as plt
from Models.Earth import Earth
from Models.Sun import Sun
from Tools.EarthPositionCalculator import EarthPositionCalculator
import numpy as np

date_a = int(input("Input the oldest date"))
date_b = int(input("Input the latest date"))

earth_a = Earth(date_a)
earth_b = Earth(date_b)

calculator = EarthPositionCalculator(earth_a, earth_b)
earth_b.coordinates = calculator.locate()
print(earth_b.coordinates)

plt.quiver(earth_b.coordinates[0], earth_b.coordinates[1], scale=21)
plt.show()