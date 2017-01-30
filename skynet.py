import numpy as np
from PIL import Image

class Skynet:
    @static_method
    def softmax(x):
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum(axis=0)

    def __init__(self, image_size=28, verbose=False):
        self.p = image_size**2 + 1
        self.data_set = None
        self.A = np.zeros((10, self.p))
        self.verbose = verbose

    def load_data_set(self, filename='data.csv', skip_first_line=True):
        if self.verbose:
            print('Starting loading image set...')
        skip_rows = 1 if skip_first_line else 0
        self.data_set = np.matrix(np.loadtxt(filename,
                                              dtype=int,
                                              delimiter=',',
                                              skiprows=skip_rows))
        self.data_set = np.append(self.data_set, [[1] for i in range(len(self.data_set))], axis=1)
        if self.verbose:
            print('Image set loaded.')

    def load_data_from_string(self, label, image_string, delimiter=None):
        if delimiter is None:
            array = list(image_string)
        else:
            array = image_string.split(delimiter)

        array = [label] + [int(i) for i in array] + [1]

        self.data_set = np.matrix(array)
        if self.verbose:
            print('Image loaded.')

    def load_engine_matrix(self, filename='engine.csv'):
        self.A = np.matrix(np.loadtxt(filename, delimiter=','))
        if self.verbose:
            print('Loaded engine matrix.')

    def save_engine_matrix(self, filename='engine.csv'):
        np.savetxt(filename, self.A, delimiter=',')
        if self.verbose:
            print('Saved engine matrix.')

    def train(self, mbs=100, E=100, learning_rate=1e-7, data_set_start=0, N=None):
        if self.data_set is None:
            if self.verbose:
                print('No image set loaded.')
            return

        if N is None:
            N = len(self.data_set)

        if self.verbose:
            print('Starting training...')

        for i in range(E):
            indexes = [j for j in range(data_set_start, data_set_start+N, 1)]
            indexes = np.random.permutation(indexes)
            for j in range(0, N, mbs):
                deltaA = np.zeros((10, self.p))
                correct = 0
                for index in indexes[j: j+mbs]:
                    yk = self.data_set[index, 0]
                    xk = self.data_set[index, 1:]
                    res = Skynet.softmax(self.A@xk.T)
                    res_num = np.argmax(res)
                    if res_num == yk:
                        correct += 1
                    deltaA -= np.outer(res, xk)
                    deltaA[yk, :] += np.array(xk)[0]
                self.A += learning_rate * deltaA

                ratio = int((correct/mbs) * 100)
                progress = int((i/E)*100)
                if self.verbose:
                    print('\rSuccess rate: {}%\tProgress: ['.format(ratio) + '#'*(progress//5) + ' '*(20-progress//5) + ']', end='')

        if self.verbose:
            print('\nTraining completed.')

    def test(self, data_set_start=0, N=None):
        if self.data_set is None:
            if self.verbose:
                print('No imge set loaded.')
            return

        if N is None:
            N = len(self.data_set)

        if self.verbose:
            print('Starting testing...')

        correct = 0
        for i in range(data_set_start, data_set_start+N, 1):
            yk = self.data_set[i, 0]
            xk = self.data_set[i, 1:]
            res = Skynet.softmax(self.A@xk.T)
            res_num = np.argmax(res)
            if res_num == yk:
                correct += 1

            ratio = int((correct/(i + 1 - data_set_start))*100)
            progress = int(((i + 1 - data_set_start)/N)*100)
            if self.verbose:
                print('\rSuccess rate: {}%\tProgress: ['.format(ratio) + '#'*(progress//5) + ' '*(20-progress//5)+ ']', end='')

        if self.verbose:
            print('\nTesting completed. Correct rate: {}%'.format(int((correct/N)*100)))

    def recognize(self, images, ignore_first=False):
        result = []
        for image in images:
            if ignore_first:
                im = image[0, 1:]
            else:
                im = image
            res = Skynet.softmax(self.A@np.matrix(im).T)
            res_num = np.argmax(res)
            result.append((res_num, res[res_num, 0]))
        return result


# Basic usage example
if __name__ == '__main__':
    sk = Skynet(verbose=True)
    sk.load_engine_matrix()
    # im = list(Image.open('/home/vidd/Desktop/image.png').getdata())
    # im.append(1)
    # print(sk.recognize([im]))
    # sk.load_data_set(filename='/home/vidd/Downloads/train.csv')
    # sk.train(N=39000, E=1,)
    # sk.test(data_set_start=39000, N=1000)
    sk.save_engine_matrix()
    #
    # test_images = sk.data_set[30000: 30100]
    # recognized = sk.recognize(test_images, ignore_first=True) # Ignore first image 'pixel' (in this case label)
    # print(recognized)
