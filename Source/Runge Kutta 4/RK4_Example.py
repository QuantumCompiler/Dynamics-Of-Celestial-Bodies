import RK4 as rk4
import matplotlib.pyplot as plt

# Initial conditions and parameters
y0 = 0.0
t0 = 0.0
tn = 100.0
h = 0.1

def Sine(y,t):
    return rk4.np.sin(t)

y_values, t_values = rk4.RK41st(Sine, y0, t0, tn, h)

# Plot the results
plt.plot(t_values, y_values, label='RK4 Solution')
# plt.plot(t_values, -rk4.np.cos(t_values) + 1, label='Analytical Solution')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.legend()
plt.show()