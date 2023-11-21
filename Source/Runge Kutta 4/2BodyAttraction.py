from RK4 import *

# Constants
G = 6.67e-11

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