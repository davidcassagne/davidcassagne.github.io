from pylab import *

x = linspace(-8,8,201)
z = 5*exp(2j*x) + 7*exp(3j*x)

plot(x,real(z),label='real')
plot(x,imag(z),label='imag')
legend()

show()
