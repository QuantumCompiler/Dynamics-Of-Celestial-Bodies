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