# Modules
import numpy as np

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
    n = int((bn - b0) / h)
    a_values = np.zeros(n + 1)
    a_values[0] = a0
    b_values = np.linspace(b0, bn, n + 1)
    for i in range(n):
        a = a_values[i]
        b = b_values[i]
        k1 = h * ODE(a, b)
        k2 = h * ODE(a + 0.5 * k1, b + 0.5 * h)
        k3 = h * ODE(a + 0.5 * k2, b + 0.5 * h)
        k4 = h * ODE(a + k3, b + h)
        a_values[i + 1] = a + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return a_values, b_values

# Define the system of ODEs
# u' = v
# v' = f(t, u, v)
def system_of_odes(t, u, v):
    return v, -9.81  # Example: free-fall under gravity

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
    n = int((cn - c0) / h)
    a_values = np.zeros(n + 1)
    b_values = np.zeros(n + 1)
    c_values = np.linspace(c0, cn, n + 1)
    a_values[0] = a0
    b_values[0] = b0
    for i in range(n):
        a = a_values[i]
        b = b_values[i]
        c = c_values[i]
        k1_a, k1_b = h * np.array(ODE(c, a, b))
        k2_a, k2_b = h * np.array(ODE(c + 0.5 * h, a + 0.5 * k1_a, b + 0.5 * k1_b))
        k3_a, k3_b = h * np.array(ODE(c + 0.5 * h, a + 0.5 * k2_a, b + 0.5 * k2_b))
        k4_a, k4_b = h * np.array(ODE(c + h, a + k3_a, b + k3_b))
        a_values[i + 1] = a + (1/6) * (k1_a + 2 * k2_a + 2 * k3_a + k4_a)
        b_values[i + 1] = b + (1/6) * (k1_b + 2 * k2_b + 2 * k3_b + k4_b)
    return a_values, b_values, c_values