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
#   dydt - Velocity of object
#   dzdt - Acceleration of object
def Earth2DForceModel(t,y,v):
    # Height of object
    height = REARTH + y
    # Differential equations
    dydt = v # Velocity
    dzdt = - (G * MEARTH / pow(height, 2)) # Acceleration
    return dydt, dzdt

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

# ThreeCoupledBodies - Model for three bodies interacting in space
# Input:
#   t - Time variable, not used directly in this model
#   massList - Array of masses in system
#   m1x - Position of mass 1 in x
#   m1y - Position of mass 1 in y
#   m1z - Position of mass 1 in z
#   m2x - Position of mass 2 in x
#   m2y - Position of mass 2 in y
#   m2z - Position of mass 2 in z
#   m3x - Position of mass 3 in x
#   m3y - Position of mass 3 in y
#   m3z - Position of mass 3 in z
#   m1vx - Velocity of mass 1 in x
#   m1vy - Velocity of mass 1 in y
#   m1vz - Velocity of mass 1 in z
#   m2vx - Velocity of mass 2 in x
#   m2vy - Velocity of mass 2 in y
#   m2vz - Velocity of mass 2 in z
#   m3vx - Velocity of mass 3 in x
#   m3vy - Velocity of mass 3 in y
#   m3vz - Velocity of mass 3 in z
# Algorithm:
#   * Calculate the distances from mass 1 to mass 2
#   * Calculate the distances from mass 1 to mass 3
#   * Calculate the distances from mass 2 to mass 1
#   * Calculate the distances from mass 2 to mass 3
#   * Calculate the distances from mass 3 to mass 1
#   * Calculate the accelerations of mass 1
#   * Calculate the accelerations of mass 2
#   * Calculate the accelerations of mass 3
#   * Return the updated values of each parameter
# Output:
#   m1vx - Velocity of mass 1 in x
#   m1vy - Velocity of mass 1 in y
#   m1vz - Velocity of mass 1 in z
#   m2vx - Velocity of mass 2 in x
#   m2vy - Velocity of mass 2 in y
#   m2vz - Velocity of mass 2 in z
#   m3vx - Velocity of mass 3 in x
#   m3vy - Velocity of mass 3 in y
#   m3vz - Velocity of mass 3 in z
#   m1ax - Acceleration of mass 1 in x
#   m1ay - Acceleration of mass 1 in y
#   m1az - Acceleration of mass 1 in z
#   m2ax - Acceleration of mass 2 in x
#   m2ay - Acceleration of mass 2 in y
#   m2az - Acceleration of mass 2 in z
#   m3ax - Acceleration of mass 3 in x
#   m3ay - Acceleration of mass 3 in y
#   m3az - Acceleration of mass 3 in z
def ThreeCoupledBodies(t, massList, m1x, m1y, m1z, m2x, m2y, m2z, m3x, m3y, m3z, m1vx, m1vy, m1vz, m2vx, m2vy, m2vz, m3vx, m3vy, m3vz):
    # Distances from mass 1 to mass 2
    r12x = m2x - m1x
    r12y = m2y - m1y
    r12z = m2z - m1z
    r123 = pow(pow(r12x, 2) + pow(r12y, 2) + pow(r12z, 2), 1.5)
    # Distances from mass 1 to mass 3
    r13x = m3x - m1x
    r13y = m3y - m1y
    r13z = m3z - m1z
    r133 = pow(pow(r13x, 2) + pow(r13y, 2) + pow(r13z, 2), 1.5)
    # Distances from mass 2 to mass 1
    r21x = m1x - m2x
    r21y = m1y - m2y
    r21z = m1z - m2z
    r213 = pow(pow(r21x, 2) + pow(r21y, 2) + pow(r21z, 2), 1.5)
    # Distances from mass 2 to mass 3
    r23x = m3x - m2x
    r23y = m3y - m2y
    r23z = m3z - m2z
    r233 = pow(pow(r23x, 2) + pow(r23y, 2) + pow(r23z, 2), 1.5)
    # Distances from mass 3 to mass 1
    r31x = m1x - m3x
    r31y = m1y - m3y
    r31z = m1z - m3z
    r313 = pow(pow(r31x, 2) + pow(r31y, 2) + pow(r31z, 2), 1.5)
    # Distances from mass 3 to mass 2
    r32x = m2x - m3x
    r32y = m2y - m3y
    r32z = m2z - m3z
    r323 = pow(pow(r32x, 2) + pow(r32y, 2) + pow(r32z, 2), 1.5)
    # Accelerations of mass 1
    m1ax = (G * massList[1] * r12x) / r123 + (G * massList[2] * r13x) / r133
    m1ay = (G * massList[1] * r12y) / r123 + (G * massList[2] * r13y) / r133
    m1az = (G * massList[1] * r12z) / r123 + (G * massList[2] * r13z) / r133
    # Accelerations of mass 2
    m2ax = (G * massList[0] * r21x) / r213 + (G * massList[2] * r23x) / r233
    m2ay = (G * massList[0] * r21y) / r213 + (G * massList[2] * r23y) / r233
    m2az = (G * massList[0] * r21z) / r213 + (G * massList[2] * r23z) / r233
    # Accelerations of mass 3
    m3ax = (G * massList[0] * r31x) / r313 + (G * massList[1] * r32x) / r323
    m3ay = (G * massList[0] * r31y) / r313 + (G * massList[1] * r32y) / r323
    m3az = (G * massList[0] * r31z) / r313 + (G * massList[1] * r32z) / r323
    return m1vx, m1vy, m1vz, m2vx, m2vy, m2vz, m3vx, m3vy, m3vz, m1ax, m1ay, m1az, m2ax, m2ay, m2az, m3ax, m3ay, m3az