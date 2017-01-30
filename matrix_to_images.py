from PIL import Image

with open('engine.csv') as f:
    l = f.readlines()
    l = l[0].split(',')

new_image = Image.new('L', (28, 28))
new_image_data = new_image.getdata()


l = [float(i) for i in l]
max_val = max(l)

for i in range(28):
    for j in range(28):
        val = int(l[28 * i + j] * 256 / max_val)
        new_image_data.putpixel((i, j), (val))

new_image.save('image.bmp')
