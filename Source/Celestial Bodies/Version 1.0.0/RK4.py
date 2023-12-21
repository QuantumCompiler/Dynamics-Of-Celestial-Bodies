# Imports
from Modules import *

""" RK41st - Runge Kutta 4 ODE Solver (Of the form da / db) 
    Input:
        ODE - Ordinary Differential Equation that is being solved
        a0 - Original position
        b0 - Original time
        bn - Final time
        h - Step
    Algorithm:
        * Calculate the number of points n
        * Initialize the a values to zero with n + 1 entries
        * Set the initial value of a to be a0
        * Generate a list for b values from b0 to bn with n + 1 entries
        * Iterate over the total number of entries n
            * Update a to be the current value of a in avalues
            * Update b to be the current value of b in bvalues
            * Calculate k1, k2, k3, k4 from the definition of RK4
            * Update the next entry of avalues with the definition of RK4
        * Return the lists bvalues and avalues
    Output:
        avalues - List of a values that were found from RK4 method
        bvalues - List of b values that were found from RK4 method
"""
def RK41st(ODE, a0, b0, bn, h):
    # Number of points
    n = int((bn - b0) / h)
    # List for a values
    avalues = np.zeros(n + 1)
    # Initialize a
    avalues[0] = a0
    # Initialize b
    bvalues = np.linspace(b0, bn, n + 1)
    # Iterate over points
    for i in range(n):
        # Current state of values
        a = avalues[i]
        b = bvalues[i]
        # RK4 update
        k1 = h * ODE(a, b)
        k2 = h * ODE(a + 0.5 * k1, b + 0.5 * h)
        k3 = h * ODE(a + 0.5 * k2, b + 0.5 * h)
        k4 = h * ODE(a + k3, b + h)
        # Next state values
        avalues[i + 1] = a + (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return avalues, bvalues

""" RK42nd - Runge Kutta 4 ODE Solver For A Second Order ODE (Of the form d^2a / dc^2)
    Input:
        ODE - Function that represents a second order ODE
            * Particularly, this function must return da_dc, db_dc
        a0 - Initial value for a
        b0 - Initial value for b
        c0 - Initial value for c
        cn - Final value for c
        h - Step Size
    Algorithm:
        * Calculate the number of points n
        * Create lists for a, b, and c values
        * Initialize the values for a and b in their lists
        * Iterate over the total number of points n
            * Assign the values for a, b, and c with the current list value
            * Calculate the values for k1a, k2a, k3a, and k4a
            * Calculate the values for k1b, k2b, k3b, and k4b
            * Assign the next values for a and b in their lists
        * Return the lists
    Output:
        avalues - List of a values that were found from RK4 method
        bvalues - List of b values that were found from RK4 method
        cvalues - List of c values that were found from RK4 method
"""
def RK42nd(ODE, a0, b0, c0, cn, h):
    # Number of points
    n = int((cn - c0) / h)
    # List for a values
    avalues = np.zeros(n + 1)
    # List for b values
    bvalues = np.zeros(n + 1)
    # Initialize a
    avalues[0] = a0
    # Initialize b
    bvalues[0] = b0
    # Initialize c list
    cvalues = np.linspace(c0, cn, n + 1)
    # Iterate over points
    for i in range(n):
        # Current state of values
        a = avalues[i]
        b = bvalues[i]
        c = cvalues[i]
        # RK4 update
        k1a, k1b = h * np.array(ODE(c, a, b))
        k2a, k2b = h * np.array(ODE(c + 0.5 * h, a + 0.5 * k1a, b + 0.5 * k1b))
        k3a, k3b = h * np.array(ODE(c + 0.5 * h, a + 0.5 * k2a, b + 0.5 * k2b))
        k4a, k4b = h * np.array(ODE(c + h, a + k3a, b + k3b))
        # Next state of values
        avalues[i + 1] = a + (1/6) * (k1a + 2 * k2a + 2 * k3a + k4a)
        bvalues[i + 1] = b + (1/6) * (k1b + 2 * k2b + 2 * k3b + k4b)
    return avalues, bvalues, cvalues

""" RK4ProjectileMotion - Runge Kutta 4 Solver For Projectile Motion
    Input:
        ODE - Differential equation that is being used in solver
        obj - Object where the projectile motion is occurring
        ic - Initial conditions of projectile that is under projectile motion
            ic[0] - Initial position of projectile above objects surface
            ic[1] - Initial velocity of projectile in the vertical direction
        t0 - Initial time of solution
        tn - Final time of solution
    Algorithm:
        * Calculate the step size for the model
        * Calculate the number of points in solution
        * Create lists for position, velocity, and time
        * Initialize values for position and velocity
        * Iterate through the total number of points n
            * Retrieve the current stat of the system
            * Calculate the values for k1, k2, k3, and k4 respectively
            * Calculate the next state of the system
            * Update the current state of the system
        * Return the lists
    Output:
        posvals - List of position values of projectile
        velovals - List of velocity values of projectile
        timevals - List of time values of model
"""
def RK4ProjectileMotion(ODE, obj, ic, t0, tn):
    # Step size
    h = (tn - t0) / 10000
    # Number of points
    n = int((tn - t0) / h)
    # List for position values
    posvals = np.zeros(n + 1)
    # List for velocity values
    velovals = np.zeros(n + 1)
    # Initialize position
    posvals[0] = ic[0]
    # Initialize velocity
    velovals[0] = ic[1]
    # Initialize time list
    timevals = np.linspace(t0, tn, n + 1)
    # Iterate over points
    for i in range(n):
        # Current state of values
        state = (posvals[i], velovals[i])
        # Current time of state
        t = timevals[i]
        # RK4 update
        k1 = np.array(ODE(t, obj, *state))
        k2 = np.array(ODE(t + 0.5 * h, obj, *(np.add(state, 0.5 * h * k1))))
        k3 = np.array(ODE(t + 0.5 * h, obj, *(np.add(state, 0.5 * h * k2))))
        k4 = np.array(ODE(t + h, obj, *(np.add(state, h * k3))))
        # Next state of system
        next_state = np.add(state, (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4))
        # Update next state of system
        (posvals[i + 1], velovals[i + 1]) = next_state
    return posvals, velovals, timevals
    
""" RK4TwoBody - RK4 Method That Solves The Force Attraction Between Two Bodies In Space
    Input:
        ODE - Differential equation that represents the model that is to be solved
        massList - Array of masses in model
        ic - Initial conditions of bodies
        t0 - Initial time in model
        tn - Final time in model
    Algorithm:
        * Calculate the step size for the model
        * Calculate the number of points in solution
        * Create empty lists for the parameters of each mass
        * Create empty list for the time in the model
        * Initialize lists to their initial conditions
        * Iterate over the total number of points
            * Generate the state of the current parameters
            * Update the time to the current time in the step
            * Update the state with the RK4 method
            * Generate the next state of the system
            * Update the next state of the system
        * Return the lists
    Output:
        mass1Pos - List of mass 1 positions with respect to time
        mass2Pos - List of mass 2 positions with respect to time
        mass1Vel - List of mass 1 velocities with respect to time
        mass2Vel - List of mass 2 velocities with respect to time
        timevals - List of times at current steps in model
"""
def RK4TwoBody(ODE, massList, ic, t0, tn):
    # Step size
    h = (tn - t0) / 10000
    # Number of points
    n = int((tn - t0) / h)
    # Mass 1 position lists
    m1xvals = np.zeros(n + 1)
    m1yvals = np.zeros(n + 1)
    m1zvals = np.zeros(n + 1)
    # Mass 2 position lists
    m2xvals = np.zeros(n + 1)
    m2yvals = np.zeros(n + 1)
    m2zvals = np.zeros(n + 1)
    # Mass 1 velocity lists
    m1vxvals = np.zeros(n + 1)
    m1vyvals = np.zeros(n + 1)
    m1vzvals = np.zeros(n + 1)
    # Mass 2 velocity lists
    m2vxvals = np.zeros(n + 1)
    m2vyvals = np.zeros(n + 1)
    m2vzvals = np.zeros(n + 1)
    # Initializing mass 1 position lists
    m1xvals[0] = ic[0][0]
    m1yvals[0] = ic[0][1]
    m1zvals[0] = ic[0][2]
    # Initializing mass 2 position lists
    m2xvals[0] = ic[1][0]
    m2yvals[0] = ic[1][1]
    m2zvals[0] = ic[1][2]
    # Initializing mass 1 velocity lists
    m1vxvals[0] = ic[2][0]
    m1vyvals[0] = ic[2][1]
    m1vzvals[0] = ic[2][2]
    # Initializing mass 2 velocity lists
    m2vxvals[0] = ic[3][0]
    m2vyvals[0] = ic[3][1]
    m2vzvals[0] = ic[3][2]
    # Initialize time list
    timevals = np.linspace(t0, tn, n + 1)
    # Iterate over points
    for i in range(n):
        # Current state of system
        state = (m1xvals[i], m1yvals[i], m1zvals[i], 
                m2xvals[i], m2yvals[i], m2zvals[i], 
                m1vxvals[i], m1vyvals[i], m1vzvals[i], 
                m2vxvals[i], m2vyvals[i], m2vzvals[i])
        # Current time of state
        t = timevals[i]
        # RK4 update
        k1 = np.array(ODE(t, massList, *state))
        k2 = np.array(ODE(t + 0.5 * h, massList, *(np.add(state, 0.5 * h * k1))))
        k3 = np.array(ODE(t + 0.5 * h, massList, *(np.add(state, 0.5 * h * k2))))
        k4 = np.array(ODE(t + h, massList, *(np.add(state, h * k3))))
        # Next state of system
        next_state = np.add(state, (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4))
        # Update next state of system
        (m1xvals[i + 1], m1yvals[i + 1], m1zvals[i + 1],
        m2xvals[i + 1], m2yvals[i + 1], m2zvals[i + 1],
        m1vxvals[i + 1], m1vyvals[i + 1], m1vzvals[i + 1],
        m2vxvals[i + 1], m2vyvals[i + 1], m2vzvals[i + 1]) = next_state
    # Parameter lists
    mass1Pos = [m1xvals, m1yvals, m1zvals]
    mass1Vel = [m1vxvals, m1vyvals, m1vzvals]
    mass2Pos = [m2xvals, m2yvals, m2zvals]
    mass2Vel = [m2vxvals, m2vyvals, m2vzvals]
    return mass1Pos, mass2Pos, mass1Vel, mass2Vel, timevals

""" RK4ThreeBody - RK4 Method That Solves The Force Attraction Between Three Bodies In Space
    Input:
        ODE - Differential equation that represents the model that is to be solved
        massList - Array of masses in model
        ic - Initial conditions of bodies
        t0 - Initial time in model
        tn - Final time in model
    Algorithm:
        * Calculate the step size for the model
        * Calculate the number of points in solution
        * Create empty lists for the parameters of each mass
        * Create empty list for the time in the model
        * Initialize lists to their initial conditions
        * Iterate over the total number of points
            * Generate the state of the current parameters
            * Update the time to the current time in the step
            * Update the state with the RK4 method
            * Generate the next state of the system
            * Update the next state of the system
        * Return the lists
    Output:
        mass1Pos - List of mass 1 positions with respect to time
        mass2Pos - List of mass 2 positions with respect to time
        mass3Pos - List of mass 3 positions with respect to time
        mass1Vel - List of mass 1 velocities with respect to time
        mass2Vel - List of mass 2 velocities with respect to time
        mass3Vel - List of mass 3 velocities with respect to time
        timevals - List of times at current steps in model
"""
def RK4ThreeBody(ODE, massList, ic, t0, tn):
    # Step size
    h = (tn - t0) / 10000
    # Number of points
    n = int((tn - t0) / h)
    # Mass 1 position lists
    m1xvals = np.zeros(n + 1)
    m1yvals = np.zeros(n + 1)
    m1zvals = np.zeros(n + 1)
    # Mass 2 position lists
    m2xvals = np.zeros(n + 1)
    m2yvals = np.zeros(n + 1)
    m2zvals = np.zeros(n + 1)
    # Mass 3 position lists
    m3xvals = np.zeros(n + 1)
    m3yvals = np.zeros(n + 1)
    m3zvals = np.zeros(n + 1)
    # Mass 1 velocity lists
    m1vxvals = np.zeros(n + 1)
    m1vyvals = np.zeros(n + 1)
    m1vzvals = np.zeros(n + 1)
    # Mass 2 velocity lists
    m2vxvals = np.zeros(n + 1)
    m2vyvals = np.zeros(n + 1)
    m2vzvals = np.zeros(n + 1)
    # Mass 3 velocity lists
    m3vxvals = np.zeros(n + 1)
    m3vyvals = np.zeros(n + 1)
    m3vzvals = np.zeros(n + 1)
    # Initializing mass 1 position lists
    m1xvals[0] = ic[0][0]
    m1yvals[0] = ic[0][1]
    m1zvals[0] = ic[0][2]
    # Initializing mass 2 position lists
    m2xvals[0] = ic[1][0]
    m2yvals[0] = ic[1][1]
    m2zvals[0] = ic[1][2]
    # Initializing mass 3 position lists
    m3xvals[0] = ic[2][0]
    m3yvals[0] = ic[2][1]
    m3zvals[0] = ic[2][2]
    # Initializing mass 1 velocity lists
    m1vxvals[0] = ic[3][0]
    m1vyvals[0] = ic[3][1]
    m1vzvals[0] = ic[3][2]
    # Initializing mass 2 velocity lists
    m2vxvals[0] = ic[4][0]
    m2vyvals[0] = ic[4][1]
    m2vzvals[0] = ic[4][2]
    # Initializing mass 3 velocity lists
    m3vxvals[0] = ic[5][0]
    m3vyvals[0] = ic[5][1]
    m3vzvals[0] = ic[5][2]
    # Initialize time list
    timevals = np.linspace(t0, tn, n + 1)
    # Iterate over points
    for i in range(n):
        # Current state of system
        state = (m1xvals[i], m1yvals[i], m1zvals[i],
                m2xvals[i], m2yvals[i], m2zvals[i],
                m3xvals[i], m3yvals[i], m3zvals[i],
                m1vxvals[i], m1vyvals[i], m1vzvals[i],
                m2vxvals[i], m2vyvals[i], m2vzvals[i],
                m3vxvals[i], m3vyvals[i], m3vzvals[i])
        # Current time of state
        t = timevals[i]
        # RK4 update
        k1 = np.array(ODE(t, massList, *state))
        k2 = np.array(ODE(t + 0.5 * h, massList, *(np.add(state, 0.5 * h * k1))))
        k3 = np.array(ODE(t + 0.5 * h, massList, *(np.add(state, 0.5 * h * k2))))
        k4 = np.array(ODE(t + h, massList, *(np.add(state, h * k3))))
        # Next state of system
        next_state = np.add(state, (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4))
        # Update next state of system
        (m1xvals[i + 1], m1yvals[i + 1], m1zvals[i + 1],
        m2xvals[i + 1], m2yvals[i + 1], m2zvals[i + 1],
        m3xvals[i + 1], m3yvals[i + 1], m3zvals[i + 1],
        m1vxvals[i + 1], m1vyvals[i + 1], m1vzvals[i + 1],
        m2vxvals[i + 1], m2vyvals[i + 1], m2vzvals[i + 1],
        m3vxvals[i + 1], m3vyvals[i + 1], m3vzvals[i + 1]) = next_state
    # Parameter lists
    mass1Pos = [m1xvals, m1yvals, m1zvals]
    mass1Vel = [m1vxvals, m1vyvals, m1vzvals]
    mass2Pos = [m2xvals, m2yvals, m2zvals]
    mass2Vel = [m2vxvals, m2vyvals, m2vzvals]
    mass3Pos = [m3xvals, m3yvals, m3zvals]
    mass3Vel = [m3vxvals, m3vyvals, m3vzvals]
    return mass1Pos, mass2Pos, mass3Pos, mass1Vel, mass2Vel, mass3Vel, timevals