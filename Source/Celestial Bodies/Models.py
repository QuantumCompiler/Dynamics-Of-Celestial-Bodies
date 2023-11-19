# Imports
from RK4 import *

# Earth2DForceModel - Model for simulating motion of body in free fall on earth
# Input:
#   t - Time variable, not used directly in this model
#   y - Height of object above earth
#   v - Velocity of object
# Algorithm:
#   * Calculate the distance of the object from the center of the Earth
#   * Create differential equations
#   * Return differential equations
# Output:
#   dy_dt - Velocity of object
#   dv_dt - Acceleration of object
def Earth2DForceModel(t,y,v):
    # Height of object
    R_earth += y
    # Differential equations
    dy_dt = v # Velocity
    dv_dt = - (G * M_earth / pow(R_earth, 2)) # Acceleration
    return dy_dt, dv_dt

# TwoCoupledBodies - Model for two bodies interacting in space
# Input:
#   t - Time variable, not used directly in this model
#   massList - Array of masses in system
#   m1x - Position of mass 1 in x
#   m1y - Position of mass 1 in y
#   m1z - Position of mass 1 in z
#   m2x - Position of mass 2 in x
#   m2y - Position of mass 2 in y
#   m2z - Position of mass 2 in z
#   m1vx - Velocity of mass 1 in x
#   m1vy - Velocity of mass 1 in y
#   m1vz - Velocity of mass 1 in z
#   m2vx - Velocity of mass 2 in x
#   m2vy - Velocity of mass 2 in y
#   m2vz - Velocity of mass 2 in z
# Algorithm:
#   * Calculate the distances from mass 1 to mass 2
#   * Calculate the distances from mass 2 to mass 1
#   * Calculate the accelerations of mass 1
#   * Calculate the accelerations of mass 2
#   * Return the updated values of each parameter
# Output:
#   m1vx - Velocity of mass 1 in x
#   m1vy - Velocity of mass 1 in y
#   m1vz - Velocity of mass 1 in z
#   m2vx - Velocity of mass 2 in x
#   m2vy - Velocity of mass 2 in y
#   m2vz - Velocity of mass 2 in z
#   m1ax - Acceleration of mass 1 in x
#   m1ay - Acceleration of mass 1 in y
#   m1az - Acceleration of mass 1 in z
#   m2ax - Acceleration of mass 2 in x
#   m2ay - Acceleration of mass 2 in y
#   m2az - Acceleration of mass 2 in z
def TwoCoupledBodies(t, massList, m1x, m1y, m1z, m2x, m2y, m2z, m1vx, m1vy, m1vz, m2vx, m2vy, m2vz):
    # Distances from mass 1 to mass 2
    r12x = m1x - m2x
    r12y = m1y - m2y
    r12z = m1z - m2z
    R12 = pow(pow(r12x, 2) + pow(r12y, 2) + pow(r12z, 2), 1.5)
    # Distances from mass 2 to mass 1
    r21x = m2x - m1x
    r21y = m2y - m1y
    r21z = m2z - m1z
    R21 = pow(pow(r21x, 2) + pow(r21y, 2) + pow(r21z, 2), 1.5)
    # Accelerations of mass 1
    m1ax = (G * massList[1] * r21x) / R21
    m1ay = (G * massList[1] * r21y) / R21
    m1az = (G * massList[1] * r21z) / R21
    # Accelerations of mass 2
    m2ax = (G * massList[0] * r12x) / R12
    m2ay = (G * massList[0] * r12y) / R12
    m2az = (G * massList[0] * r12z) / R12
    return m1vx, m1vy, m1vz, m2vx, m2vy, m2vz, m1ax, m1ay, m1az, m2ax, m2ay, m2az