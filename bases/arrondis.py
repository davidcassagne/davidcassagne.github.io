from pylab import *

x = linspace(-2, 2, 500)
plot(x, around(x,0), label="around(x,0)")
plot(x, trunc(x), label="trunc(x)")
legend()

show()
