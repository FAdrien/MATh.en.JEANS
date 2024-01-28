#!/usr/bin/python3
# -*- coding: utf-8 -*-
from sympy import divisors

d={1:2}  # Contient : 'clé' (le nombre d'étape, 'n') et 'valeur' (nombre de solutions d'orbite 'n').
def S_n(n):
    '''Fonction récurrente pour obtenir le nombre de solutions d'orbite 'n'.'''
    S=2**n  # Le nombre de solutions de période divisant 'n'.
    for diviseur in divisors(n)[:-1]:  # On parcourt la liste des diviseurs de 'n' sauf 'n'.
        v=d.get(diviseur,0)
        if v:  # Si on connaît le nombre de solutions d'orbite 'diviseur'.
            S-=v  # On le soustrait à 'S'.
        else:  # Sinon on le calcul, on l'ajoute au dictionnaire puis on le soustrait.
            v=S_n(diviseur)
            d[diviseur]=v
            S-=v
    return S
