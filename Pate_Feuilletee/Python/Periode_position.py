#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Position_apres_etapes import position_apres_etape
from math import gcd

def periode_position(num,den,etape_max=1000):
    '''Cherche si la position "num/den" est périodique pour un nombre d'étape inférieur à "etape_max".'''
    num1=num # On stocke "num" ailleurs pour la comparaison ligne 9.
    for k in range(etape_max):
        num1=position_apres_etape(num1,den)[0]
        if num1==num:return "La position '"+str(num)+"/"+str(den)+"' est "+str(k+1)+"-périodique."
    return "La position '"+str(num)+"/"+str(den)+"' ne se répète pas avant "+str(etape_max)+" étapes."
