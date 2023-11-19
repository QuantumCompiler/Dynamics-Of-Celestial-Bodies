# Imports
from Models import *

# Earth2DModelSolver - Solves the 2D force model for projectile motion on Earth
# Input:
#   ic - Array of initial conditions:
#       ic[0] - Object's initial height
#       ic[1] - Object's initial velocity
#   t0 - Initial time of trajectory
#   tn - Final time of trajectory
# Algorithm:
#   * Calculate the step size to be used in the model
#   * Call the RK4 solver
# Output:
#   ypos - Position of object with respect to time in y
#   yvelo - Velocity of object with respect to time in y
#   time - List of time values
def Earth2DModelSolver(ic, t0, tn):
    # Step size
    h = (tn - t0) / 1000
    # RK4 solver
    ypos, yvelo, time = RK42nd(Earth2DForceModel, ic[0], ic[1], t0, tn, h)
    return ypos, yvelo, time

# Earth2DModelPlotPos - Plots the position versus time of projectile motion on Earth
# Input:
#   ic - Array of initial conditions
#       ic[0] - Object's initial height
#       ic[1] - Object's initial velocity
#   t0 - Initial time of trajectory
#   tn - Final time of trajectory
# Algorithm:
#   * Call the RK4 solver
#   * Plot the position vs. time
#   * Set the title and labels of the plot
# Output:
#   This function does not return a value, it plots data for a given set of initial conditions in projectile motion
def Earth2DModelPlotPos(ic, t0, tn):
    # Solver
    ypos, yvelo, time = Earth2DModelSolver(ic, t0, tn)
    # Plot
    plt.plot(time, ypos, color = 'blue', label = 'Trajectory')
    # Title and labels
    plt.title(f"2D Projectile Motion - Position vs. Time: $y_{0} =$ {round(ic[0], 3)} (m), $v_{0} =$ {round(ic[1], 3)} $(\\frac{{m}}{{s}})$")
    plt.xlabel(f"Time In ({round(tn, 3)}) Seconds")
    plt.ylabel(f"Height In (m)")
    plt.legend()
    plt.show()

# Earth2DModelPlotVelo - Plots the velocity versus time of projectile motion on Earth
# Input:
#   ic - Array of initial conditions
#       ic[0] - Object's initial height
#       ic[1] - Object's initial velocity
#   t0 - Initial time of trajectory
#   tn - Final time of trajectory
# Algorithm:
#   * Call the RK4 solver
#   * Plot the velocity vs. time
#   * Set the title and labels of the plot
# Output:
#   This function does not return a value, it plots data for a given set of initial conditions in projectile motion
def Earth2DModelPlotVelo(ic, t0, tn):
    # Solver
    ypos, yvelo, time = Earth2DModelSolver(ic, t0, tn)
    # Plot
    plt.plot(time, yvelo, color = 'blue', label = 'Velocity')
    # Title and labels
    plt.title(f"2D Projectile Motion - Velocity vs. Time: $y_{0} =$ {round(ic[0], 3)} (m), $v_{0} =$ {round(ic[1], 3)} $(\\frac{{m}}{{s}})$")
    plt.xlabel(f"Time In ({round(tn, 3)}) Seconds")
    plt.ylabel(f"Velocity In $(\\frac{{m}}{{s}})$")
    plt.show()