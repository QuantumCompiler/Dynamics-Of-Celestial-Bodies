############### Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

############### Force Attraction in Y-Direction
def model(parameters,t):
    y,vy=parameters
    r=6.3781*10**6+y
    G=6.67408*10**-11
    M=5.972*10**24
    A=-(G*M/r**2)
    out=[vy,A]
    return out

############### Initial Velocity Condition
ic=[100,0]

############### Time Points
t=np.linspace(0,4.52,1000)
    
############### Solve ODE
y=odeint(model,ic,t)

############### Plot
plt.plot(t,y[:,0])
plt.title('Position vs. Time')
plt.xlabel('Time in Seconds (t)')
plt.ylabel('Vertical Position in Meters (m)')
plt.show()

plt.plot(t,y[:,1])
plt.show()