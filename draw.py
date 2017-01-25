import tkinter as tk
from PIL import Image
import io
from skynet import Skynet

width = 280
height = 280

pendown = False
xold, yold = None, None

def pendown_event(event):
    global pendown
    pendown = True

def penup_event(event):
    global pendown, xold, yold
    pendown = False
    xold = None
    yold = None

def motion(event):
    global pendown, xold, yold
    if pendown:
        if xold is not None and yold is not None:
            event.widget.create_line(xold, yold, event.x, event.y, smooth=True, width=18, fill='white')
        xold = event.x
        yold = event.y

def recognize():
    global recognized_text
    ps = drawing_area.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.thumbnail((28, 28), Image.ANTIALIAS)
    img.save('image.png')
    image_data = img.getdata()

    image_vector = [0 for i in range(28 * 28 + 1)]
    image_vector[-1] = 1

    for i in range(28):
        for j in range(28):
            r, g, b = image_data.getpixel((j, i))
            image_vector[28 * i + j] = (r + g + b) / 3

    recognized_text.set(str(sk.recognize([image_vector])[0][0]))

def reset_canvas():
    drawing_area.delete('all')
    drawing_area.create_rectangle(0, 0, width+10, height+10, fill='black')


sk = Skynet()
sk.load_engine_matrix()

window = tk.Frame()
window.master.title("Digit recognition")
window.grid()

drawing_area = tk.Canvas(window, width=width, height=height)
drawing_area.grid(row=0, column=0)
reset_canvas()

recognized_text = tk.StringVar()
label = tk.Label(window, textvariable=recognized_text)
label.grid(row=0, column=1)

recognize_button = tk.Button(window, text="Recognize", command=recognize)
recognize_button.grid(row=1, column=1)

clear_button = tk.Button(window, text="Clear", command=reset_canvas)
clear_button.grid(row=1, column=0)

drawing_area.bind("<Motion>", motion)
drawing_area.bind("<ButtonPress-1>", pendown_event)
drawing_area.bind("<ButtonRelease-1>", penup_event)

window.mainloop()
