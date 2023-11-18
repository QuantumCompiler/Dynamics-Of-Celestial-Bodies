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

# Initial Conditions
sun = 1.989 * 10**30
earth = 5.972 * 10**24
AU = 1.5e11
daySec = 24 * 60 * 60
masses = [sun, earth]
ic = [[0,0,0],[1 * AU,0,0],[0,0,0],[0,29780,0]]
t0 = 0
tn = 365.25 * daySec
h = 1200

# 2D Plot

# sunPos, earthPos, sunVel, earthVel, time = RK4TwoBody(CoupledBodies, masses, ic, t0, tn, h)

# plt.plot(earthPos[0], earthPos[1], color = 'blue', label = 'Earth')
# plt.plot(sunPos[0], sunPos[1], color = 'orange', label = 'Sun', linewidth = 5)
# plt.xlabel('X Position (m)')
# plt.ylabel('Y Position (m)')
# plt.title('Earth\'s Orbit Around The Sun')
# plt.legend()
# plt.grid(True)
# plt.axis('equal')
# plt.show()

# 2D Animation

# sunPos, earthPos, sunVel, earthVel, time = RK4TwoBody(CoupledBodies, masses, ic, t0, tn, h)

# fig, ax = plt.subplots()
# ax.set_xlim(-1.5*AU, 1.5*AU)
# ax.set_ylim(-1.5*AU, 1.5*AU)

# earth_line, = plt.plot([], [], 'o-', color='blue', markersize=3, label='Earth')
# sun, = plt.plot([], [], 'o', color='orange', markersize=6, label='Sun')

# def init():
#     earth_line.set_data([], [])
#     sun.set_data([], [])
#     return earth_line, sun

# def animate(i):
#     xearth, yearth = earth_line.get_data()
#     xsun, ysun = sun.get_data()
#     xearth = np.append(xearth, earthPos[0][i])
#     xsun = np.append(xsun, sunPos[0][i])
#     yearth = np.append(yearth, earthPos[1][i])
#     ysun = np.append(ysun, sunPos[1][i])
#     earth_line.set_data(xearth, yearth)
#     sun.set_data(xsun, ysun)
#     return earth_line, sun

# ani = FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=1e-5, blit=True)
# plt.xlabel('X Position (m)')
# plt.ylabel('Y Position (m)')
# plt.title("Earth's Orbit Around The Sun")
# plt.legend()
# plt.grid(True)
# plt.axis('equal')
# plt.show()

# 3D Animation

sunPos, earthPos, sunVel, earthVel, time = RK4TwoBody(CoupledBodies, masses, ic, t0, tn, h)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.5*AU, 1.5*AU)
ax.set_ylim(-1.5*AU, 1.5*AU)
ax.set_zlim(-1.5*AU, 1.5*AU)

earth_line, = ax.plot([], [], [], 'o-', color='blue', markersize=1, label='Earth')
sun, = ax.plot([], [], [], 'o', color='orange', markersize=6, label='Sun')

def init():
    earth_line.set_data([], [])
    earth_line.set_3d_properties([])
    sun.set_data([], [])
    sun.set_3d_properties([])
    return earth_line, sun

def animate(i):
    earth_line.set_data(earthPos[0][:i], earthPos[1][:i])
    earth_line.set_3d_properties(earthPos[2][:i])
    sun.set_data(sunPos[0][:i], sunPos[1][:i])
    sun.set_3d_properties(sunPos[2][:i])
    return earth_line, sun

ani = FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=1e-5, blit=True)

ax.set_xlabel('X Position (m)')
ax.set_ylabel('Y Position (m)')
ax.set_zlabel('Z Position (m)')
plt.title("Earth's Orbit Around The Sun")
plt.legend()
plt.grid(True)
plt.show()