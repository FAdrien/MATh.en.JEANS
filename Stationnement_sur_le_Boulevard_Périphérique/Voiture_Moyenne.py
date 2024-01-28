from fractions import Fraction
#from matplotlib import pyplot as plt
from mpmath import *

mp.dps=100

# Liste du nombre moyen de voiture en fonction du nombre de tirets (place) (fonction 1).
l1=[0,0] 
#[0,0] # Liste du nombre moyen de voiture en fonction du nombre de tirets (place) (fonction 2) [L(1), L(2)].
l2=[0,1]
# Liste du nombre moyen de voiture en fonction du nombre de tirets (place) (fluctuations).
l3=[mpf(5)/3,2,mpf(37)/15] 
l4=1
#n=int(input('Nb tirets: '))
def E_1(n):
    '''Cette fonction calcule à l'aide d'une formule de récursion le nombre moyen de voiture sur "n" tirets. '''  
    if len(l1)>=n+1:return l1[n]
    else:
        s=0
        for i in range(n-1):s+=l1[i]
        l1.append(1+mpf(2)*mpf(s)/(n-1))
        return l1[-1]
        
def E_2(n):
    global l2
    '''Cette fonction calcule à l'aide d'une formule de récursion le nombre moyen de voiture sur "n" tirets. '''
    l2.append(mpf(mpf(n-2)*l2[1]+mpf(2)*l2[0]+1)/(n-1))
    #l2.append(Fraction((n-2)*l2[1]+2*l2[0]+1,n-1))#.limit_denominator()) # Simplifier les calculs
    l2=l2[1:]
    return l2[1]
    
def E_2_fast(n):
    global l4
    '''Cette fonction calcule à l'aide d'une formule de récursion le nombre moyen de voiture sur "n" tirets. '''
    l4*=1+mpf(2)/(n-1)
    return l4
    
def E_22(n):
    global l3
    '''Cette fonction calcule à l'aide d'une formule de récursion le nombre moyen de voiture sur "n" tirets (v2). '''
    l3.append(mpf(mpf(n-2)*l3[2]+mpf(2)*l3[1]+1)/(n-1))
    l3=l3[1:]
    return l3[-1]

def fluctuationpaire(n,name):
    '''Cette fonction se charge de calculer les fluctuations dans la suite des nombres pairs.'''
    f=open(name,'w')
    for i in range(7,n+1):
        q,r=mpf(mpf(E_22(i))/int(i/2))*100,mpf(mpf(l3[0])/int((i-2)/2))*100
        if not (i%2 or r<=q):f.write(str(l3)+(100-len(str(l3)))*' '+'# '+str(i)+'\n')
    f.close()
    
def fluctuationimpaire(n,name):
    '''Cette fonction se charge de calculer les fluctuations dans la suite des nombres impairs.'''
    f=open(name,'w')
    for i in range(7,n+1):
        q,r=mpf(mpf(E_22(i))/int(i/2))*100,mpf(mpf(l3[0])/int((i-2)/2))*100
        if i%2 and not r>=q:f.write(str(l3)+(100-len(str(l3)))*' '+'# '+str(i)+'\n')
    f.close()

def maximumP(n,v):
    '''Cette fonction permet de calculer le plus grand nombre de tiret (pair) de tel sorte que sa part soit inférieure à "v".'''
    i,p=n,0
    while p<=v:
        m=E_2(i)
        if i%2==0:p=mpf(mpf(m)/int(i/2))*100
        else:p=0
        i+=1
    return i-1
    
def files(start=1,stop=100,step=10000):
    for k in range(start,stop):
        f=open('Calculs/E/E(n)_n__'+str(step*k+1)+'__'+str(step*(k+1)),'w')
        for i in range(step*k+1,step*(k+1)+1):
            l=str(Fraction(E_2(i),i).limit_denominator())
            f.write(l+(100-len(l))*' '+'#'+str(i)+'\n')
        f.close()
    print(l2)
    
def bounds(start=2,stop=1000):
    '''Calcul du rayon de convergence de L(n+1)-L(n) pour n-> oo.'''
    lamb=0
    epsi=0
    for i in range(start,stop):
        p1,p2=l2
        p3=E_2(i)
        if i==stop-1:
            p21=p2-p1
            p31=p3-p2
            lamb=min(p21,p31,(p1)/(i-1))
            epsi=max(p21,p31,(p1)/(i-1))
            print(p31)
            print(p21)
    return lamb,epsi#,stop-1,l2
    


#0.432332223046275082021736327508 0.432333223047139747332397663802
#[mpf('432331.358381693654053000252771195'), mpf('432331.790714052035746654305771483')]


# i = 1 000 000
# l2 = [Fraction(152838799317, 353522), Fraction(76419476078, 176761)]

#i = 10 000 000
# l2 = [Fraction(1528389799317, 353522), Fraction(764194976078, 176761)]

#0.4323323|01614918138867262622844094...    }
#0.4323323|5838169500740637396211385...     } i = 9999999

#0.4323323|205371816480409316281791...      }
#0.4323323|58381694213719049675757091...    } i = 15000000

# Cela semble converger vers 1-1/e^2.


#for i in range(6,100+1):E_1(i)    # On calcule les valeur du tableau nécessaire à la récursion.
#for n in range(2,100):
#    m=E_1(n)                    # On calcul le nombre moyen de voiture sur 'n' tirets.
#    print('***Calcul pour',n,'voitures***')
#    print('     Nombre moyen de voitures: ',m)
#    print('     Part du nombre total de voitures positionnables: ',m/int(n/2)*100,'%')
