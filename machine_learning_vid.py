import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

mbs = 100
E = 100
learning_rate = 0.0000001
p = 28*28 + 1

# Zaenkrat rabs pobrisat prvo vrstico kjer je napisan label, pixel1......... drgac nau delal
data = np.matrix(np.loadtxt('/home/vidd/Downloads/train.csv', dtype=int, delimiter=','))
N = len(data)
data = np.append(data, [[1] for i in range(N)], axis=1)


print('starting')

learn = False

if learn:
    A = np.zeros((10, p))
    for i in range(E):
        indexes = [i for i in range(N)]
        indexes = np.random.permutation(indexes)
        for j in range(0, N, mbs):
            deltaA = np.zeros((10, p))
            correct = 0
            for index in indexes[j : j+mbs]:
                yk = data[index, 0]
                xk = data[index, 1:]
                res = softmax(A@xk.T)
                res_num = np.argmax(res)
                if res_num == yk:
                    correct += 1
                deltaA -= np.outer(res, xk)
                deltaA[yk,:] += np.array(xk)[0]
            A += learning_rate * deltaA
            ratio = correct/mbs
            print(ratio)

    np.savetxt('engine.csv', A, delimiter=',')
else:
    A = np.matrix(np.loadtxt('engine.csv', delimiter=','))

data = np.matrix(np.loadtxt('/home/vidd/Downloads/test.csv', dtype=int, delimiter=','))
N = len(data)
data = np.append(data, [[1] for i in range(N)], axis=1)

correct = 0
for i in range(N):
    yk = data[i, 0]
    xk = data[i, 1:]
    res = softmax(A@xk.T)
    res_num = np.argmax(res)
    print(res_num, yk)
    if res_num == yk:
        correct += 1
print(correct/N)
