# Imports
from Models import *

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Solvers
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

""" ProjectileMotionSolver - Solves projectile motion for a projectile on a given object
    Input:
        obj - List of object parameters where projectile motion is occurring
            obj[0] - Mass of object
            obj[1] - Distance from center of mass of object
        ic - Initial conditions of projectile
            ic[0] - Initial vertical position of projectile
            ic[1] - Initial vertical velocity of projectile
        t0 - Initial time of model
        tn - Final time of model
    Algorithm:
        * Calculate the number of steps for the RK4 solver
        * Call the RK4 solver
        * Return the lists
    Output:
        pos - List of positions of projectile
        vel - List of velocities of projectile
        time - List of times of model
"""
def ProjectileMotionSolver(obj, ic, t0, tn):
    # Steps
    h = (tn - t0) / 10000
    # RK4 Solver
    pos, vel, time = RK4ProjectileMotion(ProjectileMotion, obj, ic, t0, tn, h)
    return pos, vel, time

""" CoupledTwoBodySolver - Solves the 2 Body problem with an RK4
    Input:
        massList - Array of masses:
        ic - Matrix of initial conditions:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial velocity of mass 1 in x
            ic[2][1] - Initial velocity of mass 1 in y
            ic[2][2] - Initial velocity of mass 1 in z
            ic[3][0] - Initial velocity of mass 2 in x
            ic[3][1] - Initial velocity of mass 2 in y
            ic[3][2] - Initial velocity of mass 2 in z
        t0 - Initial time of model
        tn - Final time of model
    Algorithm:
        * Calculate the number of steps for the RK4 solver
        * Call the RK4 solver
        * Return the lists from the RK4 solver
    Output:
        mass1Pos - List of positions of mass 1:
            mass1Pos[0] - Positions of mass 1 in x
            mass1Pos[1] - Positions of mass 1 in y
            mass1Pos[2] - Positions of mass 1 in z
        mass2Pos - List of positions of mass 2:
            mass2Pos[0] - Positions of mass 2 in x
            mass2Pos[1] - Positions of mass 2 in y
            mass2Pos[2] - Positions of mass 2 in z
        mass1Vel - List of velocities of mass 1:
            mass1Vel[0] - Velocities of mass 1 in x
            mass1Vel[1] - Velocities of mass 1 in y
            mass1Vel[2] - Velocities of mass 1 in z
        mass2Vel - List of velocities of mass 2:
            mass2Vel[0] - Velocities of mass 2 in x
            mass2Vel[1] - Velocities of mass 2 in y
            mass2Vel[2] - Velocities of mass 2 in z
        time - List of time values in model
"""
def CoupledTwoBodySolver(massList, ic, t0, tn):
    # Steps
    h = (tn - t0) / 10000
    # RK4 solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = RK4TwoBody(TwoCoupledBodies, massList, ic, t0, tn, h)
    return mass1Pos, mass2Pos, mass1Vel, mass2Vel, time

""" CoupledThreeBodySolver - Solves the 3 Body problem with an RK4
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions for masses in system:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial x position of mass 3
            ic[2][1] - Initial y position of mass 3
            ic[2][2] - Initial z position of mass 3
            ic[3][0] - Initial velocity of mass 1 in x
            ic[3][1] - Initial velocity of mass 1 in y
            ic[3][2] - Initial velocity of mass 1 in z
            ic[4][0] - Initial velocity of mass 2 in x
            ic[4][1] - Initial velocity of mass 2 in y
            ic[4][2] - Initial velocity of mass 2 in z
            ic[5][0] - Initial velocity of mass 3 in x
            ic[5][1] - Initial velocity of mass 3 in y
            ic[5][2] - Initial velocity of mass 3 in z
        t0 - Initial time of system
        tn - Final time of system
    Algorithm:
        * Calculate the number of steps for the RK4 solver
        * Call the RK4 solver
        * Return the lists from the RK4 solver
    Output:
        mass1Pos - List of positions of mass 1:
            mass1Pos[0] - Positions of mass 1 in x
            mass1Pos[1] - Positions of mass 1 in y
            mass1Pos[2] - Positions of mass 1 in z
        mass2Pos - List of positions of mass 2:
            mass2Pos[0] - Positions of mass 2 in x
            mass2Pos[1] - Positions of mass 2 in y
            mass2Pos[2] - Positions of mass 2 in z
        mass3Pos - List of positions of mass 3:
            mass3Pos[0] - Positions of mass 3 in x
            mass3Pos[1] - Positions of mass 3 in y
            mass3Pos[2] - Positions of mass 3 in z
        mass1Vel - List of velocities of mass 1:
            mass1Vel[0] - Velocities of mass 1 in x
            mass1Vel[1] - Velocities of mass 1 in y
            mass1Vel[2] - Velocities of mass 1 in z
        mass2Vel - List of velocities of mass 2:
            mass2Vel[0] - Velocities of mass 2 in x
            mass2Vel[1] - Velocities of mass 2 in y
            mass2Vel[2] - Velocities of mass 2 in z
        mass3Vel - List of velocities of mass 3:
            mass3Vel[0] - Velocities of mass 3 in x
            mass3Vel[1] - Velocities of mass 3 in y
            mass3Vel[2] - Velocities of mass 3 in z
        time - List of time values in model
"""
def CoupledThreeBodySolver(massList, ic, t0, tn):
    # Steps
    h = (tn - t0) / 10000
    # RK4 Solver
    mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time = RK4ThreeBody(ThreeCoupledBodies, massList, ic, t0, tn, h)
    return mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Two Bodies
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Projectile Motion Position
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" ProjectileMotionPositionPlot - Position plot of projectile motion
    Input:
        obj - List of object parameters where projectile motion is occurring
            obj[0] - Mass of object
            obj[1] - Distance from center of mass of object
        ic - Initial conditions of projectile
            ic[0] - Initial vertical position of projectile
            ic[1] - Initial vertical velocity of projectile
        t0 - Initial time of model
        tn - Final time of model
    Algorithm:
        * Call the solver for projectile motion
        * Plot the position versus time
    Output:
        This function does not return a value
"""
def ProjectileMotionPositionPlot(obj, ic, t0, tn, objName, projectileName):
    # Solver
    position, velocity, time = ProjectileMotionSolver(obj, ic, t0, tn)
    # Plot
    plt.plot(time, position, '-', color = 'green', linewidth = 1, label = projectileName)
    plt.title(f"Projectile Motion Plot Of Position Under The Influence Of {objName}", fontsize = TWODPLOTTITLE)
    plt.xlabel(f"Time In Seconds (s)", fontsize = TWODPLOTABELS)
    plt.ylabel(f"Vertical Position In (m)", fontsize = TWODPLOTABELS)
    plt.legend()
    plt.show()

def DerfNop(obj, ic, t0, tn, objName, projectileName):
    # Solver
    position, velocity, time = ProjectileMotionSolver(obj, ic, t0, tn)

    # Create an instance of PlotCanvas
    plot_canvas = PlotCanvas(width=5, height=4, dpi=100)

    # Plot using the axes of PlotCanvas
    plot_canvas.axes.plot(time, position, '-', color='green', linewidth=1, label=projectileName)
    plot_canvas.axes.set_title(f"Projectile Motion Plot Of Position Under The Influence Of {objName}")
    plot_canvas.axes.set_xlabel("Time In Seconds (s)")
    plot_canvas.axes.set_ylabel("Vertical Position In (m)")
    plot_canvas.axes.legend()

""" ProjectileMotionPositionAnim - Position animation plot of projectile motion
    Input:
        obj - List of object parameters where projectile motion is occurring
            obj[0] - Mass of object
            obj[1] - Distance from center of mass of object
        ic - Initial conditions of projectile
            ic[0] - Initial vertical position of projectile
            ic[1] - Initial vertical velocity of projectile
        t0 - Initial time of model
        tn - Final time of model
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min positions
        * Set the max and min for the axii
        * Format the scales of the axii
        * Set up the animation parameters
        * Define the init function
        * Define the animation function
        * Call the animation
        * Set the title and labels
    Output:
        This function does not return a value
"""
def ProjectileMotionPositionAnim(obj, ic, t0, tn, objName, projectileName):
    # Solver
    position, velocity, time = ProjectileMotionSolver(obj, ic, t0, tn)
    fig, ax = plt.subplots()
    # Animation parameters
    projectile, = ax.plot([], [], 'o', color = 'green', markersize = 2, label = projectileName)
    projectileTrail, = ax.plot([], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
    plt.xlim(min(time) - 0.05 * max(time), 1.05 * max(time))
    plt.ylim(min(position) - 0.05 * max(position), 1.05 * max(position))
    # Init Inner Function
    def init():
        projectile.set_data([], [])
        projectileTrail.set_data([], [])
        return projectile, projectileTrail
    # Animate Inner Function
    def animate(k):
        projectile.set_data([time[k], position[k]])
        projectileTrail.set_data(time[:k+1], position[:k+1])
        return projectile, projectileTrail
    # Animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=1e-5, blit=True, repeat=True)
    # Title and labels
    ax.set_title(f"Projectile Motion Animation Of Position Under The Influence Of {objName}", fontsize = TWODANIMTITLE)
    ax.set_xlabel(f"Time In Seconds (s)", fontsize = TWODANIMLABELS)
    ax.set_ylabel(f"Vertical Position In (m)", fontsize = TWODANIMLABELS)
    ax.legend()

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Projectile Motion Velocity
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" ProjectileMotionVelocityPlot - Velocity plot of projectile motion
    Input:
        obj - List of object parameters where projectile motion is occurring
            obj[0] - Mass of object
            obj[1] - Distance from center of mass of object
        ic - Initial conditions of projectile
            ic[0] - Initial vertical position of projectile
            ic[1] - Initial vertical velocity of projectile
        t0 - Initial time of model
        tn - Final time of model
    Algorithm:
        * Call the solver for projectile motion
        * Plot the velocity versus time
    Output:
        This function does not return a value
"""
def ProjectileMotionVelocityPlot(obj, ic, t0, tn, objName, projectileName):
    # Solver
    position, velocity, time = ProjectileMotionSolver(obj, ic, t0, tn)
    # Plot
    plt.plot(time, velocity, '-', color = 'green', linewidth = 1, label = projectileName)
    plt.title(f"Projectile Motion Plot Of Velocity Under The Influence Of {objName}", fontsize = TWODPLOTTITLE)
    plt.xlabel(f"Time In Seconds (s)", fontsize = TWODPLOTABELS)
    plt.ylabel(f"Vertical Velocity In $(\\frac{{m}}{{s}})$", fontsize = TWODPLOTABELS)
    plt.legend()
    plt.show()

""" ProjectileMotionVelocityAnim - Velocity animation plot of projectile motion
    Input:
        obj - List of object parameters where projectile motion is occurring
            obj[0] - Mass of object
            obj[1] - Distance from center of mass of object
        ic - Initial conditions of projectile
            ic[0] - Initial vertical position of projectile
            ic[1] - Initial vertical velocity of projectile
        t0 - Initial time of model
        tn - Final time of model
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min positions
        * Set the max and min for the axii
        * Format the scales of the axii
        * Set up the animation parameters
        * Define the init function
        * Define the animation function
        * Call the animation
        * Set the title and labels
    Output:
        This function does not return a value
"""
def ProjectileMotionVelocityAnim(obj, ic, t0, tn, objName, projectileName):
    # Solver
    position, velocity, time = ProjectileMotionSolver(obj, ic, t0, tn)
    fig, ax = plt.subplots()
    # Animation parameters
    projectile, = ax.plot([], [], 'o', color = 'green', markersize = 2, label = projectileName)
    projectileTrail, = ax.plot([], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
    plt.xlim(min(time) - 0.05 * max(time), 1.05 * max(time))
    plt.ylim(1.05 * min(velocity), 0.05 * abs(min(velocity)))
    # Init Inner Function
    def init():
        projectile.set_data([], [])
        projectileTrail.set_data([], [])
        return projectile, projectileTrail
    # Animate Inner Function
    def animate(k):
        projectile.set_data([time[k], velocity[k]])
        projectileTrail.set_data(time[:k+1], velocity[:k+1])
        return projectile, projectileTrail
    # Animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=1e-5, blit=True, repeat=True)
    # Title and labels
    ax.set_title(f"Projectile Motion Animation Of Velocity Under The Influence Of {objName}", fontsize = TWODANIMTITLE)
    ax.set_xlabel(f"Time In Seconds (s)", fontsize = TWODANIMLABELS)
    ax.set_ylabel(f"Vertical Velocity In $(\\frac{{m}}{{s}})$", fontsize = TWODPLOTABELS)
    ax.legend()

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Two Body 2D Position
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" CoupledTwoBody2DPlotPos - Plots the positions of two bodies in space in 2D
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial velocity of mass 1 in x
            ic[2][1] - Initial velocity of mass 1 in y
            ic[2][2] - Initial velocity of mass 1 in z
            ic[3][0] - Initial velocity of mass 2 in x
            ic[3][1] - Initial velocity of mass 2 in y
            ic[3][2] - Initial velocity of mass 2 in z
        t0 - Initial time in the system
        tn - Final time in the system
        i - Index used for accessing elements in the lists returned from the RK4 solver
        j - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x direction
            1 - Corresponds to y direction
            2 - Corresponds to z direction
        m1Name - Name of mass 1
        m2Name - Name of mass 2
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min distances
        * Determine the place holders for the directions
        * Set the max and mins for axii
        * Format the scales of the axii
        * Plot the data
        * Place titles and labels on plot
    Output:
        This function does not return a value
"""
def CoupledTwoBody2DPlotPos(massList, ic, t0, tn, i, j, m1Name, m2Name):
    # Solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = CoupledTwoBodySolver(massList, ic, t0, tn)
    # Max pos
    maxDistX = max(max([pos[0] for pos in mass1Pos]), max([pos[0] for pos in mass2Pos])) * 1.1
    maxDistY = max(max([pos[1] for pos in mass1Pos]), max([pos[1] for pos in mass2Pos])) * 1.1
    maxDistZ = max(max([pos[2] for pos in mass1Pos]), max([pos[2] for pos in mass2Pos])) * 1.1
    # Direction place holder
    iDirection = ''
    jDirection = ''
    if (i == 0):
        iDirection = "$x$"
        plt.xlim(-maxDistX, maxDistX)
    elif (i == 1):
        iDirection = "$y$"
        plt.xlim(-maxDistY, maxDistY)
    elif (i == 2):
        iDirection = "$z$"
        plt.xlim(-maxDistZ, maxDistZ)
    if (j == 0):
        jDirection = "$x$"
        plt.ylim(-maxDistX, maxDistX)
    elif (j == 1):
        jDirection = "$y$"
        plt.ylim(-maxDistY, maxDistY)
    elif (j == 2):
        jDirection = "$z$"
        plt.ylim(-maxDistZ, maxDistZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax = plt.gca()
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Plot
    plt.plot(mass1Pos[i], mass1Pos[j], 'o', color = "green", markersize = '2', label = m1Name)
    plt.plot(mass2Pos[i], mass2Pos[j], 'o', color = "blue", markersize = '1', label = m2Name)
    # Title and labels
    plt.title(f"2D Position Plot Of Two Coupled Bodies - {jDirection} vs. {iDirection}", fontsize = TWODPLOTTITLE)
    plt.xlabel(f"{iDirection} Position In (m)", fontsize = TWODPLOTABELS)
    plt.ylabel(f"{jDirection} Position In (m)", fontsize = TWODPLOTABELS)
    plt.legend()
    plt.show()

""" CoupledTwoBody2DAnimPos - Plots the positions of two bodies in space as an animation in 2D
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial velocity of mass 1 in x
            ic[2][1] - Initial velocity of mass 1 in y
            ic[2][2] - Initial velocity of mass 1 in z
            ic[3][0] - Initial velocity of mass 2 in x
            ic[3][1] - Initial velocity of mass 2 in y
            ic[3][2] - Initial velocity of mass 2 in z
        t0 - Initial time in system
        tn - Final time in system
        i - Index used for accessing elements in the lists returned from the RK4 solver
        j - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x direction
            1 - Corresponds to y direction
            2 - Corresponds to z direction
        m1Name - Name of mass 1
        m2Name - Name of mass 2
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min positions
        * Determine the place holders for the directions
        * Set the max and min for the axii
        * Format the scales of the axii
        * Set up the animation parameters
        * Define the init function
        * Define the animation function
        * Call the animation
        * Set the title and labels
    Output:
        This function does not return a value
"""
def CoupledTwoBody2DAnimPos(massList, ic, t0, tn, i, j, m1Name, m2Name):
    # Solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = CoupledTwoBodySolver(massList, ic, t0, tn)
    fig, ax = plt.subplots()
    # Max pos
    maxDistX = max(max([pos[0] for pos in mass1Pos]), max([pos[0] for pos in mass2Pos])) * 1.1
    maxDistY = max(max([pos[1] for pos in mass1Pos]), max([pos[1] for pos in mass2Pos])) * 1.1
    maxDistZ = max(max([pos[2] for pos in mass1Pos]), max([pos[2] for pos in mass2Pos])) * 1.1
    # Direction place holder
    iDirection = ''
    jDirection = ''
    if (i == 0):
        iDirection = "$x$"
        ax.set_xlim(-maxDistX, maxDistX)
    elif (i == 1):
        iDirection = "$y$"
        ax.set_xlim(-maxDistY, maxDistY)
    elif (i == 2):
        iDirection = "$z$"
        ax.set_xlim(-maxDistZ, maxDistZ)
    if (j == 0):
        jDirection = "$x$"
        ax.set_ylim(-maxDistX, maxDistX)
    elif (j == 1):
        jDirection = "$y$"
        ax.set_ylim(-maxDistY, maxDistY)
    elif (j == 2):
        jDirection = "$z$"
        ax.set_ylim(-maxDistZ, maxDistZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Animation parameters
    Mass1, = ax.plot([], [], 'o', color = 'green', markersize = 2, label = m1Name)
    Mass2, = ax.plot([], [], 'o', color = 'blue', markersize = 1, label = m2Name)
    Mass1Trail, = ax.plot([], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
    Mass2Trail, = ax.plot([], [], '-', color='blue', linewidth = 1, alpha=0.5)
    # Init Inner Function
    def init():
        Mass1.set_data([], [])
        Mass2.set_data([], [])
        Mass1Trail.set_data([], [])
        Mass2Trail.set_data([], [])
        return Mass1, Mass2, Mass1Trail, Mass2Trail
    # Animate Inner Function
    def animate(k):
        Mass1.set_data([mass1Pos[i][k]], [mass1Pos[j][k]])
        Mass2.set_data([mass2Pos[i][k]], [mass2Pos[j][k]])
        Mass1Trail.set_data(mass1Pos[i][:k+1], mass1Pos[j][:k+1])
        Mass2Trail.set_data(mass2Pos[i][:k+1], mass2Pos[j][:k+1])
        return Mass1, Mass2, Mass1Trail, Mass2Trail
    # Animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(mass1Pos[0]), interval=1e-5, blit=True, repeat=True)
    # Title and labels
    ax.set_title(f"2D Position Animation Of Two Coupled Bodies - {jDirection} vs. {iDirection}", fontsize = TWODANIMTITLE)
    ax.set_xlabel(f"{iDirection} Position In (m)", fontsize = TWODANIMLABELS)
    ax.set_ylabel(f"{jDirection} Position In (m)", fontsize = TWODANIMLABELS)
    ax.legend()
    plt.show()

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Two Body 2D Velocity
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" CoupledTwoBody2DPlotVel - Plots the velocity vs. time of two bodies in space in 2D
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial velocity of mass 1 in x
            ic[2][1] - Initial velocity of mass 1 in y
            ic[2][2] - Initial velocity of mass 1 in z
            ic[3][0] - Initial velocity of mass 2 in x
            ic[3][1] - Initial velocity of mass 2 in y
            ic[3][2] - Initial velocity of mass 2 in z
        t0 - Initial time in the system
        tn - Final time in the system
        i - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x velocity
            1 - Corresponds to y velocity
            2 - Corresponds to z velocity
        m1Name - Name of mass 1
        m2Name - Name of mass 2
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min velocities
        * Determine the place holders for the directions
        * Set the max and mins for axii
        * Format the scales of the axii
        * Plot the data
        * Place titles and labels on plot
    Output:
        This function does not return a value
"""
def CoupledTwoBody2DPlotVel(massList, ic, t0, tn, i, m1Name, m2Name):
    # Solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = CoupledTwoBodySolver(massList, ic, t0, tn)
    # Max velocity
    maxVelX = max(max([vel[0] for vel in mass1Vel]), max([vel[0] for vel in mass2Vel])) * 1.1
    maxVelY = max(max([vel[1] for vel in mass1Vel]), max([vel[1] for vel in mass2Vel])) * 1.1
    maxVelZ = max(max([vel[2] for vel in mass1Vel]), max([vel[2] for vel in mass2Vel])) * 1.1
    # Direction place holder
    plt.xlim((tn - 1.05 * tn), 1.05 * tn)
    iVelocity = ''
    if (i == 0):
        iVelocity = "$v_{x}$"
        plt.ylim(-maxVelX, maxVelX)
    elif (i == 1):
        iVelocity = "$v_{y}$"
        plt.ylim(-maxVelY, maxVelY)
    elif (i == 2):
        iVelocity = "$v_{z}$"
        plt.ylim(-maxVelZ, maxVelZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax = plt.gca()
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Plot
    plt.plot(time, mass1Vel[i], 'o', color = "green", markersize = '1', label = m1Name)
    plt.plot(time, mass2Vel[i], 'o', color = "blue", markersize = '1', label = m2Name)
    # Title and labels
    plt.title(f"2D Velocity Plot Of Two Coupled Bodies - {iVelocity} vs. Time", fontsize = TWODPLOTTITLE)
    plt.xlabel(f"Time In $(s)$", fontsize = TWODPLOTABELS)
    plt.ylabel(f"Velocity ({iVelocity}) In $\\frac{{m}}{{s}}$", fontsize = TWODPLOTABELS)
    plt.legend()
    plt.show()

""" CoupledTwoBody2DAnimVel - Plots the velocity vs. time of two bodies in space as an animation in 2D
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial velocity of mass 1 in x
            ic[2][1] - Initial velocity of mass 1 in y
            ic[2][2] - Initial velocity of mass 1 in z
            ic[3][0] - Initial velocity of mass 2 in x
            ic[3][1] - Initial velocity of mass 2 in y
            ic[3][2] - Initial velocity of mass 2 in z
        t0 - Initial time in system
        tn - Final time in system
        i - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x velocity
            1 - Corresponds to y velocity
            2 - Corresponds to z velocity
        m1Name - Name of mass 1
        m2Name - Name of mass 2
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min velocities
        * Determine the place holders for the directions
        * Set the max and min for the axii
        * Format the scales of the axii
        * Set up the animation parameters
        * Define the init function
        * Define the animation function
        * Call the animation
        * Set the title and labels
    Output:
        This function does not return a value
"""
def CoupledTwoBody2DAnimVel(massList, ic, t0, tn, i, m1Name, m2Name):
    # Solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = CoupledTwoBodySolver(massList, ic, t0, tn)
    fig, ax = plt.subplots()
    # Max velocity
    maxVelX = max(max([vel[0] for vel in mass1Vel]), max([vel[0] for vel in mass2Vel])) * 1.1
    maxVelY = max(max([vel[1] for vel in mass1Vel]), max([vel[1] for vel in mass2Vel])) * 1.1
    maxVelZ = max(max([vel[2] for vel in mass1Vel]), max([vel[2] for vel in mass2Vel])) * 1.1
    # Velocity place holder
    ax.set_xlim((tn - 1.05 * tn), 1.05 * tn)
    iVelocity = ''
    if (i == 0):
        iVelocity = "$v_{x}$"
        ax.set_ylim(-maxVelX, maxVelX)
    elif (i == 1):
        iVelocity = "$v_{y}$"
        ax.set_ylim(-maxVelY, maxVelY)
    elif (i == 2):
        iVelocity = "$v_{z}$"
        ax.set_ylim(-maxVelZ, maxVelZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Animation parameters
    Mass1, = ax.plot([], [], 'o', color = 'green', markersize = 2, label = m1Name)
    Mass2, = ax.plot([], [], 'o', color = 'blue', markersize = 1, label = m2Name)
    Mass1Trail, = ax.plot([], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
    Mass2Trail, = ax.plot([], [], '-', color='blue', linewidth = 1, alpha=0.5)
    # Init Inner Function
    def init():
        Mass1.set_data([], [])
        Mass2.set_data([], [])
        Mass1Trail.set_data([], [])
        Mass2Trail.set_data([], [])
        return Mass1, Mass2, Mass1Trail, Mass2Trail
    # Animate Inner Function
    def animate(k):
        Mass1.set_data([time[k]], [mass1Vel[i][k]])
        Mass2.set_data([time[k]], [mass2Vel[i][k]])
        Mass1Trail.set_data(time[:k+1], mass1Vel[i][:k+1])
        Mass2Trail.set_data(time[:k+1], mass2Vel[i][:k+1])
        return Mass1, Mass2, Mass1Trail, Mass2Trail
    # Animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(mass1Vel[0]), interval=1e-5, blit=True, repeat=True)
    # Title and labels
    ax.set_title(f"2D Velocity Animation Of Two Coupled Bodies - {iVelocity} vs. Time", fontsize = TWODANIMTITLE)
    ax.set_xlabel(f"Time In $(s)$", fontsize = TWODANIMLABELS)
    ax.set_ylabel(f"Velocity ({iVelocity}) In $\\frac{{m}}{{s}}$", fontsize = TWODANIMLABELS)
    ax.legend()
    plt.show()

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Two Body 3D Position
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" CoupledTwoBody3DPlotPos - Plots the positions of two bodies in space in 3D
    Input:
        massList - Array of masses in the system
        ic - Matrix of initial conditions:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial velocity of mass 1 in x
            ic[2][1] - Initial velocity of mass 1 in y
            ic[2][2] - Initial velocity of mass 1 in z
            ic[3][0] - Initial velocity of mass 2 in x
            ic[3][1] - Initial velocity of mass 2 in y
            ic[3][2] - Initial velocity of mass 2 in z
        t0 - Initial time in system
        tn - Final time in system
        m1Name - Name of mass 1
        m2Name - Name of mass 2
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min distances
        * Determine the place holders for the directions
        * Set the max and mins for axii
        * Format the scales of the axii
        * Plot the data
        * Place titles and labels on plot
    Output:
        This function does not return a value
"""
def CoupledTwoBody3DPlotPos(massList, ic, t0, tn, m1Name, m2Name):
    # Solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = CoupledTwoBodySolver(massList, ic, t0, tn)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Max pos
    maxDistX = max(max([pos[0] for pos in mass1Pos]), max([pos[0] for pos in mass2Pos])) * 1.1
    maxDistY = max(max([pos[1] for pos in mass1Pos]), max([pos[1] for pos in mass2Pos])) * 1.1
    maxDistZ = max(max([pos[2] for pos in mass1Pos]), max([pos[2] for pos in mass2Pos])) * 1.1
    # Set max and min
    ax.set_xlim(-maxDistX, maxDistX)
    ax.set_ylim(-maxDistY, maxDistY)
    ax.set_zlim(-maxDistZ, maxDistZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.zaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Plot
    ax.plot(mass1Pos[0], mass1Pos[1], mass1Pos[2], 'o', color = 'green', markersize = '2', label = m1Name)
    ax.plot(mass2Pos[0], mass2Pos[1], mass2Pos[2], 'o', color = 'blue', markersize = '1', label = m2Name)
    # Title and labels
    ax.set_title(f"3D Position Plot Of Two Coupled Bodies", fontsize = THREEDPLOTTILE)
    ax.set_xlabel(f"$x$ Position In (m)", fontsize = THREEDPLOTLABELS)
    ax.set_ylabel(f"$y$ Position In (m)", fontsize = THREEDPLOTLABELS)
    ax.set_zlabel(f"$z$ Position In (m)", fontsize = THREEDPLOTLABELS)
    ax.legend()
    ax.grid(False)
    plt.show()

""" CoupledTwoBody3DAnimPos - Plots the positions of two bodies in space as an animation in 3D
    Input:
        massList - Array of masses in the system
        ic - Matrix of initial conditions:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial velocity of mass 1 in x
            ic[2][1] - Initial velocity of mass 1 in y
            ic[2][2] - Initial velocity of mass 1 in z
            ic[3][0] - Initial velocity of mass 2 in x
            ic[3][1] - Initial velocity of mass 2 in y
            ic[3][2] - Initial velocity of mass 2 in z
        t0 - Initial time in system
        tn - Final time in system
        m1Name - Name of mass 1
        m2Name - Name of mass 2
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min positions
        * Determine the place holders for the directions
        * Set the max and min for the axii
        * Format the scales of the axii
        * Set up the animation parameters
        * Define the init function
        * Define the animation function
        * Call the animation
        * Set the title and labels
    Output:
        This function does not return a value
"""
def CoupledTwoBody3DAnimPos(massList, ic, t0, tn, m1Name, m2Name):
    # Solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = CoupledTwoBodySolver(massList, ic, t0, tn)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Max pos
    maxDistX = max(max([pos[0] for pos in mass1Pos]), max([pos[0] for pos in mass2Pos])) * 1.1
    maxDistY = max(max([pos[1] for pos in mass1Pos]), max([pos[1] for pos in mass2Pos])) * 1.1
    maxDistZ = max(max([pos[2] for pos in mass1Pos]), max([pos[2] for pos in mass2Pos])) * 1.1
    # Set max and min
    ax.set_xlim(-maxDistX, maxDistX)
    ax.set_ylim(-maxDistY, maxDistY)
    ax.set_zlim(-maxDistZ, maxDistZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.zaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Animation parameters
    Mass1, = ax.plot([], [], [], 'o', color = 'green', markersize = 2, label = m1Name)
    Mass2, = ax.plot([], [], [], 'o', color = 'blue', markersize = 1, label = m2Name)
    Mass1Trail, = ax.plot([], [], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
    Mass2Trail, = ax.plot([], [], [], '-', color='blue', linewidth = 1, alpha=0.5)
    # Init Inner Function
    def init():
        Mass1.set_data([], [])
        Mass1.set_3d_properties([])
        Mass2.set_data([], [])
        Mass2.set_3d_properties([])
        Mass1Trail.set_data([], [])
        Mass2Trail.set_data([], [])
        return Mass1, Mass2, Mass1Trail, Mass2Trail
    # Animate Inner Function
    def animate(k):
        Mass1.set_data([mass1Pos[0][k]], [mass1Pos[1][k]])
        Mass1.set_3d_properties([mass1Pos[2][k]])
        Mass2.set_data([mass2Pos[0][k]], [mass2Pos[1][k]])
        Mass2.set_3d_properties([mass2Pos[2][k]])
        Mass1Trail.set_data(mass1Pos[0][:k+1], mass1Pos[1][:k+1])
        Mass1Trail.set_3d_properties(mass1Pos[2][:k+1])
        Mass2Trail.set_data(mass2Pos[0][:k+1], mass2Pos[1][:k+1])
        Mass2Trail.set_3d_properties(mass2Pos[2][:k+1])
        return Mass1, Mass2, Mass1Trail, Mass2Trail
    # Animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(mass1Pos[0]), interval=1e-5, blit=True, repeat=True)
    ax.set_title(f"3D Position Animation Of Two Coupled Bodies", fontsize = THREEDANIMTILE)
    ax.set_xlabel(f"$x$ Position In (m)", fontsize = THREEDANIMLABELS)
    ax.set_ylabel(f"$y$ Position In (m)", fontsize = THREEDANIMLABELS)
    ax.set_zlabel(f"$z$ Position In (m)", fontsize = THREEDANIMLABELS)
    ax.legend()
    ax.grid(False)
    plt.show()

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Two Body 3D Velocity
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" CoupledTwoBody3DPlotVel - Plots the velocities of two bodies in space in 3D
    Input:
        massList - Array of masses in the system
        ic - Matrix of initial conditions:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial velocity of mass 1 in x
            ic[2][1] - Initial velocity of mass 1 in y
            ic[2][2] - Initial velocity of mass 1 in z
            ic[3][0] - Initial velocity of mass 2 in x
            ic[3][1] - Initial velocity of mass 2 in y
            ic[3][2] - Initial velocity of mass 2 in z
        t0 - Initial time in system
        tn - Final time in system
        i - Index used for accessing elements in the lists returned from the RK4 solver
        j - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x velocity
            1 - Corresponds to y velocity
            2 - Corresponds to z velocity
        m1Name - Name of mass 1
        m2Name - Name of mass 2
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min velocities
        * Determine the place holders for the directions
        * Set the max and mins for axii
        * Format the scales of the axii
        * Plot the data
        * Place titles and labels on plot
    Output:
        This function does not return a value
"""
def CoupledTwoBody3DPlotVel(massList, ic, t0, tn, i, j, m1Name, m2Name):
    # Solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = CoupledTwoBodySolver(massList, ic, t0, tn)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Max vel
    maxVelX = max(max([vel[0] for vel in mass1Vel]), max([vel[0] for vel in mass2Vel])) * 1.1
    maxVelY = max(max([vel[1] for vel in mass1Vel]), max([vel[1] for vel in mass2Vel])) * 1.1
    maxVelZ = max(max([vel[2] for vel in mass1Vel]), max([vel[2] for vel in mass2Vel])) * 1.1
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax = plt.gca()
    ax.zaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Direction place holder
    ax.set_xlim((tn - 1.05 * tn), 1.05 * tn)
    iVelocity = ''
    jVelocity = ''
    if (i == 0):
        iVelocity = "$v_{x}$"
        ax.set_ylim(-maxVelX, maxVelX)
    elif (i == 1):
        iVelocity = "$v_{y}$"
        ax.set_ylim(-maxVelY, maxVelY)
    elif (i == 2):
        iVelocity = "$v_{z}$"
        ax.set_ylim(-maxVelZ, maxVelZ)
    if (j == 0):
        jVelocity = "$v_{x}$"
        ax.set_zlim(-maxVelX, maxVelX)
    elif (j == 1):
        jVelocity = "$v_{y}$"
        ax.set_zlim(-maxVelY, maxVelY)
    elif (j == 2):
        jVelocity = "$v_{z}$"
        ax.set_zlim(-maxVelZ, maxVelZ)
    # Plot
    ax.plot(time, mass1Vel[i], mass1Vel[j], 'o', color = 'green', markersize = '1', label = m1Name)
    ax.plot(time, mass2Vel[i], mass2Vel[j], 'o', color = 'blue', markersize = '1', label = m2Name)
    # Title and labels
    ax.set_title(f"3D Velocity Plot Of Two Coupled Bodies - {jVelocity} And {iVelocity} vs. Time", fontsize = THREEDPLOTTILE)
    ax.set_xlabel("Time In (s)", fontsize = THREEDPLOTLABELS)
    ax.set_ylabel(f"Velocity ({iVelocity}) In (m/s)", fontsize = THREEDPLOTLABELS)
    ax.set_zlabel(f"Velocity ({jVelocity}) In (m/s)", fontsize = THREEDPLOTLABELS)
    ax.legend()
    ax.grid(False)
    plt.show()

""" CoupledTwoBody3DAnimVel - Plots the velocity vs. time of two bodies in space as an animation in 3D
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial velocity of mass 1 in x
            ic[2][1] - Initial velocity of mass 1 in y
            ic[2][2] - Initial velocity of mass 1 in z
            ic[3][0] - Initial velocity of mass 2 in x
            ic[3][1] - Initial velocity of mass 2 in y
            ic[3][2] - Initial velocity of mass 2 in z
        t0 - Initial time in system
        tn - Final time in system
        i - Index used for accessing elements in the lists returned from the RK4 solver
        j - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x velocity
            1 - Corresponds to y velocity
            2 - Corresponds to z velocity
        m1Name - Name of mass 1
        m2Name - Name of mass 2
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min velocities
        * Determine the place holders for the directions
        * Set the max and min for the axii
        * Format the scales of the axii
        * Set up the animation parameters
        * Define the init function
        * Define the animation function
        * Call the animation
        * Set the title and labels
    Output:
        This function does not return a value
"""
def CoupledTwoBody3DAnimVel(massList, ic, t0, tn, i, j, m1Name, m2Name):
    # Solver
    mass1Pos, mass2Pos, mass1Vel, mass2Vel, time = CoupledTwoBodySolver(massList, ic, t0, tn)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Max vel
    maxVelX = max(max([vel[0] for vel in mass1Vel]), max([vel[0] for vel in mass2Vel])) * 1.1
    maxVelY = max(max([vel[1] for vel in mass1Vel]), max([vel[1] for vel in mass2Vel])) * 1.1
    maxVelZ = max(max([vel[2] for vel in mass1Vel]), max([vel[2] for vel in mass2Vel])) * 1.1
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax = plt.gca()
    ax.zaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Direction place holder
    ax.set_xlim((tn - 1.05 * tn), 1.05 * tn)
    iVelocity = ''
    jVelocity = ''
    if (i == 0):
        iVelocity = "$v_{x}$"
        ax.set_ylim(-maxVelX, maxVelX)
    elif (i == 1):
        iVelocity = "$v_{y}$"
        ax.set_ylim(-maxVelY, maxVelY)
    elif (i == 2):
        iVelocity = "$v_{z}$"
        ax.set_ylim(-maxVelZ, maxVelZ)
    if (j == 0):
        jVelocity = "$v_{x}$"
        ax.set_zlim(-maxVelX, maxVelX)
    elif (j == 1):
        jVelocity = "$v_{y}$"
        ax.set_zlim(-maxVelY, maxVelY)
    elif (j == 2):
        jVelocity = "$v_{z}$"
        ax.set_zlim(-maxVelZ, maxVelZ)
    # Animation parameters
    Mass1, = ax.plot([], [], [], 'o', color = 'green', markersize = 2, label = m1Name)
    Mass2, = ax.plot([], [], [], 'o', color = 'blue', markersize = 1, label = m2Name)
    Mass1Trail, = ax.plot([], [], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
    Mass2Trail, = ax.plot([], [], [], '-', color='blue', linewidth = 1, alpha=0.5)
    # Init Inner Function
    def init():
        Mass1.set_data([], [])
        Mass1.set_3d_properties([])
        Mass2.set_data([], [])
        Mass2.set_3d_properties([])
        Mass1Trail.set_data([], [])
        Mass2Trail.set_data([], [])
        return Mass1, Mass2, Mass1Trail, Mass2Trail
    # Animate Inner Function
    def animate(k):
        Mass1.set_data([time[k]], [mass1Vel[i][k]])
        Mass1.set_3d_properties([mass1Vel[j][k]])
        Mass2.set_data([time[k]], [mass2Vel[i][k]])
        Mass2.set_3d_properties([mass2Vel[j][k]])
        Mass1Trail.set_data(time[:k+1], mass1Vel[i][:k+1])
        Mass1Trail.set_3d_properties(mass1Vel[j][:k+1])
        Mass2Trail.set_data(time[:k+1], mass2Vel[i][:k+1])
        Mass2Trail.set_3d_properties(mass2Vel[j][:k+1])
        return Mass1, Mass2, Mass1Trail, Mass2Trail
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((-1, 1))
    ax.yaxis.set_major_formatter(formatter)
    ax.zaxis.set_major_formatter(formatter)
    # Animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(mass1Vel[0]), interval=1e-5, blit=True, repeat=True)
    # Title and labels
    ax.set_title(f"3D Velocity Animation Of Two Coupled Bodies - {jVelocity} And {iVelocity} vs. Time", fontsize = THREEDANIMTILE)
    ax.set_xlabel("Time In (s)", fontsize = THREEDPLOTLABELS)
    ax.set_ylabel(f"Velocity ({iVelocity}) In (m/s)", fontsize = THREEDPLOTLABELS)
    ax.set_zlabel(f"Velocity ({jVelocity}) In (m/s)", fontsize = THREEDPLOTLABELS)
    ax.legend()
    ax.grid(False)
    plt.show()

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 
##### Three Bodies
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### ##### 

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Three Body 2D Position
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" CoupledThreeBody2DPlotPos - Plots the positions of three bodies in space in 2D
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions for masses in system:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial x position of mass 3
            ic[2][1] - Initial y position of mass 3
            ic[2][2] - Initial z position of mass 3
            ic[3][0] - Initial velocity of mass 1 in x
            ic[3][1] - Initial velocity of mass 1 in y
            ic[3][2] - Initial velocity of mass 1 in z
            ic[4][0] - Initial velocity of mass 2 in x
            ic[4][1] - Initial velocity of mass 2 in y
            ic[4][2] - Initial velocity of mass 2 in z
            ic[5][0] - Initial velocity of mass 3 in x
            ic[5][1] - Initial velocity of mass 3 in y
            ic[5][2] - Initial velocity of mass 3 in z
        t0 - Initial time of system
        tn - Final time of system
        i - Index used for accessing elements in the lists returned from the RK4 solver
        j - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x direction
            1 - Corresponds to y direction
            2 - Corresponds to z direction
        m1Name - Name of mass 1
        m2Name - Name of mass 2
        m3Name - Name of mass 3
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min distances
        * Determine the place holders for the directions
        * Set the max and mins for axii
        * Format the scales of the axii
        * Plot the data
        * Place titles and labels on plot
    Output:
        This function does not return a value
"""
def CoupledThreeBody2DPlotPos(massList, ic, t0, tn, i, j, m1Name, m2Name, m3name):
    # Solver
    mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time = CoupledThreeBodySolver(massList, ic, t0, tn)
    # Max pos
    maxDistX = max(max([pos[0] for pos in mass1Pos]), max([pos[0] for pos in mass2Pos])) * 1.1
    maxDistY = max(max([pos[1] for pos in mass1Pos]), max([pos[1] for pos in mass2Pos])) * 1.1
    maxDistZ = max(max([pos[2] for pos in mass1Pos]), max([pos[2] for pos in mass2Pos])) * 1.1
    # Direction place holder
    iDirection = ''
    jDirection = ''
    if (i == 0):
        iDirection = "$x$"
        plt.xlim(-maxDistX, maxDistX)
    elif (i == 1):
        iDirection = "$y$"
        plt.xlim(-maxDistY, maxDistY)
    elif (i == 2):
        iDirection = "$z$"
        plt.xlim(-maxDistZ, maxDistZ)
    if (j == 0):
        jDirection = "$x$"
        plt.ylim(-maxDistX, maxDistX)
    elif (j == 1):
        jDirection = "$y$"
        plt.ylim(-maxDistY, maxDistY)
    elif (j == 2):
        jDirection = "$z$"
        plt.ylim(-maxDistZ, maxDistZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax = plt.gca()
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Plot
    plt.plot(mass1Pos[i], mass1Pos[j], 'o', color = "green", markersize = '3', label = m1Name)
    plt.plot(mass2Pos[i], mass2Pos[j], 'o', color = "blue", markersize = '2', label = m2Name)
    plt.plot(mass3Pos[i], mass3Pos[j], 'o', color = "red", markersize = '1', label = m3name)
    # Title and labels
    plt.title(f"2D Position Plot Of Three Coupled Bodies - {jDirection} vs. {iDirection}", fontsize = TWODPLOTTITLE)
    plt.xlabel(f"{iDirection} Position In (m)", fontsize = TWODPLOTABELS)
    plt.ylabel(f"{jDirection} Position In (m)", fontsize = TWODPLOTABELS)
    plt.legend()
    plt.show()

""" CoupledThreeBody2DAnimPos - Plots the positions of three bodies in space as an animation in 2D
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions for masses in system:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial x position of mass 3
            ic[2][1] - Initial y position of mass 3
            ic[2][2] - Initial z position of mass 3
            ic[3][0] - Initial velocity of mass 1 in x
            ic[3][1] - Initial velocity of mass 1 in y
            ic[3][2] - Initial velocity of mass 1 in z
            ic[4][0] - Initial velocity of mass 2 in x
            ic[4][1] - Initial velocity of mass 2 in y
            ic[4][2] - Initial velocity of mass 2 in z
            ic[5][0] - Initial velocity of mass 3 in x
            ic[5][1] - Initial velocity of mass 3 in y
            ic[5][2] - Initial velocity of mass 3 in z
        t0 - Initial time of system
        tn - Final time of system
        i - Index used for accessing elements in the lists returned from the RK4 solver
        j - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x direction
            1 - Corresponds to y direction
            2 - Corresponds to z direction
        m1Name - Name of mass 1
        m2Name - Name of mass 2
        m3Name - Name of mass 3
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min positions
        * Determine the place holders for the directions
        * Set the max and min for the axii
        * Format the scales of the axii
        * Set up the animation parameters
        * Define the init function
        * Define the animation function
        * Call the animation
        * Set the title and labels
    Output:
        This function does not return a value
"""
def CoupledThreeBody2DAnimPos(massList, ic, t0, tn, i, j, m1Name, m2Name, m3Name):
    # Solver
    mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time = CoupledThreeBodySolver(massList, ic, t0, tn)
    fig, ax = plt.subplots()
    # Max pos
    maxDistX = max(max([pos[0] for pos in mass1Pos]), max([pos[0] for pos in mass2Pos]), max([pos[0] for pos in mass3Pos])) * 1.1
    maxDistY = max(max([pos[1] for pos in mass1Pos]), max([pos[1] for pos in mass2Pos]), max([pos[1] for pos in mass3Pos])) * 1.1
    maxDistZ = max(max([pos[2] for pos in mass1Pos]), max([pos[2] for pos in mass2Pos]), max([pos[2] for pos in mass3Pos])) * 1.1
    # Direction place holder
    iDirection = ''
    jDirection = ''
    if (i == 0):
        iDirection = "$x$"
        ax.set_xlim(-maxDistX, maxDistX)
    elif (i == 1):
        iDirection = "$y$"
        ax.set_xlim(-maxDistY, maxDistY)
    elif (i == 2):
        iDirection = "$z$"
        ax.set_xlim(-maxDistZ, maxDistZ)
    if (j == 0):
        jDirection = "$x$"
        ax.set_ylim(-maxDistX, maxDistX)
    elif (j == 1):
        jDirection = "$y$"
        ax.set_ylim(-maxDistY, maxDistY)
    elif (j == 0):
        jDirection = "$z$"
        ax.set_ylim(-maxDistZ, maxDistZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Animation parameters
    Mass1, = ax.plot([], [], 'o', color = 'green', markersize = 3, label = m1Name)
    Mass2, = ax.plot([], [], 'o', color = 'blue', markersize = 2, label = m2Name)
    Mass3, = ax.plot([], [], 'o', color = 'red', markersize = 1, label = m3Name)
    Mass1Trail, = ax.plot([], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
    Mass2Trail, = ax.plot([], [], '-', color='blue', linewidth = 1, alpha=0.5)
    Mass3Trail, = ax.plot([], [], '-', color='red', linewidth = 1, alpha=0.5)
    # Init Inner Function
    def init():
        Mass1.set_data([], [])
        Mass2.set_data([], [])
        Mass3.set_data([], [])
        Mass1Trail.set_data([], [])
        Mass2Trail.set_data([], [])
        Mass3Trail.set_data([], [])
        return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail
    # Animate Inner Function
    def animate(k):
        Mass1.set_data([mass1Pos[i][k]], [mass1Pos[j][k]])
        Mass2.set_data([mass2Pos[i][k]], [mass2Pos[j][k]])
        Mass3.set_data([mass3Pos[i][k]], [mass3Pos[j][k]])
        Mass1Trail.set_data(mass1Pos[i][:k+1], mass1Pos[j][:k+1])
        Mass2Trail.set_data(mass2Pos[i][:k+1], mass2Pos[j][:k+1])
        Mass3Trail.set_data(mass3Pos[i][:k+1], mass3Pos[j][:k+1])
        return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail
    # Animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(mass1Pos[0]), interval=1e-5, blit=True, repeat=True)
    # Title and labels
    ax.set_title(f"2D Position Animation Of Three Coupled Bodies - {jDirection} vs. {iDirection}", fontsize = TWODPLOTTITLE)
    ax.set_xlabel(f"{iDirection} Position In (m)", fontsize = TWODPLOTABELS)
    ax.set_ylabel(f"{jDirection} Position In (m)", fontsize = TWODPLOTABELS)
    ax.legend()
    plt.show()

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Three Body 2D Velocity
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" CoupledThreeBody2DPlotVel - Plots the velocity vs. time of three bodies in space in 2D
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions for masses in system:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial x position of mass 3
            ic[2][1] - Initial y position of mass 3
            ic[2][2] - Initial z position of mass 3
            ic[3][0] - Initial velocity of mass 1 in x
            ic[3][1] - Initial velocity of mass 1 in y
            ic[3][2] - Initial velocity of mass 1 in z
            ic[4][0] - Initial velocity of mass 2 in x
            ic[4][1] - Initial velocity of mass 2 in y
            ic[4][2] - Initial velocity of mass 2 in z
            ic[5][0] - Initial velocity of mass 3 in x
            ic[5][1] - Initial velocity of mass 3 in y
            ic[5][2] - Initial velocity of mass 3 in z
        t0 - Initial time in the system
        tn - Final time in the system
        i - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x velocity
            1 - Corresponds to y velocity
            2 - Corresponds to z velocity
        m1Name - Name of mass 1
        m2Name - Name of mass 2
        m3Name - Name of mass 3
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min velocities
        * Determine the place holders for the directions
        * Set the max and mins for axii
        * Format the scales of the axii
        * Plot the data
        * Place titles and labels on plot
    Output:
        This function does not return a value
"""
def CoupledThreeBody2DPlotVel(massList, ic, t0, tn, i, m1Name, m2Name, m3Name):
    # Solver
    mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time = CoupledThreeBodySolver(massList, ic, t0, tn)
    # Max velocity
    maxVelX = max(max([vel[0] for vel in mass1Vel]), max([vel[0] for vel in mass2Vel]), max([vel[0] for vel in mass3Vel])) * 1.1
    maxVelY = max(max([vel[1] for vel in mass1Vel]), max([vel[1] for vel in mass2Vel]), max([vel[0] for vel in mass2Vel])) * 1.1
    maxVelZ = max(max([vel[2] for vel in mass1Vel]), max([vel[2] for vel in mass2Vel]), max([vel[0] for vel in mass2Vel])) * 1.1
    # Direction place holder
    plt.xlim((tn - 1.05 * tn), 1.05 * tn)
    iVelocity = ''
    if (i == 0):
        iVelocity = "$v_{x}$"
        plt.ylim(-maxVelX, maxVelX)
    elif (i == 1):
        iVelocity = "$v_{y}$"
        plt.ylim(-maxVelY, maxVelY)
    elif (i == 2):
        iVelocity = "$v_{z}$"
        plt.ylim(-maxVelZ, maxVelZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax = plt.gca()
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Plot
    plt.plot(time, mass1Vel[i], 'o', color = "green", markersize = '1', label = m1Name)
    plt.plot(time, mass2Vel[i], 'o', color = "blue", markersize = '1', label = m2Name)
    plt.plot(time, mass3Vel[i], 'o', color = "red", markersize = '1', label = m3Name)
    # Title and labels
    plt.title(f"2D Velocity Plot Of Two Coupled Bodies - {iVelocity} vs. Time", fontsize = TWODPLOTTITLE)
    plt.xlabel(f"Time In $(s)$", fontsize = TWODPLOTABELS)
    plt.ylabel(f"Velocity ({iVelocity}) In $\\frac{{m}}{{s}}$", fontsize = TWODPLOTABELS)
    plt.legend()
    plt.show()

""" CoupledThreeBody2DAnimVel - Plots the velocities of three bodies in space as an animation
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions for masses in system:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial x position of mass 3
            ic[2][1] - Initial y position of mass 3
            ic[2][2] - Initial z position of mass 3
            ic[3][0] - Initial velocity of mass 1 in x
            ic[3][1] - Initial velocity of mass 1 in y
            ic[3][2] - Initial velocity of mass 1 in z
            ic[4][0] - Initial velocity of mass 2 in x
            ic[4][1] - Initial velocity of mass 2 in y
            ic[4][2] - Initial velocity of mass 2 in z
            ic[5][0] - Initial velocity of mass 3 in x
            ic[5][1] - Initial velocity of mass 3 in y
            ic[5][2] - Initial velocity of mass 3 in z
        t0 - Initial time of system
        tn - Final time of system
        i - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x velocity
            1 - Corresponds to y velocity
            2 - Corresponds to z velocity
        m1Name - Name of mass 1
        m2Name - Name of mass 2
        m3Name - Name of mass 3
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min positions
        * Determine the place holders for the directions
        * Set the max and min for the axii
        * Format the scales of the axii
        * Set up the animation parameters
        * Define the init function
        * Define the animation function
        * Call the animation
        * Set the title and labels
    Output:
        This function does not return a value
"""
def CoupledThreeBody2DAnimVel(massList, ic, t0, tn, i, m1Name, m2Name, m3Name):
    # Solver
    mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time = CoupledThreeBodySolver(massList, ic, t0, tn)
    fig, ax = plt.subplots()
    # Max pos
    maxVelX = max(max([vel[0] for vel in mass1Vel]), max([vel[0] for vel in mass2Vel]), max([vel[0] for vel in mass3Vel])) * 1.1
    maxVelY = max(max([vel[1] for vel in mass1Vel]), max([vel[1] for vel in mass2Vel]), max([vel[1] for vel in mass3Vel])) * 1.1
    maxVelZ = max(max([vel[2] for vel in mass1Vel]), max([vel[2] for vel in mass2Vel]), max([vel[2] for vel in mass3Vel])) * 1.1
    # Direction place holder
    ax.set_xlim((tn - 1.05 * tn), 1.05 * tn)
    iVelocity = ''
    if (i == 0):
        iVelocity = "$v_{x}$"
        plt.ylim(-maxVelX, maxVelX)
    elif (i == 1):
        iVelocity = "$v_{y}$"
        plt.ylim(-maxVelY, maxVelY)
    elif (i == 2):
        iVelocity = "$v_{z}$"
        plt.ylim(-maxVelZ, maxVelZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Animation parameters
    Mass1, = ax.plot([], [], 'o', color = 'green', markersize = 3, label = m1Name)
    Mass2, = ax.plot([], [], 'o', color = 'blue', markersize = 2, label = m2Name)
    Mass3, = ax.plot([], [], 'o', color = 'red', markersize = 1, label = m3Name)
    Mass1Trail, = ax.plot([], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
    Mass2Trail, = ax.plot([], [], '-', color='blue', linewidth = 1, alpha=0.5)
    Mass3Trail, = ax.plot([], [], '-', color='red', linewidth = 1, alpha=0.5)
    # Init Inner Function
    def init():
        Mass1.set_data([], [])
        Mass2.set_data([], [])
        Mass3.set_data([], [])
        Mass1Trail.set_data([], [])
        Mass2Trail.set_data([], [])
        Mass3Trail.set_data([], [])
        return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail
    # Animate Inner Function
    def animate(k):
        Mass1.set_data([time[k]], [mass1Vel[i][k]])
        Mass2.set_data([time[k]], [mass2Vel[i][k]])
        Mass3.set_data([time[k]], [mass3Vel[i][k]])
        Mass1Trail.set_data(time[:k+1], mass1Vel[i][:k+1])
        Mass2Trail.set_data(time[:k+1], mass2Vel[i][:k+1])
        Mass3Trail.set_data(time[:k+1], mass3Vel[i][:k+1])
        return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail
    # Animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(mass1Vel[0]), interval=1e-5, blit=True, repeat=True)
    # Title and labels
    ax.set_title(f"2D Velocity Animation Of Three Coupled Bodies - {iVelocity} vs. Time", fontsize = TWODANIMTITLE)
    ax.set_xlabel(f"Time In $(s)$", fontsize = TWODANIMLABELS)
    ax.set_ylabel(f"Velocity ({iVelocity}) In $\\frac{{m}}{{s}}$", fontsize = TWODANIMLABELS)
    ax.legend()
    plt.show()

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Three Body 3D Position
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" CoupledThreeBody3DPlotPos - Plots the positions of three bodies in space
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions for masses in system:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial x position of mass 3
            ic[2][1] - Initial y position of mass 3
            ic[2][2] - Initial z position of mass 3
            ic[3][0] - Initial velocity of mass 1 in x
            ic[3][1] - Initial velocity of mass 1 in y
            ic[3][2] - Initial velocity of mass 1 in z
            ic[4][0] - Initial velocity of mass 2 in x
            ic[4][1] - Initial velocity of mass 2 in y
            ic[4][2] - Initial velocity of mass 2 in z
            ic[5][0] - Initial velocity of mass 3 in x
            ic[5][1] - Initial velocity of mass 3 in y
            ic[5][2] - Initial velocity of mass 3 in z
        t0 - Initial time of system
        tn - Final time of system
        m1Name - Name of mass 1
        m2Name - Name of mass 2
        m3Name - Name of mass 3
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min distances
        * Determine the place holders for the directions
        * Set the max and mins for axii
        * Format the scales of the axii
        * Plot the data
        * Place titles and labels on plot
    Output:
        This function does not return a value
"""
def CoupledThreeBody3DPlotPos(massList, ic, t0, tn, m1Name, m2Name, m3name):
    # Solver
    mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time = CoupledThreeBodySolver(massList, ic, t0, tn)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Max pos
    maxDistX = max(max([pos[0] for pos in mass1Pos]), max([pos[0] for pos in mass2Pos]), max([pos[0] for pos in mass3Pos])) * 1.1
    maxDistY = max(max([pos[1] for pos in mass1Pos]), max([pos[1] for pos in mass2Pos]), max([pos[1] for pos in mass3Pos])) * 1.1
    maxDistZ = max(max([pos[2] for pos in mass1Pos]), max([pos[2] for pos in mass2Pos]), max([pos[2] for pos in mass3Pos])) * 1.1
    # Set max and min
    ax.set_xlim(-maxDistX, maxDistX)
    ax.set_ylim(-maxDistY, maxDistY)
    ax.set_zlim(-maxDistZ, maxDistZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.zaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Plot
    ax.plot(mass1Pos[0], mass1Pos[1], mass1Pos[2], 'o', color = 'green', markersize = '3', label = m1Name)
    ax.plot(mass2Pos[0], mass2Pos[1], mass2Pos[2], 'o', color = 'blue', markersize = '2', label = m2Name)
    ax.plot(mass3Pos[0], mass3Pos[1], mass3Pos[2], 'o', color = 'red', markersize = '1', label = m3name)
    # Title and labels
    ax.set_title(f"3D Position Plot Of Three Coupled Bodies", fontsize = THREEDPLOTTILE)
    ax.set_xlabel(f"$x$ Position In (m)", fontsize = THREEDPLOTLABELS)
    ax.set_ylabel(f"$y$ Position In (m)", fontsize = THREEDPLOTLABELS)
    ax.set_zlabel(f"$z$ Position In (m)", fontsize = THREEDPLOTLABELS)
    ax.legend()
    ax.grid(False)
    plt.show()

""" CoupledThreeBody3DAnimPos - Plots the positions of three bodies in space in 3D as an animation
    Input:
        massList - Array of masses in the system
        ic - Matrix of initial conditions for masses in system:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial x position of mass 3
            ic[2][1] - Initial y position of mass 3
            ic[2][2] - Initial z position of mass 3
            ic[3][0] - Initial velocity of mass 1 in x
            ic[3][1] - Initial velocity of mass 1 in y
            ic[3][2] - Initial velocity of mass 1 in z
            ic[4][0] - Initial velocity of mass 2 in x
            ic[4][1] - Initial velocity of mass 2 in y
            ic[4][2] - Initial velocity of mass 2 in z
            ic[5][0] - Initial velocity of mass 3 in x
            ic[5][1] - Initial velocity of mass 3 in y
            ic[5][2] - Initial velocity of mass 3 in z
        t0 - Initial time in system
        tn - Final time in system
        m1Name - Name of mass 1
        m2Name - Name of mass 2
        m3Name - Name of mass 3
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min positions
        * Determine the place holders for the directions
        * Set the max and min for the axii
        * Format the scales of the axii
        * Set up the animation parameters
        * Define the init function
        * Define the animation function
        * Call the animation
        * Set the title and labels
    Output:
        This function does not return a value
"""
def CoupledThreeBody3DAnimPos(massList, ic, t0, tn, m1Name, m2Name, m3Name):
    # Solver
    mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time = CoupledThreeBodySolver(massList, ic, t0, tn)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Max pos
    maxDistX = max(max([pos[0] for pos in mass1Pos]), max([pos[0] for pos in mass2Pos]), max([pos[0] for pos in mass3Pos])) * 1.1
    maxDistY = max(max([pos[1] for pos in mass1Pos]), max([pos[1] for pos in mass2Pos]), max([pos[1] for pos in mass3Pos])) * 1.1
    maxDistZ = max(max([pos[2] for pos in mass1Pos]), max([pos[2] for pos in mass2Pos]), max([pos[2] for pos in mass3Pos])) * 1.1
    # Set max and min
    ax.set_xlim(-maxDistX, maxDistX)
    ax.set_ylim(-maxDistY, maxDistY)
    ax.set_zlim(-maxDistZ, maxDistZ)
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.zaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Animation parameters
    Mass1, = ax.plot([], [], [], 'o', color = 'green', markersize = 3, label = m1Name)
    Mass2, = ax.plot([], [], [], 'o', color = 'blue', markersize = 2, label = m2Name)
    Mass3, = ax.plot([], [], [], 'o', color = 'red', markersize = 1, label = m3Name)
    Mass1Trail, = ax.plot([], [], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
    Mass2Trail, = ax.plot([], [], [], '-', color='blue', linewidth = 1, alpha=0.5)
    Mass3Trail, = ax.plot([], [], [], '-', color='red', linewidth = 1, alpha=0.5)
    # Init Inner Function
    def init():
        Mass1.set_data([], [])
        Mass1.set_3d_properties([])
        Mass2.set_data([], [])
        Mass2.set_3d_properties([])
        Mass3.set_data([], [])
        Mass3.set_3d_properties([])
        Mass1Trail.set_data([], [])
        Mass2Trail.set_data([], [])
        Mass3Trail.set_data([], [])
        return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail
    # Animate Inner Function
    def animate(k):
        Mass1.set_data([mass1Pos[0][k]], [mass1Pos[1][k]])
        Mass1.set_3d_properties([mass1Pos[2][k]])
        Mass2.set_data([mass2Pos[0][k]], [mass2Pos[1][k]])
        Mass2.set_3d_properties([mass2Pos[2][k]])
        Mass3.set_data([mass3Pos[0][k]], [mass3Pos[1][k]])
        Mass3.set_3d_properties([mass3Pos[2][k]])
        Mass1Trail.set_data(mass1Pos[0][:k+1], mass1Pos[1][:k+1])
        Mass1Trail.set_3d_properties(mass1Pos[2][:k+1])
        Mass2Trail.set_data(mass2Pos[0][:k+1], mass2Pos[1][:k+1])
        Mass2Trail.set_3d_properties(mass2Pos[2][:k+1])
        Mass3Trail.set_data(mass3Pos[0][:k+1], mass3Pos[1][:k+1])
        Mass3Trail.set_3d_properties(mass3Pos[2][:k+1])
        return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail
    # Animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(mass1Pos[0]), interval=1e-5, blit=True, repeat=True)
    ax.set_title(f"3D Position Animation Of Three Coupled Bodies", fontsize = THREEDANIMTILE)
    ax.set_xlabel(f"$x$ Position In (m)", fontsize = THREEDANIMLABELS)
    ax.set_ylabel(f"$y$ Position In (m)", fontsize = THREEDANIMLABELS)
    ax.set_zlabel(f"$z$ Position In (m)", fontsize = THREEDANIMLABELS)
    ax.legend()
    ax.grid(False)
    plt.show()

##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Three Body 3D Velocity
##### ##### ##### ##### ##### ##### ##### ##### ##### #####

""" CoupledThreeBody3DPlotVel - Plots the velocities of three bodies in space in 3D
    Input:
        massList - Array of masses in the system
        ic - Matrix of initial conditions for masses in system:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial x position of mass 3
            ic[2][1] - Initial y position of mass 3
            ic[2][2] - Initial z position of mass 3
            ic[3][0] - Initial velocity of mass 1 in x
            ic[3][1] - Initial velocity of mass 1 in y
            ic[3][2] - Initial velocity of mass 1 in z
            ic[4][0] - Initial velocity of mass 2 in x
            ic[4][1] - Initial velocity of mass 2 in y
            ic[4][2] - Initial velocity of mass 2 in z
            ic[5][0] - Initial velocity of mass 3 in x
            ic[5][1] - Initial velocity of mass 3 in y
            ic[5][2] - Initial velocity of mass 3 in z
        t0 - Initial time in system
        tn - Final time in system
        i - Index used for accessing elements in the lists returned from the RK4 solver
        j - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x velocity
            1 - Corresponds to y velocity
            2 - Corresponds to z velocity
        m1Name - Name of mass 1
        m2Name - Name of mass 2
        m3Name - Name of mass 3
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min velocities
        * Determine the place holders for the directions
        * Set the max and mins for axii
        * Format the scales of the axii
        * Plot the data
        * Place titles and labels on plot
    Output:
        This function does not return a value, it plots the positions of three bodies in space
"""
def CoupledThreeBody3DPlotVel(massList, ic, t0, tn, i, j, m1Name, m2Name, m3Name):
    # Solver
    mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time = CoupledThreeBodySolver(massList, ic, t0, tn)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Max vel
    maxVelX = max(max([vel[0] for vel in mass1Vel]), max([vel[0] for vel in mass2Vel]), max([vel[0] for vel in mass3Vel])) * 1.1
    maxVelY = max(max([vel[1] for vel in mass1Vel]), max([vel[1] for vel in mass2Vel]), max([vel[1] for vel in mass3Vel])) * 1.1
    maxVelZ = max(max([vel[2] for vel in mass1Vel]), max([vel[2] for vel in mass2Vel]), max([vel[2] for vel in mass3Vel])) * 1.1
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.zaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Direction place holder
    ax.set_xlim((tn - 1.05 * tn), 1.05 * tn)
    iVelocity = ''
    jVelocity = ''
    if (i == 0):
        iVelocity = "$v_{x}$"
        ax.set_ylim(-maxVelX, maxVelX)
    elif (i == 1):
        iVelocity = "$v_{y}$"
        ax.set_ylim(-maxVelY, maxVelY)
    elif (i == 2):
        iVelocity = "$v_{z}$"
        ax.set_ylim(-maxVelZ, maxVelZ)
    if (j == 0):
        jVelocity = "$v_{x}$"
        ax.set_zlim(-maxVelX, maxVelX)
    elif (j == 1):
        jVelocity = "$v_{y}$"
        ax.set_zlim(-maxVelY, maxVelY)
    elif (j == 2):
        jVelocity = "$v_{z}$"
        ax.set_zlim(-maxVelZ, maxVelZ)
    # Plot
    ax.plot(time, mass1Vel[i], mass1Vel[j], 'o', color = 'green', markersize = '3', label = m1Name)
    ax.plot(time, mass2Vel[i], mass2Vel[j], 'o', color = 'blue', markersize = '2', label = m2Name)
    ax.plot(time, mass3Vel[i], mass3Vel[j], 'o', color = 'red', markersize = '1', label = m3Name)
    # Title and labels
    ax.set_title(f"3D Velocity Plot Of Three Coupled Bodies - {jVelocity} And {iVelocity} vs. Time", fontsize = THREEDPLOTTILE)
    ax.set_xlabel("Time In (s)", fontsize = THREEDPLOTLABELS)
    ax.set_ylabel(f"Velocity ({iVelocity}) In (m/s)", fontsize = THREEDPLOTLABELS)
    ax.set_zlabel(f"Velocity ({jVelocity}) In (m/s)", fontsize = THREEDPLOTLABELS)
    ax.legend()
    ax.grid(False)
    plt.show()

""" CoupledThreeBody3DAnimVel - Plots the velocity vs time of three bodies in space as an animation in 3D
    Input:
        massList - Array of masses in system
        ic - Matrix of initial conditions for masses in system:
            ic[0][0] - Initial x position of mass 1
            ic[0][1] - Initial y position of mass 1
            ic[0][2] - Initial z position of mass 1
            ic[1][0] - Initial x position of mass 2
            ic[1][1] - Initial y position of mass 2
            ic[1][2] - Initial z position of mass 2
            ic[2][0] - Initial x position of mass 3
            ic[2][1] - Initial y position of mass 3
            ic[2][2] - Initial z position of mass 3
            ic[3][0] - Initial velocity of mass 1 in x
            ic[3][1] - Initial velocity of mass 1 in y
            ic[3][2] - Initial velocity of mass 1 in z
            ic[4][0] - Initial velocity of mass 2 in x
            ic[4][1] - Initial velocity of mass 2 in y
            ic[4][2] - Initial velocity of mass 2 in z
            ic[5][0] - Initial velocity of mass 3 in x
            ic[5][1] - Initial velocity of mass 3 in y
            ic[5][2] - Initial velocity of mass 3 in z
        t0 - Initial time in system
        tn - Final time in system
        i - Index used for accessing elements in the lists returned from the RK4 solver
        j - Index used for accessing elements in the lists returned from the RK4 solver
            0 - Corresponds to x velocity
            1 - Corresponds to y velocity
            2 - Corresponds to z velocity
        m1Name - Name of mass 1
        m2Name - Name of mass 2
        m3Name - Name of mass 3
    Algorithm:
        * Call the RK4 solver
        * Calculate the max and min velocities
        * Determine the place holders for the directions
        * Set the max and min for the axii
        * Format the scales of the axii
        * Set up the animation parameters
        * Define the init function
        * Define the animation function
        * Call the animation
        * Set the title and labels
    Output:
        This function does not return a value
"""
def CoupledThreeBody3DAnimVel(massList, ic, t0, tn, i, j, m1Name, m2Name, m3Name):
    # Solver
    mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, time = CoupledThreeBodySolver(massList, ic, t0, tn)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Max vel
    maxVelX = max(max([vel[0] for vel in mass1Vel]), max([vel[0] for vel in mass2Vel]), max([vel[0] for vel in mass3Vel])) * 1.1
    maxVelY = max(max([vel[1] for vel in mass1Vel]), max([vel[1] for vel in mass2Vel]), max([vel[1] for vel in mass3Vel])) * 1.1
    maxVelZ = max(max([vel[2] for vel in mass1Vel]), max([vel[2] for vel in mass2Vel]), max([vel[2] for vel in mass3Vel])) * 1.1
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.zaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Direction place holder
    ax.set_xlim((tn - 1.05 * tn), 1.05 * tn)
    iVelocity = ''
    jVelocity = ''
    if (i == 0):
        iVelocity = "$v_{x}$"
        ax.set_ylim(-maxVelX, maxVelX)
    elif (i == 1):
        iVelocity = "$v_{y}$"
        ax.set_ylim(-maxVelY, maxVelY)
    elif (i == 2):
        iVelocity = "$v_{z}$"
        ax.set_ylim(-maxVelZ, maxVelZ)
    if (j == 0):
        jVelocity = "$v_{x}$"
        ax.set_zlim(-maxVelX, maxVelX)
    elif (j == 1):
        jVelocity = "$v_{y}$"
        ax.set_zlim(-maxVelY, maxVelY)
    elif (j == 2):
        jVelocity = "$v_{z}$"
        ax.set_zlim(-maxVelZ, maxVelZ)
    # Animation parameters
    Mass1, = ax.plot([], [], [], 'o', color = 'green', markersize = 3, label = m1Name)
    Mass2, = ax.plot([], [], [], 'o', color = 'blue', markersize = 2, label = m2Name)
    Mass3, = ax.plot([], [], [], 'o', color = 'red', markersize = 1, label = m3Name)
    Mass1Trail, = ax.plot([], [], [], '-', color = 'green', linewidth = 1, alpha = 0.5)
    Mass2Trail, = ax.plot([], [], [], '-', color='blue', linewidth = 1, alpha=0.5)
    Mass3Trail, = ax.plot([], [], [], '-', color='red', linewidth = 1, alpha=0.5)
    # Init Inner Function
    def init():
        Mass1.set_data([], [])
        Mass1.set_3d_properties([])
        Mass2.set_data([], [])
        Mass2.set_3d_properties([])
        Mass3.set_data([], [])
        Mass3.set_3d_properties([])
        Mass1Trail.set_data([], [])
        Mass2Trail.set_data([], [])
        Mass3Trail.set_data([], [])
        return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail
    # Animate Inner Function
    def animate(k):
        Mass1.set_data([time[k]], [mass1Vel[i][k]])
        Mass1.set_3d_properties([mass1Vel[j][k]])
        Mass2.set_data([time[k]], [mass2Vel[i][k]])
        Mass2.set_3d_properties([mass2Vel[j][k]])
        Mass3.set_data([time[k]], [mass3Vel[i][k]])
        Mass3.set_3d_properties([mass3Vel[j][k]])
        Mass1Trail.set_data(time[:k+1], mass1Vel[i][:k+1])
        Mass1Trail.set_3d_properties(mass1Vel[j][:k+1])
        Mass2Trail.set_data(time[:k+1], mass2Vel[i][:k+1])
        Mass2Trail.set_3d_properties(mass2Vel[j][:k+1])
        Mass3Trail.set_data(time[:k+1], mass3Vel[i][:k+1])
        Mass3Trail.set_3d_properties(mass3Vel[j][:k+1])
        return Mass1, Mass2, Mass3, Mass1Trail, Mass2Trail, Mass3Trail
    # Formatting tick labels
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((-1, 1))
    ax.zaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    # Animation
    ani = FuncAnimation(fig, animate, init_func=init, frames=len(mass1Vel[0]), interval=1e-5, blit=True, repeat=True)
    # Title and labels
    ax.set_title(f"3D Velocity Animation Of Three Coupled Bodies - {jVelocity} And {iVelocity} vs. Time", fontsize = THREEDANIMTILE)
    ax.set_xlabel("Time In (s)", fontsize = THREEDPLOTLABELS)
    ax.set_ylabel(f"Velocity ({iVelocity}) In (m/s)", fontsize = THREEDPLOTLABELS)
    ax.set_zlabel(f"Velocity ({jVelocity}) In (m/s)", fontsize = THREEDPLOTLABELS)
    ax.legend()
    ax.grid(False)
    plt.show()
    