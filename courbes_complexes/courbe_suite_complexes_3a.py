from pylab import *

x = linspace(-3, 3, 51)
y = linspace(-3, 3, 51)
X, Y = meshgrid(x, y)

C = angle(X + 1j *Y) 

pcolormesh(X, Y, C, shading='gouraud')
colorbar()
xlabel('partie reelle')
ylabel('partie imaginaire')

show()
