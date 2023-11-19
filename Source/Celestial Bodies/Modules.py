# Modules
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
import sys

# Global Constants

G = 6.67408e-11 # Gravitational constant
AU = 1.5e11 # Astronomical unit
DS = pow(pow(24, 60), 60) # Number of seconds in one earth day

# Earth Constants
M_earth = 5.972e24
R_earth = 6.3781*10**6
X0_earth = 1 * AU
Y0_earth = 0
Z0_earth = 0
Vx_earth = 0
Vy_earth = 29784.8
Vz_earth = 0