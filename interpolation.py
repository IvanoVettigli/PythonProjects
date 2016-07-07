import plotly

from plotly.graph_objs import Scatter



xi = [-2, -1, 1, 2]
yi = [4, 1, 1, 4]


def neville(x, y, x0):
    """ Through any N points y[i] = f(x[i]), there is a unique
    polynomial P order N-1.  Neville's algorithm is used for finding
    interpolates of this unique polynomial at any point x. """
    n = len(x)
    p = n * [0]
    # noinspection PyUnresolvedReferences
    for k in range(n):
        for j in range(n - k):
            if k == 0:
                p[j] = y[j]
            else:
                p[j] = ((x0 - x[j + k]) * p[j] + (x[j] - x0) *
                p[j + 1]) / (x[j] - x[j + k])


    return p[0]


z = neville(xi, yi, 0)
print(z)

plotly.offline.plot({
    "data": [
        Scatter(x=[-2, -1, 0, 1, 2],
                y=[4, 1, z, 1, 4,])
    ],
 
})
