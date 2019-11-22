from math import *
from pylab import *

x = arange(-2*pi, 2*pi, 0.1)
ysin = sin(x)
ycos = cos(x)


plot(x, ysin, color="green")
plot(x, ycos,color="pink")
show()
    
    
