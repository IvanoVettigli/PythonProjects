#!/ us r / b in /env python

from pylab import *
from scipy.integrate import odeint
from scipy.optimize import brentq

b = 2.0
Vo = 20.0       # Potential out side square well
steps = 100
E = 0.0     # global variable, changed by Final_Value()


def V(x):

    if x < 1.0:
        return 0        # square well
    else:
        return Vo


def SE(y, x):

    g0 = y[1]
    g1 = - 2.0 * (E-V(x)) * y[0]
    return array([g0, g1])


def Final_Value(energy):

    global y
    global E
    E = energy
    y = odeint(SE, yo, x)
    return y[-1, 0]     # return final value ( psi at b )


y = zeros([steps, 2])
yo = array([1.0, 0.0])      # initial psi and psi-dot .
x = linspace(0, b, steps)
E1 = float(-1)
E2 = float(1)
answer = brentq(Final_Value, E1, E2)        # use brentq to solve for E-> psi=0 at b .

print('Eigenvalue found at E = %.8f ' % answer)
plot(x, y[:, 0])
xlabel("Position (Units of L)")
show()
