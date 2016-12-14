import numpy as np
import random


def read(filename):
    result = []
    counter = 0
    with open(filename) as f:
        for line in f:
            if line[:5] != "label":
                label, *values = [float(i) for i in line.split(",")]
                result.append((label, values))
                if counter > 10: return result
                counter += 1
    return result


def softmax(W, slika, b):
    v = W.dot(slika)
    asdf = np.add(v, b)
    asdf *= step
    vsota = gama(asdf)
    return np.divide(asdf, vsota)


def delta(a, b):
    return a == b


def gama(a):
    return sum(np.exp(a))


step = 0.0001
b = np.array([random.random() for _ in range(10)])
W = np.array([[random.random() for __ in range(784)] for _ in range(10)])
p = 28**2
N = 10

z = []
data = read("train.csv")

digits = [i[0] for i in data]

for _ in range(100):
    z = [-softmax(W, x, b) for digit, x in data]
    for i in range(len(z)):
        b += z[i]*step

    max_index = [np.argmax(i) for i in z]
    print(b)
    for j in range(N):
        vsota = 0
        for i in range(10):
            for k in range(p):
                W[i][k] += (delta(max_index[i], digits[i]) - z[i][max_index[i]]) * data[j][1][k]
            b[i] += delta(max_index[i], digits[i]) - z[i][max_index[i]]



z = [-softmax(W, x, b) for digit, x in data]
for i in range(len(z)):
    print(digits[i], np.argmax(z[i]), z[i])