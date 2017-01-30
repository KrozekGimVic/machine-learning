from PIL import Image

with open('engine.csv') as f:
    l = f.readlines()
    l = [i.split(',') for i in l]

new_image = Image.new('L', (28, 28 * 10))
new_image_data = new_image.getdata()

l = [[float(i) for i in j] for j in l]
max_val = max([max(i) for i in l])

for _ in range(10):
    for i in range(28):
        for j in range(28):
            val = int(l[_][i + 28 * j] * 256 / max_val)
            new_image_data.putpixel((i, j + 28*_), (val))

new_image.save('image.png')
