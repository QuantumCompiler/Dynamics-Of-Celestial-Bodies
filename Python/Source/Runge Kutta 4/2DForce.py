from RK4 import *

# Newtonian Force Attraction
def Newton(t,a,b):
    r = 6.3781*10**6 + a
    G = 6.67408*10**-11
    M = 5.972*10**24
    da_dt = b
    db_dt = -1 * (G*M / r**2)
    return da_dt, db_dt