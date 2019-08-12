# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:37:24 2016

@author: Phascolarctos
"""

"""
IN this class i define the object equation and his methods

"""
import numpy as np

class Equation():
    
    def __init__(self, a, b, c):
        
        self.delta = b**2-(4*a*c)
        self.x1 = (-b - np.sqrt(self.delta))/(2*a)
        self.x2 = (-b + np.sqrt(self.delta))/(2*a)
        
        print("\n first solution \n", self.x1,
              "\n secon solution \n", self.x2,)
              
              