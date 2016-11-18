import numpy

with open('meritve.txt') as f:
    data = f.readlines()

data = [[float(i.split()[0]), float(i.split()[1])] for i in data]

# a = numpy.array([[i[0], 1] for i in data])
# b = numpy.array([i[1] for i in data])
#
# c = numpy.linalg.lstsq(a, b)[0]
#
# print(c)

def gradientni_spust(data, a, b, grad_a, grad_b, step):
    a -= grad_a(a, b, data, step)
    b -= grad_b(a, b, data, step)
    return a, b

def grad_a(a, b, l, step):
    s = 0
    for x, y in l:
        s += (-x * (y - a * x - b)) * step
    return s

def grad_b(a, b, l, step):
    s = 0
    for x, y in l:
        s += -(y - a * x - b) * step
    return s

a, b = 0, 0
for i in range(50000):
    a, b = gradientni_spust(data, a, b, grad_a, grad_b, 5e-8)
    if i % 100 == 0: print(a, b)
print(a, b)

#-1.2984640721985186 2.190221283340356

