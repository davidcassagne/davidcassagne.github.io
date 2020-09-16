from pylab import *

x = linspace(-8,8,201)
z = 5*exp(2j*x) + 7*exp(3j*x)

X = array([x,x])

y0 = zeros(len(x))
y = abs(z)
Y = array([y0,y])

Z = array([z,z])
C = angle(Z)

plot(x,y,'k')

pcolormesh(X, Y, C, shading='gouraud', cmap=cm.hsv, vmin=-pi, vmax=pi)
colorbar()

show()
