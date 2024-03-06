# Изобразите свою версию знаменитого «Черного квадрата».

import tkinter as tk
from PIL import Image, ImageTk


def draw(shader, width, height):
    image = Image.new('RGB', (width, height))
    pixels = image.load()
    for y in range(height):
        for x in range(width):
            color = shader(x / width, y / height)
            normalized = tuple(int(c * 255) for c in color)
            pixels[x, y] = normalized
    return image


def main(shader):
    window = tk.Tk()
    label = tk.Label(window)
    global image
    image = ImageTk.PhotoImage(draw(shader, 256, 256).resize((512, 512)))
    label.pack()
    label.config(image=image)
    window.mainloop()


def shader(x, y):
    return 0, 0, 0


main(shader)
