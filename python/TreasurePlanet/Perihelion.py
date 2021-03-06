import matplotlib.pyplot as mpl
import math
from scipy import stats

alpha = 0.008

h = 0.01
L = h
t = [0]

x = [0.5]
vx = [0]

y = [0]
vy = [1.6]

r = [math.sqrt(x[0]**2+y[0]**2)]

Fx = [-x[0]/r[0]**3*(1+alpha/r[0]**2)]
Fy = [-y[0]/r[0]**3*(1+alpha/r[0]**2)]

theta = [0]

dr = [(x[0]*vx[0]+y[0]*vy[0])/r[0]]
tp = [0]
thetap = [0]

for i in range(1, 4001):

    x.append(x[i-1]+vx[i-1]*h+0.5*Fx[i-1]*pow(h, 2))
    y.append(y[i-1]+vy[i-1]*h+0.5*Fy[i-1]*pow(h, 2))

    r.append(math.sqrt(x[i]**2+y[i]**2))

    Fx.append(-x[i]/r[i]**3*(1+alpha/r[i]**2))
    Fy.append(-y[i]/r[i]**3*(1+alpha/r[i]**2))

    vx.append(vx[i-1]+0.5*(Fx[i-1]+Fx[i])*h)
    vy.append(vy[i-1]+0.5*(Fy[i-1]+Fy[i])*h)

    theta.append(math.atan(y[i]/x[i]))
    dr.append((x[i]*vx[i]+y[i]*vy[i])/r[i])

    t.append(L)
    L += h

    if dr[i-1] > 0 > dr[i]:

        thetap.append(theta[i])
        tp.append(t[i])

slope, intercept, r_value, p_value, std_err = stats.linregress(tp, thetap)

print("The slope is ", slope, "\nThe intercept is ", intercept,
      "\nr square is", r_value**2)

print("The slope is the perihelion")

mpl.figure()
mpl.plot(x, y)
mpl.grid()

mpl.figure()
mpl.plot(tp, thetap)
mpl.grid()

mpl.show()
