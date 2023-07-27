from matplotlib import pyplot
from numpy import linspace

u = 5
G = 9.81
t = linspace(0, 1, 1001)

h = u*t-0.5*G*t**2

pyplot.plot(t, h)
pyplot.xlabel("Time")
pyplot.ylabel("Height")
pyplot.show()