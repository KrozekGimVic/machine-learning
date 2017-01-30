with open('train.csv') as f:
    l = f.readlines()
    l = [i.split(',') for i in l]

res = []
l = [[int(i) for i in j] for j in l]
for image in l:
    new_image = [image[0]] + [0 if i == 0 else 1 for i in image[1:]]
    res.append(new_image)

with open('data.csv', 'w') as f:
    for image in res:
        f.write(','.join(map(str, image))+'\n')
