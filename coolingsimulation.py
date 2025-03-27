#Joshua Simpson
#Newtons law of cooling to model computer temperature

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Newtons Law of Cooling
#T = current temperature
#t = time (not used directly, but needed by odeint)
#k = cooling constant
#s = surrounding temperature
#It returns how fast the temperature is changing (dTdt).
#Defining ODE
def model (T,t,k,s):
    dTdt = -k*(T-s)
    return dTdt

#perameters
k = 0.5 #This sets k, the cooling rate. Higher k = faster cooling.
T = 80 #This is the starting temperature of the computer's liquid cooling system.
s = [50, 60, 70, 80, 90] #This is a list of surrounding temperatures you want to test against — like simulating different room temps.

t = np.linspace(0, 10)#This creates an array of time values from 0 to 10 seconds. These will be used to see how the temp changes over time.

for x in s: #this is a loop, goes through each value of list(s)
    solution = odeint(model, T, t, args=(k, x))
    plt.plot(t, solution, label="Surrounding Temp: " + str(x))

plt.xlabel('Time (Seconds)')
plt.ylabel('Temperature (Celsius)')
plt.title('Computer Cooling Over Time')
plt.legend()
plt.grid(True)
plt.show()