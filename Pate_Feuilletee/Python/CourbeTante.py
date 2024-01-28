#!/usr/bin/python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np

etape=2 # Nombre d'étapes.
x=np.linspace(0,1,1000) # On prend 1000 points équitablement espacés dans [0;1].
# On calcul l'image de chaque point pour un nombre d'étape 'n'.
def f(x):
    for k in range(etape):x=1-np.absolute(2*x-1)
    return x
    
plt.plot(x,f(x)) # Dessine la fonction f.
#plt.plot(x,x) # Dessine la droite y=x.
plt.xlabel("x")
plt.ylabel("f^"+str(etape)+" (x)")
plt.title("Représentation graphique de la composée "+str(etape)+"-ième de f")
plt.grid()
plt.show()
