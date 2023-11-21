from RK4 import *

# Constants
G = 6.67e-11

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