from numpy import *
import numpy as np
import math
import matplotlib.pyplot as plt
import time

adjustmentVal = 15;

fig, ax = plt.subplots()
ax.set_xlim(0,50)
ax.set_ylim(0,150)
ax.grid(True)
t = linspace(0, 150, 150)

input=[]
functionTimes=[]
for x in range(150):
    start = time.time()
    
    # Linear function 
    #for y in range(x):
    #    print(x)
    
    #Quadratic function
    for y in range(x):
        for z in range(x):
            print(x)

    
    functionTimes.append((time.time()-start))

base = 1/(functionTimes[0])
print(f'base: {base}')
print(f'oof: {functionTimes[0]*base}')
for x in range(len(functionTimes)):
    functionTimes[x] = functionTimes[x]*(base/adjustmentVal)
print(functionTimes)

plt.plot(t, t, 'c')          # Linear
plt.plot(t, t**2, 'g')       # Quadratic 
plt.plot(t, t**3, 'b')       # Cubic 
plt.plot(t, t*np.log(t),'y') # n*log(n)
plt.plot(t, 2**t,'r')            # 2^k 
plt.plot(t, functionTimes,'ro')
plt.show()