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
                counter += 1
                if counter >= N: return result
    return result


def softmax(W, slika, b):
    v = W.dot(slika)
    asdf = np.add(v, b)
    asdf *= step
    vsota = gama(asdf)
    return np.divide(np.exp(asdf), vsota)


def delta(a, b):
    return a == b


def gama(a):
    return sum(np.exp(a))


step = 1e-9
p = 28**2
N = 20
train_n = 200

b = np.array([1.0 for _ in range(10)])
W = np.array([[1.0 for __ in range(p)] for _ in range(10)])

z = []
data = read("train.csv")

digits = [i[0] for i in data]

for _ in range(train_n):
    print('\rTraining [' + '#' * (20*_//train_n) + '-' * (20-20*_//train_n) + '] {}% '.format(100*_//train_n), end='')
    z = [softmax(W, x, b) for __, x in data]
    for i in range(len(z)):
        b += z[i]*step

    max_index = [np.argmax(i) for i in z]
    for j in range(N):
        for i in range(10):
            for k in range(p):
                W[i][k] += (delta(i, digits[j]) - z[j][max_index[j]]) * data[j][1][k]
            b[i] += delta(i, digits[j]) - z[j][max_index[j]]

print()

z = [softmax(W, x, b) for digit, x in data]
correct = 0
for i in range(len(z)):
    correct += np.argmax(z[i]) == digits[i]
    print('Predicted:', np.argmax(z[i]), '\tReal:', digits[i], '\tCorrect:', np.argmax(z[i]) == digits[i])
print('Success rate: {:.1f}%'.format(100*correct/len(z)))
