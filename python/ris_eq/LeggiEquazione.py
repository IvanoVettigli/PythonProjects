import sys


class Leggi(object):

    def __init__(self):
        

        """Legge i coefficienti di un'equazione"""
        
        print(" \n Ciao! io sono un programma comodo e risolverò per te \
        un'equazione, ma a patto che sia nella forma ax^2+bx+c=0")

        self.a = float(input(" Quanto vale a? "))
        if self.a != 0:
            self.b = float(input(" E b? "))
            self.c = float(input(" last but not least, c? "))
        else:
            sys.exit('a non può essere uguale a zero,\
            tu stai cercando di imborgliarmi! \n programma terminato')
