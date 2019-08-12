import matplotlib.pyplot as mpl
import math
import numpy

h = pow(10, -4)
L = h
t = [0]

GM = 39.48

x = [1.97]
y = [0]

vx = [0]
vy = [0.816]

r = [math.sqrt(x[0] ** 2 + y[0] ** 2)]
v = [math.sqrt(vx[0] ** 2 + vy[0] ** 2)]

E = [-GM / r[0] + 0.5 * pow(v[0], 2)]

Fx = [-GM*x[0]/r[0]**3]
Fy = [-GM*y[0]/r[0]**3]

for i in range(1, 400001):

    x.append(x[i-1]+vx[i-1]*h+0.5*Fx[i-1]*pow(h, 2))
    y.append(y[i-1]+vy[i-1]*h+0.5*Fy[i-1]*pow(h, 2))

    r.append(math.sqrt(x[i]**2+y[i]**2))

    Fx.append(-GM*x[i]/r[i]**3)
    Fy.append(-GM*y[i]/r[i]**3)

    vx.append(vx[i-1]+0.5*(Fx[i-1]+Fx[i])*h)
    vy.append(vy[i-1]+0.5*(Fy[i-1]+Fy[i])*h)

    v.append(math.sqrt(vx[i]**2+vy[i]**2))

    E.append(-GM / r[i] + 0.5 * pow(v[i], 2))

    t.append(L)
    L += h


print(E[0], "\n", E[0]-numpy.mean(E))

mpl.figure()
mpl.plot(x, y)
mpl.title("Simulazione del moto della cometa di Halley")
mpl.xlabel("Unità di misura sugli assi 2.68x10^12[m]")
mpl.grid()

mpl.figure()
mpl.plot(t, vx)

mpl.figure()
mpl.plot(t, E)
mpl.grid()

mpl.show()
