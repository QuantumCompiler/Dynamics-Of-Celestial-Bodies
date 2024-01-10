# Celestial Bodies

The Three-Body Problem in physics refers to the challenge of predicting the motion of three celestial bodies moving under the influence of their mutual gravitational attraction. This problem is significant in the study of dynamics and celestial mechanics. It's a classic example of a complex system that's surprisingly difficult to solve.

To understand the Three-Body Problem, let's first consider the simpler Two-Body Problem. If you have two celestial bodies, like Earth and the Moon, the problem of predicting their motion around their common center of mass is relatively straightforward and can be solved with precise equations (like Kepler's laws of planetary motion).

However, things get much more complicated when you add a third body, like the Sun. The gravitational forces between each pair of objects interact in such a complex way that there's no general solution that works for all sets of initial conditions. This is what makes the Three-Body Problem so challenging.

Solutions to the Three-Body Problem:

1. **Numerical Methods**: For most practical purposes, scientists use numerical methods to approximate solutions. These involve using computers to simulate the system and calculate the positions of the bodies at successive time intervals. The accuracy of the results depends on the time intervals used and the computational power available.
1. **Restricted Three-Body Problem**: This is a simplified version where one of the bodies is assumed to have a negligible mass compared to the other two. This allows for some analytical solutions and is useful for understanding scenarios like a satellite orbiting a planet that orbits the Sun.
1. **Special Cases and Approximations**: There are a few specific scenarios where solutions have been found. For example, the Lagrange points are positions in space where a small body, under certain conditions, can be in a stable orbit relative to two larger bodies (like a satellite relative to Earth and the Sun).
1. **Chaos Theory**: The Three-Body Problem is also an example of a chaotic system. Small changes in the initial conditions can lead to vastly different outcomes, making long-term prediction practically impossible. This aspect of the problem has contributed to the development of chaos theory.

In summary, the Three-Body Problem in physics is a complex problem without a general solution. It's typically approached with numerical simulations, special case scenarios, and plays a crucial role in the study of dynamical systems and chaos theory.

## Overview

This repository contains source code and a report done on the dynamics of celestial bodies in space. This repository consists of two main folders.

- Demo: Contains demonstration images from the GUI program that was built for this project
- Report: Contains the documents found to generate the report for this project. As of this document creation, the report only covered the Forward Euler Difference Scheme (F.E.D.S) in the report.
    - Dynamics of a Triple Star System.pdf: PDF of the report generated for this project.
    - Source.zip: LaTeX files that are used to generate the report.
- Source: Contains the source code used to solve this problem.
    - Celestial Bodies: Source code in Python used to create a program for this problem.
        - Version 1.0.0: Source code for version 1.0.0 of the Celestial Bodies program.
            - src: Directory that contains the source code for this specific version
                - Images: Directory that contains the images used the program.
                    - Celestial Bodies.png: Image for the application.
                    - Icon.png: Icon for a MacOS application.
                    - Icon.ico: Icon for a Windows application.
                - Apple.spec: PyInstaller spec file for Apple platforms.
                - main.py: Main file where all previous custom / Python modules were used to run this program.
                - Microsoft.spec: PyInstaller spec file for Microsoft platforms.
                - Models.py: Differential equations of the models that were made for this program.
                - Modules.py: Python modules and global constants used in this program.
                - ProjectileMotion.py: Projectile motion classes and functions used for the projectile motion simulation.
                - RK4.py: Runge Kutta 4 differential equation solver functions used to solve models in this program.
                - ThreeBodies.py: Three body classes and functions used for the three body simulation.
                - TwoBodies.py: Two body classes and functions used for the two body simulation.
                - Windows.py: Main window and sub-window classes for the program.
    - Forward Euler: Source code in Python that was originally used to solve this problem.
        - Three Body Force Attraction (Forward Euler).py: Three body F.E.D.S solution.
        - Two Body Force Attraction (Forward Euler).py: Two body F.E.D.S solution.
        - Two Dimensional Force Attraction (Forward Euler).py: Two dimensional force attraction F.E.D.S solution.
    - Runge Kutta 4: Source code in Python that was constructed to solve this problem with a dynamic time step.
        - 2BodyAttraction.py: Two body force attraction differential equation.
        - 2DForce.py: Two D force attraction differential equation.
        - 3BodyAttraction.py: Three body force attraction differential equation.
        - RK4.py: RK4 solvers for the aforementioned models.
- .gitignore: Git ignore file for specific files and directories.

## Releases

### Version 1.0.0

Version 1.0.0 of Celestial Bodies was built with Python and the PyQt framework. This application is available for download as both a Windows .exe file and MacOS .app file. The releases of this program can be found [here](https://github.com/QuantumCompiler/Dynamics-Of-Celestial-Bodies/releases/tag/v1.0.0).

#### Version 1.0.0 Graphics
<p align = "center">
    <img src = "Demo/Main Window Demo.png" width = "800">
    <img src = "Demo/Parameters Input Demo.png" width = "800">
    <img src = "Demo/2D Projectile Motion Position Demo.png" width = "800">
    <img src = "Demo/2D Two Body Position Demo.png" width = "800">
    <img src = "Demo/3D Three Body Position Demo.png" width = "800">
</p>