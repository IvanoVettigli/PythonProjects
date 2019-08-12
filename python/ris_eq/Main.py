from Discriminante_positivo import discriminante_positivo
from Discriminante_negativo import discriminante_negativo
from Discriminante_nullo import discriminante_nullo
from Grafico import grafico
import LeggiEquazione

l = LeggiEquazione.Leggi()

delta = l.b**2-4*l.a*l.c

if delta < 0:
    discriminante_negativo(l.a, l.b, delta)
elif delta == 0:
    discriminante_nullo(l.a, l.b, l.c, delta)
else:
    discriminante_positivo(l.a, l.b, delta)

valore = input(" \n Vuoi il grafico della parabola intorno al vertice? ")
if "Si" == valore or "si" == valore:
    grafico(l.a, l.b, l.c)
    print("programma terminato comodamente!")
else:
    print(" \n programma terminato, grazie di aver usato un prodotto della \
    programmi comodi corporation!")
