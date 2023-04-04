#################### Libraries
import matplotlib.pyplot as plt

#################### Constants
G=6.67e-11
M1=2.0*10**27
M2=2.0*10**31
M3=2.0*10**29
AU=1.5e11
DS=24.0*60*60
GC1=G*M1*M2
GC2=G*M2*M3
GC3=G*M1*M3

#################### Time Steps
t=0.0
dt=0.1*DS

#################### Initial Conditions
##### Mass 1 Parameters
x1=-1.0*AU
y1=0.0
z1=0.0
xv1=0.0
yv1=30000.0
zv1=0.0

##### Mass 2 Parameters
x2=0.0
y2=0.0
z2=0.0
xv2=0.0
yv2=100.0
zv2=0.0

##### Mass 3 Parameters
x3=1.0*AU
y3=0.0
z3=0.0
xv3=0.0
yv3=-30000.0
zv3=0.0

#################### Lists
x1list=[]
y1list=[]
z1list=[]
x2list=[]
y2list=[]
z2list=[]
x3list=[]
y3list=[]
z3list=[]

#################### Loop
while t<(5*365.25)*DS:
    ############### Compute The Forces
    ########## Radial Variables
    ##### From Mass 1 to Mass 2
    r12x=x2-x1
    r12y=y2-y1
    r12z=z2-z1
    r123=(r12x**2+r12y**2+r12z**2)**1.5
    ##### From Mass 2 to Mass 3
    r23x=x3-x2
    r23y=y3-y2
    r23z=z3-z2
    r233=(r23x**2+r23y**2+r23z**2)**1.5
    ##### From Mass 1 to Mass 3
    r13x=x3-x1
    r13y=y3-y1
    r13z=z3-z1
    r133=(r13x**2+r13y**2+r13z**2)**1.5
    ########## Forces in all directions
    ##### Forces on Mass 1 due to Masses 2 and 3
    fx123=-(GC1*r12x)/(r123)-(GC3*r13x)/(r133)
    fy123=-(GC1*r12y)/(r123)-(GC3*r13y)/(r133)
    fz123=-(GC1*r12z)/(r123)-(GC3*r13z)/(r133)
    ##### Forces on Mass 2 due to Masses 1 and 3
    fx213=-(GC2*r23x)/(r233)-(GC1*r12x)/(r123)
    fy213=-(GC2*r23y)/(r233)-(GC1*r12y)/(r123)
    fz213=-(GC2*r23z)/(r233)-(GC1*r12z)/(r123)
    ##### Forces on Mass 3 due to Masses 1 and 2
    fx312=-(GC3*r13x)/(r133)-(GC2*r23x)/(r233)
    fy312=-(GC3*r13y)/(r133)-(GC2*r23y)/(r233)
    fz312=-(GC3*r13z)/(r133)-(GC2*r23z)/(r233)
    ########## Update Quantities
    ##### Mass 1
    xv1+=-(fx123*dt)/M1
    yv1+=-(fy123*dt)/M1
    zv1+=-(fz123*dt)/M1
    x1+=xv1*dt
    y1+=yv1*dt
    z1+=zv1*dt
    t+=dt
    ##### Mass 2
    xv2+=(fx213*dt)/M2
    yv2+=(fy213*dt)/M2
    zv2+=(fz213*dt)/M2
    x2+=xv2*dt
    y2+=yv2*dt
    z2+=zv2*dt
    ##### Mass 3
    xv3+=(fx312*dt)/M3
    yv3+=(fy312*dt)/M3
    zv3+=(fz312*dt)/M3
    x3+=xv3*dt
    y3+=yv3*dt
    z3+=zv3*dt
    ########## Append in Lists
    ##### X-Direction
    x1list.append(x1)
    x2list.append(x2)
    x3list.append(x3)
    ##### Y-Direction
    y1list.append(y1)
    y2list.append(y2)
    y3list.append(y3)
    ##### Z-Direction
    z1list.append(z1)
    z2list.append(z2)
    z3list.append(z3)
    
#################### Plots
plt.plot(x1list,y1list,"-k",label='Mass 1',linewidth=2.0)
plt.plot(x2list,y2list,"-b",label='Mass 2',linewidth=2.0)
plt.plot(x3list,y3list,"-g",label='Mass 3',linewidth=2.0)
plt.xlabel("X-Position in Meters")
plt.ylabel("Y-Position in Meters")
plt.axis("equal")
plt.title("3 Body System Initial Position")
plt.legend()
plt.show()
    
#################### Planets
##### Mercury
# M=3.285*10**23
# V=47400
# R=0.39 AU
##### Venus
# M=4.867*10**24
# V=35000
# R=0.723 AU
##### Earth
# M=5.972*10**24
# V=30000
# R=1.0 AU
##### Mars
# M=6.39*10**23
# V=24100
# R=1.524 AU
##### Jupiter
# M=1.898*10**27
# V=13100
# R=5.2 AU
##### Saturn
# M=5.683*10**26
# V=9600
# R=9.6 AU
##### Uranus
# M=8.681*10**25
# V=6800
# R=19.2 AU
##### Neptune
# M=1.024*10**26
# V=5430
# R=30.1 AU
##### Pluto
# M=1.309*10**22
# V=4740
# R=29 AU
##### Sun
# M=1.989*10**30


































