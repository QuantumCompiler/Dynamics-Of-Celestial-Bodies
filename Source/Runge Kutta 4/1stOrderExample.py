from RK4 import *

# Initial conditions and parameters
y0 = 0.0
t0 = 0.0
tn = 100.0
h = 0.1

def Sine(y,t):
    return np.sin(t)

y_values, t_values = RK41st(Sine, y0, t0, tn, h)

# Plot the results
plt.plot(t_values, y_values, label='RK4 Solution')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.legend()
plt.show()