import sys


def read(filename):
    result = []
    with open(filename) as f:
        for line in f:
            if line[:5] != "label":
                label, *values = [int(i) for i in line.split(",")]
                result.append((label, values))
    return result

asdf = read(sys.argv[1])

for asdfasdf in asdf:
    asdfasdf = asdfasdf[1]
    for i in range(0, len(asdfasdf), 28):
        print(''.join(['#' if i else ' ' for i in asdfasdf[i:i+28]]))
