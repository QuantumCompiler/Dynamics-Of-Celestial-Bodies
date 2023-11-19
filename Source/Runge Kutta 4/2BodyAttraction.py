from RK4 import *

# Constants
G = 6.67e-11
AU = 1.5e11
daySec = 24 * 60 * 60
sun = 1.989 * 10**30
earth = 5.972 * 10**24

# Coupled Force Equations
def CoupledBodies(t, massList, m1x, m1y, m1z, m2x, m2y, m2z, m1vx, m1vy, m1vz, m2vx, m2vy, m2vz):
    r12_x = m1x - m2x
    r12_y = m1y - m2y
    r12_z = m1z - m2z
    r12_3 = pow(pow(r12_x, 2) + pow(r12_y, 2) + pow(r12_z, 2), 1.5)
    r21_x = m2x - m1x
    r21_y = m2y - m1y
    r21_z = m2z - m1z
    r21_3 = pow(pow(r21_x, 2) + pow(r21_y, 2) + pow(r21_z, 2), 1.5)
    m1_ax = (G * massList[1] * r21_x) / r21_3
    m1_ay = (G * massList[1] * r21_y) / r21_3
    m1_az = (G * massList[1] * r21_z) / r21_3
    m2_ax = (G * massList[0] * r12_x) / r12_3
    m2_ay = (G * massList[0] * r12_y) / r12_3
    m2_az = (G * massList[0] * r12_z) / r12_3
    return m1vx, m1vy, m1vz, m2vx, m2vy, m2vz, m1_ax, m1_ay, m1_az, m2_ax, m2_ay, m2_az

# Initial Conditions
masses = [sun, earth]
ic = [[0,0,0],[1 * AU,0,0],[0,0,0],[0,29780,0]]
t0 = 0
tn = 365.25 * daySec
h = 1200

# 2D Plot

sunPos, earthPos, sunVel, earthVel, time = RK4TwoBody(CoupledBodies, masses, ic, t0, tn, h)

plt.plot(sunPos[0], sunPos[1], color = 'orange', label = 'Sun', linewidth = 5)
plt.plot(earthPos[0], earthPos[1], color = 'blue', label = 'Earth')
plt.xlabel('Position In Meters')
plt.ylabel('Position In Meters')
plt.title('Sun-Earth Orbit 2D Plot')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

# 2D Animation

sunPos, earthPos, sunVel, earthVel, time = RK4TwoBody(CoupledBodies, masses, ic, t0, tn, h)

fig, ax = plt.subplots()
ax.set_xlim(-1.5*AU, 1.5*AU)
ax.set_ylim(-1.5*AU, 1.5*AU)

sun, = plt.plot([], [], 'o', color='orange', markersize=8, label='Sun')
earth, = plt.plot([], [], 'o-', color='blue', markersize=2, label='Earth')
earthTrail, = ax.plot([], [], '-', color='blue', linewidth=1, alpha=0.5)

def init():
    sun.set_data([], [])
    earth.set_data([], [])
    earthTrail.set_data([], [])
    return sun, earth, earthTrail

def animate(i):
    sun.set_data([sunPos[0][i]], [sunPos[1][i]])
    earth.set_data([earthPos[0][i]], [earthPos[1][i]])
    earthTrail.set_data(earthPos[0][:i+1], earthPos[1][:i+1])
    return sun, earth, earthTrail

ani = FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=1e-5, blit=True, repeat=True)
plt.xlabel('Position In Meters')
plt.ylabel('Position In Meters')
plt.title("Sun-Earth Orbit 2D Simulation")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()

# 3D Plot

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sunPos[0], sunPos[1], sunPos[2], color='orange', linewidth=5, label='Sun')
ax.plot(earthPos[0], earthPos[1], earthPos[2], color='blue', linewidth=2, label='Earth')
ax.set_xlabel('Position In Meters')
ax.set_ylabel('Position In Meters')
ax.set_zlabel('Position In Meters')
ax.set_title('Sun-Earth Orbit 3D Plot')
ax.legend()
plt.show()

# 3D Animation

sunPos, earthPos, sunVel, earthVel, time = RK4TwoBody(CoupledBodies, masses, ic, t0, tn, h)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.5*AU, 1.5*AU)
ax.set_ylim(-1.5*AU, 1.5*AU)
ax.set_zlim(-1.5*AU, 1.5*AU)

sun, = ax.plot([], [], [], 'o', color='orange', markersize=8, label='Sun')
earth, = ax.plot([], [], [], 'o', color='blue', markersize=2, label='Earth')
earthTrail, = ax.plot([], [], [], '-', color='blue', linewidth=1, alpha=0.5)

def init():
    sun.set_data([], [])
    sun.set_3d_properties([])
    earth.set_data([], [])
    earth.set_3d_properties([])
    earthTrail.set_data([], [])
    earthTrail.set_3d_properties([])
    return sun, earth, earthTrail

def animate(i):
    sun.set_data([sunPos[0][i]], [sunPos[1][i]])
    sun.set_3d_properties([sunPos[2][i]])
    earth.set_data([earthPos[0][i]], [earthPos[1][i]])
    earth.set_3d_properties([earthPos[2][i]])
    earthTrail.set_data(earthPos[0][:i+1], earthPos[1][:i+1])
    earthTrail.set_3d_properties(earthPos[2][:i+1])
    return sun, earth, earthTrail

ani = FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=1e-5, blit=True, repeat=True)
ax.set_xlabel('Position In Meters')
ax.set_ylabel('Position In Meters')
ax.set_zlabel('Position In Meters')
plt.title("Sun-Earth Orbit 3D Simulation")
plt.legend()
plt.grid(True)
plt.show()