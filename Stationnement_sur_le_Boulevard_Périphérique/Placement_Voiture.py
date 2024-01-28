'''

Ce fichier permet de placer des voitures selon le choix de utilisateur. C'est-à-dire que, cette fois-ci, c'est le choix des conducteurs de voitures qui détermine le nombre de voitures placées.

'''

from random import randint

g=lambda a:a!=''
n=int(input('Nb tirets: '))
l=[(i,i+1) for i in range(1,n)] + [(n,1)]

def placement():
    # On effectue une copie de toutes les place disponibles et création d'une liste contenant les voitures qui seront placés.
    liste,voiture=l[:],0
    while liste!=[]:                            # Tant que la liste n'est pas vide.
        r=randint(0,len(liste)-1)               # On choisi un nombre aléatoire.
        voiture+=1                # On ajoute une voiture dans la liste.
        # On prend les places qui précède et succède celle choisie.
        c1,c2=(r+1)%len(liste),r-1
        if liste[c1][0]==liste[r][1]:liste[c1]=''                       # On remplace les positions inutilisables par du vide.
        if liste[c2]!='' and liste[c2][1]==liste[r][0]:liste[c2]=''      # Idem.
        liste[r]=''                                     # Idem
        liste=list(filter(g,liste))
    return voiture
    
s=0
for i in range(100):
    s+=placement()
print(s/100)
