# Imports
from Modules import *

# RK41st - Runge Kutta 4 ODE Solver (Of the form da / db) 
# Input:
#   ODE - Ordinary Differential Equation that is being solved
#   a0 - Original position
#   b0 - Original time
#   bn - Final time
#   h - Step
# Algorithm:
#   * Calculate the number of points n
#   * Initialize the a values to zero with n + 1 entries
#   * Set the initial value of a to be a0
#   * Generate a list for b values from b0 to bn with n + 1 entries
#   * Iterate over the total number of entries n
#       * Update a to be the current value of a in a_values
#       * Update b to be the current value of b in b_values
#       * Calculate k1, k2, k3, k4 from the definition of RK4
#       * Update the next entry of a_values with the definition of RK4
#   * Return the lists b_values and a_values
# Output:
#   a_values - List of a values that were found from RK4 method
#   b_values - List of b values that were found from RK4 method
def RK41st(ODE, a0, b0, bn, h):
    # Number of points
    n = int((bn - b0) / h)
    # List for a values
    a_values = np.zeros(n + 1)
    # Initialize a
    a_values[0] = a0
    # Initialize b
    b_values = np.linspace(b0, bn, n + 1)
    # Iterate over points
    for i in range(n):
        # Current state of values
        a = a_values[i]
        b = b_values[i]
        # RK4 update
        k1 = h * ODE(a, b)
        k2 = h * ODE(a + 0.5 * k1, b + 0.5 * h)
        k3 = h * ODE(a + 0.5 * k2, b + 0.5 * h)
        k4 = h * ODE(a + k3, b + h)
        # Next state values
        a_values[i + 1] = a + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return a_values, b_values

# RK42nd - Runge Kutta 4 ODE Solver For A Second Order ODE (Of the form d^2a / dc^2)
# Input:
#   ODE - Function that represents a second order ODE
#       * Particularly, this function must return da_dc, db_dc
#   a0 - Initial value for a
#   b0 - Initial value for b
#   c0 - Initial value for c
#   cn - Final value for c
#   h - Step Size
# Algorithm:
#   * Calculate the number of points n
#   * Create lists for a, b, and c values
#   * Initialize the values for a and b in their lists
#   * Iterate over the total number of points n
#       * Assign the values for a, b, and c with the current list value
#       * Calculate the values for k1_a, k2_a, k3_a, and k4_a
#       * Calculate the values for k1_b, k2_b, k3_b, and k4_b
#       * Assign the next values for a and b in their lists
#   * Return the lists
# Output:
#   a_values - List of a values that were found from RK4 method
#   b_values - List of b values that were found from RK4 method
#   c_values - List of c values that were found from RK4 method
def RK42nd(ODE, a0, b0, c0, cn, h):
    # Number of points
    n = int((cn - c0) / h)
    # List for a values
    a_values = np.zeros(n + 1)
    # List for b values
    b_values = np.zeros(n + 1)
    # Initialize a
    a_values[0] = a0
    # Initialize b
    b_values[0] = b0
    # Initialize c list
    c_values = np.linspace(c0, cn, n + 1)
    # Iterate over points
    for i in range(n):
        # Current state of values
        a = a_values[i]
        b = b_values[i]
        c = c_values[i]
        # RK4 update
        k1_a, k1_b = h * np.array(ODE(c, a, b))
        k2_a, k2_b = h * np.array(ODE(c + 0.5 * h, a + 0.5 * k1_a, b + 0.5 * k1_b))
        k3_a, k3_b = h * np.array(ODE(c + 0.5 * h, a + 0.5 * k2_a, b + 0.5 * k2_b))
        k4_a, k4_b = h * np.array(ODE(c + h, a + k3_a, b + k3_b))
        # Next state of values
        a_values[i + 1] = a + (1/6) * (k1_a + 2 * k2_a + 2 * k3_a + k4_a)
        b_values[i + 1] = b + (1/6) * (k1_b + 2 * k2_b + 2 * k3_b + k4_b)
    return a_values, b_values, c_values

# RK4TwoBody - RK4 Method That Solves The Force Attraction Between Two Bodies In Space
# Input:
#   ODE - Differential equation that represents the model that is to be solved
#   massList - Array of masses in model
#   ic - Initial conditions of bodies
#   t0 - Initial time in model
#   tn - Final time in model
#   h - Step size
# Algorithm:
#   * Calculate the number of points in solution
#   * Create empty lists for the parameters of each mass
#   * Create empty list for the time in the model
#   * Initialize lists to their initial conditions
#   * Iterate over the total number of points
#       * Generate the state of the current parameters
#       * Update the time to the current time in the step
#       * Update the state with the RK4 method
#       * Generate the next state of the system
#       * Update the next state of the system
#   * Return the lists
# Output:
#   mass1Pos - List of mass 1 positions with respect to time
#   mass2Pos - List of mass 2 positions with respect to time
#   mass1Vel - List of mass 1 velocities with respect to time
#   mass2Vel - List of mass 2 velocities with respect to time
#   time_vals - List of times at current steps in model
def RK4TwoBody(ODE, massList, ic, t0, tn, h):
    # Number of points
    n = int((tn - t0) / h)
    # Mass 1 position lists
    m1_x_vals = np.zeros(n + 1)
    m1_y_vals = np.zeros(n + 1)
    m1_z_vals = np.zeros(n + 1)
    # Mass 2 position lists
    m2_x_vals = np.zeros(n + 1)
    m2_y_vals = np.zeros(n + 1)
    m2_z_vals = np.zeros(n + 1)
    # Mass 1 velocity lists
    m1_vx_vals = np.zeros(n + 1)
    m1_vy_vals = np.zeros(n + 1)
    m1_vz_vals = np.zeros(n + 1)
    # Mass 2 velocity lists
    m2_vx_vals = np.zeros(n + 1)
    m2_vy_vals = np.zeros(n + 1)
    m2_vz_vals = np.zeros(n + 1)
    # Initializing mass 1 position lists
    m1_x_vals[0] = ic[0][0]
    m1_y_vals[0] = ic[0][1]
    m1_z_vals[0] = ic[0][2]
    # Initializing mass 2 position lists
    m2_x_vals[0] = ic[1][0]
    m2_y_vals[0] = ic[1][1]
    m2_z_vals[0] = ic[1][2]
    # Initializing mass 1 velocity lists
    m1_vx_vals[0] = ic[2][0]
    m1_vy_vals[0] = ic[2][1]
    m1_vz_vals[0] = ic[2][2]
    # Initializing mass 2 velocity lists
    m2_vx_vals[0] = ic[3][0]
    m2_vy_vals[0] = ic[3][1]
    m2_vz_vals[0] = ic[3][2]
    # Initialize time list
    time_vals = np.linspace(t0, tn, n + 1)
    # Iterate over points
    for i in range(n):
        # Current state of system
        state = (m1_x_vals[i], m1_y_vals[i], m1_z_vals[i], 
                m2_x_vals[i], m2_y_vals[i], m2_z_vals[i], 
                m1_vx_vals[i], m1_vy_vals[i], m1_vz_vals[i], 
                m2_vx_vals[i], m2_vy_vals[i], m2_vz_vals[i])
        # Current time of state
        t = time_vals[i]
        # RK4 update
        k1 = np.array(ODE(t, massList, *state))
        k2 = np.array(ODE(t + 0.5 * h, massList, *(np.add(state, 0.5 * h * k1))))
        k3 = np.array(ODE(t + 0.5 * h, massList, *(np.add(state, 0.5 * h * k2))))
        k4 = np.array(ODE(t + h, massList, *(np.add(state, h * k3))))
        # Next state of system
        next_state = np.add(state, (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4))
        # Update next stat of system
        (m1_x_vals[i + 1], m1_y_vals[i + 1], m1_z_vals[i + 1],
        m2_x_vals[i + 1], m2_y_vals[i + 1], m2_z_vals[i + 1],
        m1_vx_vals[i + 1], m1_vy_vals[i + 1], m1_vz_vals[i + 1],
        m2_vx_vals[i + 1], m2_vy_vals[i + 1], m2_vz_vals[i + 1]) = next_state
    # Parameter lists
    mass1Pos = [m1_x_vals, m1_y_vals, m1_z_vals]
    mass1Vel = [m1_vx_vals, m1_vy_vals, m1_vz_vals]
    mass2Pos = [m2_x_vals, m2_y_vals, m2_z_vals]
    mass2Vel = [m2_vx_vals, m2_vy_vals, m2_vz_vals]
    return mass1Pos, mass2Pos, mass1Vel, mass2Vel, time_vals

# RK4ThreeBody - RK4 Method That Solves The Force Attraction Between Three Bodies In Space
# Input:
#   ODE - Differential equation that represents the model that is to be solved
#   massList - Array of masses in model
#   ic - Initial conditions of bodies
#   t0 - Initial time in model
#   tn - Final time in model
#   h - Step size
# Algorithm:
#   * Calculate the number of points in solution
#   * Create empty lists for the parameters of each mass
#   * Create empty list for the time in the model
#   * Initialize lists to their initial conditions
#   * Iterate over the total number of points
#       * Generate the state of the current parameters
#       * Update the time to the current time in the step
#       * Update the state with the RK4 method
#       * Generate the next state of the system
#       * Update the next state of the system
#   * Return the lists
# Output:
#   mass1Pos - List of mass 1 positions with respect to time
#   mass2Pos - List of mass 2 positions with respect to time
#   mass3Pos - List of mass 3 positions with respect to time
#   mass1Vel - List of mass 1 velocities with respect to time
#   mass2Vel - List of mass 2 velocities with respect to time
#   mass3Vel - List of mass 3 velocities with respect to time
#   time_vals - List of times at current steps in model
def RK4ThreeBody(ODE, massList, ic, t0, tn, h):
    # Number of points
    n = int((tn - t0) / h)
    # Mass 1 position lists
    m1_x_vals = np.zeros(n + 1)
    m1_y_vals = np.zeros(n + 1)
    m1_z_vals = np.zeros(n + 1)
    # Mass 2 position lists
    m2_x_vals = np.zeros(n + 1)
    m2_y_vals = np.zeros(n + 1)
    m2_z_vals = np.zeros(n + 1)
    # Mass 3 position lists
    m3_x_vals = np.zeros(n + 1)
    m3_y_vals = np.zeros(n + 1)
    m3_z_vals = np.zeros(n + 1)
    # Mass 1 velocity lists
    m1_vx_vals = np.zeros(n + 1)
    m1_vy_vals = np.zeros(n + 1)
    m1_vz_vals = np.zeros(n + 1)
    # Mass 2 velocity lists
    m2_vx_vals = np.zeros(n + 1)
    m2_vy_vals = np.zeros(n + 1)
    m2_vz_vals = np.zeros(n + 1)
    # Mass 3 velocity lists
    m3_vx_vals = np.zeros(n + 1)
    m3_vy_vals = np.zeros(n + 1)
    m3_vz_vals = np.zeros(n + 1)
    # Initializing mass 1 position lists
    m1_x_vals[0] = ic[0][0]
    m1_y_vals[0] = ic[0][1]
    m1_z_vals[0] = ic[0][2]
    # Initializing mass 2 position lists
    m2_x_vals[0] = ic[1][0]
    m2_y_vals[0] = ic[1][1]
    m2_z_vals[0] = ic[1][2]
    # Initializing mass 3 position lists
    m3_x_vals[0] = ic[2][0]
    m3_y_vals[0] = ic[2][1]
    m3_z_vals[0] = ic[2][2]
    # Initializing mass 1 velocity lists
    m1_vx_vals[0] = ic[3][0]
    m1_vy_vals[0] = ic[3][1]
    m1_vz_vals[0] = ic[3][2]
    # Initializing mass 2 velocity lists
    m2_vx_vals[0] = ic[4][0]
    m2_vy_vals[0] = ic[4][1]
    m2_vz_vals[0] = ic[4][2]
    # Initializing mass 3 velocity lists
    m3_vx_vals[0] = ic[5][0]
    m3_vy_vals[0] = ic[5][1]
    m3_vz_vals[0] = ic[5][2]
    # Initialize time list
    time_vals = np.linspace(t0, tn, n + 1)
    # Iterate over points
    for i in range(n):
        # Current state of system
        state = (m1_x_vals[i], m1_y_vals[i], m1_z_vals[i],
                m2_x_vals[i], m2_y_vals[i], m2_z_vals[i],
                m3_x_vals[i], m3_y_vals[i], m3_z_vals[i],
                m1_vx_vals[i], m1_vy_vals[i], m1_vz_vals[i],
                m2_vx_vals[i], m2_vy_vals[i], m2_vz_vals[i],
                m3_vx_vals[i], m3_vy_vals[i], m3_vz_vals[i])
        # Current time of state
        t = time_vals[i]
        # RK4 update
        k1 = np.array(ODE(t, massList, *state))
        k2 = np.array(ODE(t + 0.5 * h, massList, *(np.add(state, 0.5 * h * k1))))
        k3 = np.array(ODE(t + 0.5 * h, massList, *(np.add(state, 0.5 * h * k2))))
        k4 = np.array(ODE(t + h, massList, *(np.add(state, h * k3))))
        # Next state of system
        next_state = np.add(state, (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4))
        # Update next stat of system
        (m1_x_vals[i + 1], m1_y_vals[i + 1], m1_z_vals[i + 1],
        m2_x_vals[i + 1], m2_y_vals[i + 1], m2_z_vals[i + 1],
        m3_x_vals[i + 1], m3_y_vals[i + 1], m3_z_vals[i + 1],
        m1_vx_vals[i + 1], m1_vy_vals[i + 1], m1_vz_vals[i + 1],
        m2_vx_vals[i + 1], m2_vy_vals[i + 1], m2_vz_vals[i + 1],
        m3_vx_vals[i + 1], m3_vy_vals[i + 1], m3_vz_vals[i + 1]) = next_state
    # Parameter lists
    mass1Pos = [m1_x_vals, m1_y_vals, m1_z_vals]
    mass1Vel = [m1_vx_vals, m1_vy_vals, m1_vz_vals]
    mass2Pos = [m2_x_vals, m2_y_vals, m2_z_vals]
    mass2Vel = [m2_vx_vals, m2_vy_vals, m2_vz_vals]
    mass3Pos = [m3_x_vals, m3_y_vals, m3_z_vals]
    mass3Vel = [m3_vx_vals, m3_vy_vals, m3_vz_vals]
    return mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time_vals