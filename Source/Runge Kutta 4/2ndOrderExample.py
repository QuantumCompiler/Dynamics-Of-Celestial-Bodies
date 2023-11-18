from RK4 import *
import matplotlib.pyplot as plt

# dy^2/dt^2 = -9.81
def Grav(t,x,v):
    da_dx = v
    db_dx = -9.81
    return da_dx, db_dx

x0 = 100
v0 = 100
t0 = 0
tn = 20
h = 0.1

x_values, v_values, time_values = RK42nd(Grav, x0, v0, t0, tn, h)

plt.plot(time_values, x_values)
plt.show()

# dy^2/dx^2 = sin(x) - xy
def Abstract(x,a,b):
    da_dx = b
    db_dx = np.sin(x) - x * a
    return da_dx, db_dx

a0 = 0
b0 = 0
x0 = 0
xn = 10
h = 0.1

a_values, b_values, x_values = RK42nd(Abstract, a0, b0, x0, xn, h)

plt.plot(x_values, a_values)
plt.show()