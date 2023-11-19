from RK4 import *

# Constants
G = 6.67e-11
AU = 1.5e11
daySec = 24 * 60 * 60
sun = 1.989e30
earth = 5.972e24
moon = 7.348e22

def CoupledBodies(t, massList, m1x, m1y, m1z, m2x, m2y, m2z, m3x, m3y, m3z, m1vx, m1vy, m1vz, m2vx, m2vy, m2vz, m3vx, m3vy, m3vz):
    r12x = m2x - m1x
    r12y = m2y - m1y
    r12z = m2z - m1z
    r12_3 = pow(pow(r12x, 2) + pow(r12y, 2) + pow(r12z, 2), 1.5)
    r21x = m1x - m2x
    r21y = m1y - m2y
    r21z = m1z - m2z
    r21_3 = pow(pow(r21x, 2) + pow(r21y, 2) + pow(r21z, 2), 1.5)
    r13x = m3x - m1x
    r13y = m3y - m1y
    r13z = m3z - m1z
    r13_3 = pow(pow(r13x, 2) + pow(r13y, 2) + pow(r13z, 2), 1.5)
    r31x = m1x - m3x
    r31y = m1y - m3y
    r31z = m1z - m3z
    r31_3 = pow(pow(r31x, 2) + pow(r31y, 2) + pow(r31z, 2), 1.5)
    r23x = m3x - m2x
    r23y = m3y - m2y
    r23z = m3z - m2z
    r23_3 = pow(pow(r23x, 2) + pow(r23y, 2) + pow(r23z, 2), 1.5)
    r32x = m2x - m3x
    r32y = m2y - m3y
    r32z = m2z - m3z
    r32_3 = pow(pow(r32x, 2) + pow(r32y, 2) + pow(r32z, 2), 1.5)
    m1_ax = (G * massList[1] * r12x) / r12_3 + (G * massList[2] * r13x) / r13_3
    m1_ay = (G * massList[1] * r12y) / r12_3 + (G * massList[2] * r13y) / r13_3
    m1_az = (G * massList[1] * r12z) / r12_3 + (G * massList[2] * r13z) / r13_3
    m2_ax = (G * massList[0] * r21x) / r21_3 + (G * massList[2] * r23x) / r23_3
    m2_ay = (G * massList[0] * r21y) / r21_3 + (G * massList[2] * r23y) / r23_3
    m2_az = (G * massList[0] * r21z) / r21_3 + (G * massList[2] * r23z) / r23_3
    m3_ax = (G * massList[0] * r31x) / r31_3 + (G * massList[1] * r32x) / r32_3
    m3_ay = (G * massList[0] * r31y) / r31_3 + (G * massList[1] * r32y) / r32_3
    m3_az = (G * massList[0] * r31z) / r31_3 + (G * massList[1] * r32z) / r32_3
    return m1vx, m1vy, m1vz, m2vx, m2vy, m2vz, m3vx, m3vy, m3vz, m1_ax, m1_ay, m1_az, m2_ax, m2_ay, m2_az, m3_ax, m3_ay, m3_az


# Initial Conditions
masses = [sun, earth, moon]
ic = [
    [0, 0, 0],  # Sun position
    [AU, 0, 0],  # Earth position
    [AU + 3.844e8, 0, 0],  # Moon position
    [0, 0, 0],  # Sun velocity
    [0, 29780, 0],  # Earth velocity
    [0, 29780 + 1022, 0]  # Moon velocity
]
t0 = 0
tn = 365.25 * daySec
h = 1200

# 2D Plot

sunPos, earthPos, moonPos, sunVel, earthVel, moonVel = RK4ThreeBody(CoupledBodies, masses, ic, t0, tn, h)

plt.plot(sunPos[0], sunPos[1], color = 'orange', linewidth = '5', label = 'Sun')
plt.plot(earthPos[0], earthPos[1], color = 'blue', label = 'Earth')
plt.plot(moonPos[0], moonPos[1], color = 'grey', label = 'Moon')
plt.title('Earth Orbiting The Sun And The Moon Orbiting Earth')
plt.xlabel('Position In Meters')
plt.ylabel('Position In Meters')
plt.legend()
plt.show()

# 2D Animation

fig, ax = plt.subplots()
max_dist = max(np.max(np.abs(earthPos)), np.max(np.abs(moonPos))) * 1.1
ax.set_xlim(-max_dist, max_dist)
ax.set_ylim(-max_dist, max_dist)

sun, = ax.plot([], [], 'o', color='orange', markersize=8, label='Sun')
earth, = ax.plot([], [], 'o', color='blue', markersize=2, label='Earth')
moon, = ax.plot([], [], 'o', color='grey', markersize=1, label='Moon')
earthTrail, = ax.plot([], [], '-', color='blue', linewidth=1, alpha=0.5)
moonTrail, = ax.plot([], [], '-', color='grey', linewidth=1, alpha=0.5)

def init():
    sun.set_data([], [])
    earth.set_data([], [])
    moon.set_data([], [])
    earthTrail.set_data([], [])
    moonTrail.set_data([], [])
    return sun, earth, moon, earthTrail, moonTrail

def animate(i):
    sun.set_data([sunPos[0][i]], [sunPos[1][i]])
    earth.set_data([earthPos[0][i]], [earthPos[1][i]])
    moon.set_data([moonPos[0][i]], [moonPos[1][i]])
    earthTrail.set_data(earthPos[0][:i+1], earthPos[1][:i+1])
    moonTrail.set_data(moonPos[0][:i+1], moonPos[1][:i+1])
    return sun, earth, moon, earthTrail, moonTrail

ani = FuncAnimation(fig, animate, init_func=init, frames=len(earthPos[0]), interval=1e-5, blit=True, repeat=True)
ax.set_xlabel('Position In Meters')
ax.set_ylabel('Position In Meters')
ax.set_title("Sun-Earth-Moon System Simulation")
ax.legend()
plt.show()

# 3D Animation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
max_dist = max(np.max(np.abs(earthPos)), np.max(np.abs(moonPos))) * 1.1
ax.set_xlim([-max_dist, max_dist])
ax.set_ylim([-max_dist, max_dist])
ax.set_zlim([-max_dist, max_dist])

sun_plot, = ax.plot([], [], [], 'o', color='orange', markersize=8, label='Sun')
earth_plot, = ax.plot([], [], [], 'o', color='blue', markersize=2, label='Earth')
moon_plot, = ax.plot([], [], [], 'o', color='grey', markersize=1, label='Moon')
earthTrail, = ax.plot([], [], [], '-', color='blue', linewidth=1, alpha=0.5)
moonTrail, = ax.plot([], [], [], '-', color='grey', linewidth=1, alpha=0.5)

def init():
    sun_plot.set_data([], [])
    sun_plot.set_3d_properties([])
    earth_plot.set_data([], [])
    earth_plot.set_3d_properties([])
    earthTrail.set_data([], [])
    moon_plot.set_data([], [])
    moon_plot.set_3d_properties([])
    moonTrail.set_data([], [])
    return sun_plot, earth_plot, moon_plot, earthTrail, moonTrail

def animate(i):
    sun_plot.set_data([sunPos[0][i]], [sunPos[1][i]])
    sun_plot.set_3d_properties([sunPos[2][i]])
    earth_plot.set_data([earthPos[0][i]], [earthPos[1][i]])
    earth_plot.set_3d_properties([earthPos[2][i]])
    earthTrail.set_data(earthPos[0][:i+1], earthPos[1][:i+1])
    earthTrail.set_3d_properties(earthPos[2][:i+1])
    moon_plot.set_data([moonPos[0][i]], [moonPos[1][i]])
    moon_plot.set_3d_properties([moonPos[2][i]])
    moonTrail.set_data(moonPos[0][:i+1], moonPos[1][:i+1])
    moonTrail.set_3d_properties(moonPos[2][:i+1])
    return sun_plot, earth_plot, moon_plot, earthTrail, moonTrail

ani = FuncAnimation(fig, animate, init_func=init, frames=len(earthPos[0]), interval=1e-5, blit=True, repeat=True)
ax.set_xlabel('Position In Meters')
ax.set_ylabel('Position In Meters')
ax.set_zlabel('Position In Meters')
ax.set_title("3D Animation of Sun-Earth-Moon System")
ax.legend()
plt.show()