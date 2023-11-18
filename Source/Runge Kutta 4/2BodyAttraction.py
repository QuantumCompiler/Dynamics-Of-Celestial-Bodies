from RK4 import *

# Coupled Force Equations
def CoupledBodies(t, massList, m1x, m1y, m1z, m2x, m2y, m2z, m1vx, m1vy, m1vz, m2vx, m2vy, m2vz):
    G = 6.67e-11
    r_x = m2x - m1x
    r_y = m2y - m1y
    r_z = m2z - m1z
    r_3 = (r_x**2 + r_y**2 + r_z**2)**1.5
    m1_vx = m1vx
    m1_vy = m1vy
    m1_vz = m1vz
    m2_vx = m2vx
    m2_vy = m2vy
    m2_vz = m2vz
    m1_ax = (G * massList[1] * r_x) / r_3
    m1_ay = (G * massList[1] * r_y) / r_3
    m1_az = (G * massList[1] * r_z) / r_3
    m2_ax = - (G * massList[0] * r_x) / r_3   
    m2_ay = - (G * massList[0] * r_y) / r_3   
    m2_az = - (G * massList[0] * r_z) / r_3   
    return m1_vx, m1_vy, m1_vz, m2_vx, m2_vy, m2_vz, m1_ax, m1_ay, m1_az, m2_ax, m2_ay, m2_az

sun = 1.989 * 10**30
earth = 5.972 * 10**24
AU = 1.5e11
daySec = 24 * 60 * 60
masses = [sun, earth]
ic = [[0,0,0],[1 * AU,0,0],[0,0,0],[0,29780,0]]
t0 = 0
tn = 365.25 * daySec
h = 1200

sunPos, earthPos, sunVel, earthVel, time = RK4TwoBody(CoupledBodies, masses, ic, t0, tn, h)

plt.plot(earthPos[0], earthPos[1], color = 'blue', label = 'Earth')
plt.plot(sunPos[0], sunPos[1], color = 'orange', label = 'Sun', linewidth = 5)
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Earth\'s Orbit Around The Sun')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()