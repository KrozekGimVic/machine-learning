import sys

if len(sys.argv) == 3:
    in_file, out_file = sys.argv[1:]
else:
    in_file = 'train.csv'
    out_file = 'data.csv'

with open(in_file) as f:
    l = f.readlines()
    l = [i.split(',') for i in l[1:]]

res = []
l = [[int(i) for i in j] for j in l]
for image in l:
    new_image = [image[0]] + [0 if i == 0 else 1 for i in image[1:]]
    res.append(new_image)

with open(out_file, 'w') as f:
    for image in res:
        f.write(','.join(map(str, image))+'\n')
