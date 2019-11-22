import math
from math import *
import pylab

XY = []

for x in range (-25, 26):
    for y in range(-25, 26):
        XY.append((x,y))


skala = lambda x: (2*pi/25)*x

values = []
def f(*par):
    for i in par:
        values.append(tuple(map(skala, i)))

#przeliczamy wartosci na zakres od <-2pi do 2pi>
for i in XY:
    f(i)

function = []
xx = []
for (x,y) in values:
    function.append( sin(x) * cos(y) )
    xx.append( x ); 

X = []
Y = []
def extract(*par):
    for i in par:
        X.append( i[0] )
        Y.append( i[1] )

for i in XY:
    extract(i) 

pylab.plot(X, Y, "o:")  #siatka wartosci
pylab.plot(X,values[:len(X)],color="red")
pylab.show()    
