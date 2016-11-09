import numpy

with open('meritve.txt') as f:
    data = f.readlines()

data = [[float(i.split()[0]), float(i.split()[1])] for i in data]

a = numpy.array([[i[0], 1] for i in data])
b = numpy.array([i[1] for i in data])

c = numpy.linalg.lstsq(a, b)[0]

print(c)
