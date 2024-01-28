#!/usr/bin/python3
# -*- coding: utf-8 -*-
def binaire(num,den,precision=1000):
    '''Converti une position "num/den" en binaire.'''
    binaire="" # Résultat en binaire.
    unite=0 # Chiffre des unité de la position.
    for k in range(precision): # On calcul 'precision' chiffres après la virgule.
        num*=2
        if num>=den:unite=1 # Si 'num/den' a pour chiffre des unités 1.
        else:unite=0 # Sinon 'num/den' a pour chiffre des unités 0.
        binaire+=str(unite) # On ajoute ce chiffre des unités.
        num-=den*unite # On soustrait le dénominateur au numérateur si 'unité' vaut 1.
    # On renvoie le nombre en binaire avec 'precision' chiffres après la virgule.
    return binaire

print(binaire(7,15,50))
