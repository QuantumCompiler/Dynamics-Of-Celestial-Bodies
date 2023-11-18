from RK4 import *

# Newtonian Force Attraction
def Newton(t,a,b):
    r = 6.3781*10**6 + a
    G = 6.67408*10**-11
    M = 5.972*10**24
    da_dt = b
    db_dt = -1 * (G*M / r**2)
    return da_dt, db_dt

y0 = 100
v0 = 0
t0 = 0
tn = 4.52
h = 0.1

y_values, v_values, t_values = RK42nd(Newton, y0, v0, t0, tn, h)

plt.plot(t_values, y_values)
plt.title(f"Position Versus Time W/ $y_{0} = 100$, $y'_{0} = 0$")
plt.xlabel(f"Time In Seconds")
plt.ylabel(f"Position In Meters")
plt.show()