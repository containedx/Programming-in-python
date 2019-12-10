from math import *
from itertools import *
a = [ 4, 2, 3 ]
omega = list( product(a, a, a) )

def f( a, b, c):
    return sin(a)*sin(b)*cos(c)

values = []
for zm in omega:
    values.append( f( zm[0], zm[1], zm[2] ) )

#najmniejsza wartosc:
min = values[0]

for j in values:
    if min > j:
        min = j
        print( "znalzlem nowe min:", min, "\n" )


print("przestrzen OMEGA\n")
for i in omega:
    print(i)

for i in values:
    print(i)


print( "\nMIN: ", min , "\n\n")


####### rekurencja ????????

def g( *l):
    if not l:
        return []
    if len(l) == 1:
        return [ (e,) for e in l[0] ] 
    else:
        L=[]
        for i in g(*l[1:]): #i - krotka
            for j in l[0]:  # z j robimy krotke
                L.append((j,)+i)
        return L

Lista = g( [1, 2, 3], 'abc' )
print( Lista )

print( g(a, a, a) )
#czyli w sumie chyba robimy to samo co funkcja product XD



