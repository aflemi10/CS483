from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
ax.set_xlim(0,50)
ax.set_ylim(0,150)
ax.grid(True)

t = linspace(0, 500, 500)

plt.plot(t, t, 'r')         # Linear
plt.plot(t, t**2, 'b')      # Quadratic 
plt.plot(t, t**3, 'g')      # Cubic 
plt.plot(t,t*np.log(t),'y') # n*log(n)
plt.show()