import matplotlib.pyplot as plt

import numpy as np

import plotly.plotly as py

from random import *

posizione = 0
N = 1000
prove = 1000
spostamento = []

for iterazioni in range(prove):

    for passi in range(N):

        x = random()
        if x >= 0.66:
            posizione += 1
        if x <= 0.33:
            posizione -= 1
    spostamento.append(posizione % 12)
    posizione = 0

plt.figure()
plt.hist(spostamento)
plt.show()
