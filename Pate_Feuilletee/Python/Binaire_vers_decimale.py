#!/usr/bin/python3
# -*- coding: utf-8 -*-
from fractions import Fraction

def binaire_vers_decimale(binaire,periodique=False,irreductible=False):
    '''Renvoie le rationnel (entre 0 et 1) en base 10 de 'binaire'. 
       Si le bloc de chiffres 'binaire' est périodique mettre 'periodique' à 'True'.
       Le rationnel renvoyé est un tuple numérateur/dénominateur.
       Si 'irreductible' vaut 'True', la fractions renvoyée est irréductible.
    '''
    num=0 # Le numérateur du rationnel.
    den=1 # Le dénominateur du rationnel.
    for chiffre in binaire[::-1]: # Pour parcourir 'binaire' à l'envers.
        num+=int(chiffre)*den # Calcul du numérateur.
        den*=2 # On multiplie le dénominateur par 2 (soucis de rapidité).
    if periodique:
        if irreductible:return Fraction(num,den-1) # Si la fraction doit être irréductible.
        return str(num)+"/"+str(den-1) # On retourne la fraction.
    if irreductible:return Fraction(num,den) # Si la fraction doit être irréductible.
    return str(num)+"/"+str(den) # On retourne la fraction.
