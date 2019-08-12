import matplotlib.pyplot as mpl


def grafico(a, b, c):
    """
    Fa il grafico della parabola
    """

    xi = []
    yi = []
    Vx = -b/(2*a)

    for j in range(10, 0, -1):
        xi.append(Vx-j)
        yi.append(a*xi[10-j]**2+b*xi[10-j]+c)
    xi.append(Vx)
    yi.append(a*xi[10]**2+b*xi[10]+c)
    for j in range(0, 11, 1):
         xi.append(Vx+j)
         yi.append(a*xi[11+j]**2+b*xi[11+j]+c)
    mpl.plot(xi, yi)
    mpl.grid()
    mpl.show()
