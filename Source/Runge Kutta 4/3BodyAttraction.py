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
h = daySec / 5

# 2D Plot

sunPos, earthPos, moonPos, sunVel, earthVel, moonVel = RK4ThreeBody(CoupledBodies, masses, ic, t0, tn, h)

plt.plot(sunPos[0], sunPos[1], color = 'orange', linewidth = '5', label = 'Sun')
plt.plot(earthPos[0], earthPos[1], color = 'blue', label = 'Earth')
plt.plot(moonPos[0], moonPos[1], color = 'grey', label = 'Moon')
plt.title('Sun-Earth-Moon Orbit\'s 2D Plot')
plt.xlabel('Position (m)')
plt.ylabel('Position (m)')
plt.legend()
plt.savefig('Sun-Earth-Moon Orbit\'s 2D Plot.png', dpi = 500)
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
ax.set_xlabel('Position (m)')
ax.set_ylabel('Position (m)')
ax.set_title('Sun-Earth-Moon Orbit\'s 2D Simulation')
ax.legend()
plt.show()
ani.save('Sun-Earth-Moon Orbit\'s 2D Simulation.mp4', writer='ffmpeg', fps= len(earthPos[0]) // 10)

# 3D Plot

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sunPos[0], sunPos[1], sunPos[2], color='orange', linewidth=5, label='Sun')
ax.plot(earthPos[0], earthPos[1], earthPos[2], color='blue', linewidth=2, label='Earth')
ax.plot(moonPos[0], moonPos[1], moonPos[2], color='grey', linewidth=1, label='Moon')
ax.set_xlabel('Position (m)')
ax.set_ylabel('Position (m)')
ax.set_zlabel('Position (m)')
ax.set_title('Sun-Earth-Moon Orbit\'s 3D Plot')
ax.legend()
plt.savefig('Sun-Earth-Moon Orbit\'s 3D Plot.png', dpi = 500)
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
ax.set_xlabel('Position (m)')
ax.set_ylabel('Position (m)')
ax.set_zlabel('Position (m)')
ax.set_title('Sun-Earth-Moon Orbit\'s 3D Simulation')
ax.legend()
plt.show()
ani.save('Sun-Earth-Moon Orbit\'s 3D Simulation.mp4', writer='ffmpeg', fps= len(earthPos[0]) // 10)

# Random Bodies 2D Plot

mass1 = 1.989e30
mass2 = 5.972e28
mass3 = 7.348e26

# Initial Conditions
masses = [mass1, mass2, mass3]
ic = [
    [0, 0, 0],  # Mass 1 position
    [2*AU, 0.5*AU, 0],  # Mass 2 position
    [4*AU, -0.5*AU, 0],  # Mass 3 position
    [2000, 1000, 500],  # Mass 1 velocity
    [0, 15000, 0],  # Mass 2 velocity
    [0, -10000, 0]  # Mass 3 velocity
]
t0 = 0
tn = 10 * 365.25 * daySec
h = daySec

m1Pos, m2Pos, m3Pos, m1Vel, m2Vel, m3Vel = RK4ThreeBody(CoupledBodies, masses, ic, t0, tn, h)

plt.plot(m1Pos[0], m1Pos[1], color = 'orange', label = 'Mass 1')
plt.plot(m2Pos[0], m2Pos[1], color = 'blue', label = 'Mass 2')
plt.plot(m3Pos[0], m3Pos[1], color = 'red', label = 'Mass 3')
plt.title('3 Celestial Bodies Orbit\'s 2D Plot')
plt.xlabel('Position (m)')
plt.ylabel('Position (m)')
plt.legend()
plt.savefig('3 Celestial Bodies Orbit\'s 2D Plot.png', dpi = 500)
plt.show()

# Random Bodies 2D Animation

fig, ax = plt.subplots()
Mass1, = ax.plot([], [], 'o', color='orange', markersize=8, label='Mass 1')
Mass2, = ax.plot([], [], 'o', color='blue', markersize=2, label='Mass 2')
Mass3, = ax.plot([], [], 'o', color='red', markersize=1, label='Mass 3')
Mass1Trail, = ax.plot([], [], '-', color='orange', linewidth=1, alpha=0.5)
Mass2Trail, = ax.plot([], [], '-', color='blue', linewidth=1, alpha=0.5)
Mass3Trail, = ax.plot([], [], '-', color='red', linewidth=1, alpha=0.5)

def init():
    Mass1.set_data([], [])
    Mass2.set_data([], [])
    Mass3.set_data([], [])
    Mass1Trail.set_data([], [])
    Mass2Trail.set_data([], [])
    Mass3Trail.set_data([], [])
    return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail

def animate(i):
    Mass1.set_data([m1Pos[0][i]], [m1Pos[1][i]])
    Mass2.set_data([m2Pos[0][i]], [m2Pos[1][i]])
    Mass3.set_data([m3Pos[0][i]], [m3Pos[1][i]])
    Mass1Trail.set_data(m1Pos[0][:i+1], m1Pos[1][:i+1])
    Mass2Trail.set_data(m2Pos[0][:i+1], m2Pos[1][:i+1])
    Mass3Trail.set_data(m3Pos[0][:i+1], m3Pos[1][:i+1])
    return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail

ani = FuncAnimation(fig, animate, init_func=init, frames=len(m2Pos[0]), interval=1e-5, blit=True, repeat=True)
ax.set_xlabel('Position (m)')
ax.set_ylabel('Position (m)')
ax.set_title('3 Celestial Bodies Orbit\'s 2D Simulation')
ax.set_xlim(-1*AU, 8*AU)
ax.set_ylim(-5*AU, 8*AU)
ax.legend()
plt.show()
ani.save('3 Celestial Bodies Orbit\'s 2D Simulation.mp4', writer='ffmpeg', fps= len(m1Pos[0]) // 10)

# Random Bodies 3D Plot

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(m1Pos[0], m1Pos[1], m1Pos[2], color='orange', linewidth=1, label='Mass 1')
ax.plot(m2Pos[0], m2Pos[1], m2Pos[2], color='blue', linewidth=1, label='Mass 2')
ax.plot(m3Pos[0], m3Pos[1], m3Pos[2], color='red', linewidth=1, label='Mass 3')
ax.set_xlabel('Position (m)')
ax.set_ylabel('Position (m)')
ax.set_zlabel('Position (m)')
ax.set_title('3 Celestial Bodies Orbit\'s 3D Plot')
ax.legend()
plt.savefig('3 Celestial Bodies Orbit\'s 3D Plot.png', dpi = 500)
plt.show()

# Random Bodies 3D Animation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-AU, 8*AU)
ax.set_ylim(-5*AU, 8*AU)
ax.set_zlim(0, 1.5*AU)

Mass1, = ax.plot([], [], [], 'o', color='orange', markersize=8, label='Mass 1')
Mass2, = ax.plot([], [], [], 'o', color='blue', markersize=2, label='Mass 2')
Mass3, = ax.plot([], [], [], 'o', color='red', markersize=1, label='Mass 3')
Mass1Trail, = ax.plot([], [], [], '-', color='orange', linewidth=1, alpha=0.5)
Mass2Trail, = ax.plot([], [], [], '-', color='blue', linewidth=1, alpha=0.5)
Mass3Trail, = ax.plot([], [], [], '-', color='red', linewidth=1, alpha=0.5)

def init():
    Mass1.set_data([], [])
    Mass1.set_3d_properties([])
    Mass1Trail.set_data([], [])
    Mass2.set_data([], [])
    Mass2.set_3d_properties([])
    Mass2Trail.set_data([], [])
    Mass3.set_data([], [])
    Mass3.set_3d_properties([])
    Mass3Trail.set_data([], [])
    return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail

def animate(i):
    Mass1.set_data([m1Pos[0][i]], [m1Pos[1][i]])
    Mass1.set_3d_properties([m1Pos[2][i]])
    Mass1Trail.set_data(m1Pos[0][:i+1], m1Pos[1][:i+1])
    Mass1Trail.set_3d_properties(m1Pos[2][:i+1])
    Mass2.set_data([m2Pos[0][i]], [m2Pos[1][i]])
    Mass2.set_3d_properties([m2Pos[2][i]])
    Mass2Trail.set_data(m2Pos[0][:i+1], m2Pos[1][:i+1])
    Mass2Trail.set_3d_properties(m2Pos[2][:i+1])
    Mass3.set_data([m3Pos[0][i]], [m3Pos[1][i]])
    Mass3.set_3d_properties([m3Pos[2][i]])
    Mass3Trail.set_data(m3Pos[0][:i+1], m3Pos[1][:i+1])
    Mass3Trail.set_3d_properties(m3Pos[2][:i+1])
    return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail

ani = FuncAnimation(fig, animate, init_func=init, frames=len(m2Pos[0]), interval=1e-5, blit=True, repeat=True)
ax.set_xlabel('Position (m)')
ax.set_ylabel('Position (m)')
ax.set_zlabel('Position (m)')
ax.set_title('3 Celestial Bodies Orbit\'s 3D Simulation')
ax.legend()
plt.show()
ani.save('3 Celestial Bodies Orbit\'s 3D Simulation.mp4', writer='ffmpeg', fps= len(m1Pos[0]) // 10)