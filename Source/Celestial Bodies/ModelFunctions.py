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

# CoupledTwoBodySolver - Solves the 2 Body problem with an RK4
# Input:
#   massList - Array of masses:
#       massList[0] - Mass of mass 1
#       massList[1] - Mass of mass 2
#   ic - Matrix of initial conditions:
#       ic[0][0] - Initial x position of mass 1
#       ic[0][1] - Initial y position of mass 1
#       ic[0][2] - Initial z position of mass 1
#       ic[1][0] - Initial x position of mass 2
#       ic[1][1] - Initial y position of mass 2
#       ic[1][2] - Initial z position of mass 2
#       ic[2][0] - Initial velocity of mass 1 in x
#       ic[2][1] - Initial velocity of mass 1 in y
#       ic[2][2] - Initial velocity of mass 1 in z
#       ic[3][0] - Initial velocity of mass 2 in x
#       ic[3][1] - Initial velocity of mass 2 in y
#       ic[3][2] - Initial velocity of mass 2 in z
#   t0 - Initial time of model
#   tn - Final time of model
# Algorithm:
#   * Calculate the number of steps required for the solver
#   * Call the RK4 solver
#   * Return the lists
# Output:
#   mass1Pos - List of positions of mass 1:
#       mass1Pos[0] - Positions of mass 1 in x
#       mass1Pos[1] - Positions of mass 1 in y
#       mass1Pos[2] - Positions of mass 1 in z
#   mass2Pos - List of positions of mass 2:
#       mass2Pos[0] - Positions of mass 2 in x
#       mass2Pos[1] - Positions of mass 2 in y
#       mass2Pos[2] - Positions of mass 2 in z
#   mass1Vel - List of velocities of mass 1:
#       mass1Vel[0] - Velocities of mass 1 in x
#       mass1Vel[1] - Velocities of mass 1 in y
#       mass1Vel[2] - Velocities of mass 1 in z
#   mass2Vel - List of velocities of mass 2:
#       mass2Vel[0] - Velocities of mass 2 in x
#       mass2Vel[1] - Velocities of mass 2 in y
#       mass2Vel[2] - Velocities of mass 2 in z
#   time - List of time values in model
def CoupledTwoBodySolver(massList, ic, t0, tn):
    # Steps
    h = (tn - t0) / 1000
    # RK4 solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = RK4TwoBody(TwoCoupledBodies, massList, ic, t0, tn, h)
    return mass1Pos, mass2Pos, mass1Vel, mass2Vel, time

def CoupledTwoBody2DPlotPos(massList, ic, t0, tn, i, j, m1Name, m2Name):
    # Solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = CoupledTwoBodySolver(massList, ic, t0, tn)
    # Direction place holder
    iDirection = ''
    jDirection = ''
    if (i == 0):
        iDirection = "$x$"
    elif (i == 1):
        iDirection = "$y$"
    elif (i == 2):
        iDirection = "$z$"
    if (j == 0):
        jDirection = "$x$"
    elif (j == 1):
        jDirection = "$y$"
    elif (j == 2):
        jDirection = "$z$"
    # Plot
    plt.plot(mass1Pos[i], mass1Pos[j], color = "green", label = m1Name)
    plt.plot(mass2Pos[i], mass2Pos[j], color = "blue", label = m2Name)
    # Title and labels
    plt.title(f"2D Position Plot Of Coupled Bodies - {jDirection} vs. {iDirection}")
    plt.xlabel(f"{iDirection} Direction In (m)")
    plt.ylabel(f"{jDirection} Direction In (m)")
    plt.legend()
    plt.show()