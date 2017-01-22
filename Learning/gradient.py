from math import sin, cos

def gradientni_spust(tocka, gradient, korak):
    nova_tocka = list(tocka[:])
    for i in range(len(tocka)):
        nova_tocka[i] -= gradient[i](*tocka) * korak
    return nova_tocka

grad_x = lambda x, y: 2*x + (60*(x - 1)**3)/((x-1)**4 + y**2 + 3)**2 + 2*cos(x*y)*y
grad_y = lambda x, y: (30*y)/((x-1)**4 + y**2 + 3)**2 + 2*cos(x*y)*x + 2*y

gradient = grad_x, grad_y
tocka = 1, 1
korak = 0.01

for i in range(10000):
    tocka = gradientni_spust(tocka, gradient, korak)

print('x min: {:0.6f}, y min: {:1.6f}'.format(*tocka))
