#!/usr/bin/python3
# -*- coding: utf-8 -*-
def position_apres_etape(num,den,etape=1):
    '''Calcul de la position "num/den" apres un nombre d'étapes donné (une étape par défaut).'''
    # Pour chaque étape, on calcul la nouvelle position de la coquille.
    for k in range(etape):
        if 2*num>den: # Si la position est > à 1/2.
            num=2*(den-num)
        else:num*=2 # Si la position est <= 1/2 on multiplie par 2.
    # On renvoie le numérateur (le dénominateur est inchangé).
    return num,den
