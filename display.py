from Tkinter import *
from PIL import Image, ImageTk
import threading
from time import sleep
import os
import inspect


class display():
    def run(self, run, kill, scale, dims):
        self.root = Tk()
        self.scale = scale
        self.dims = dims
        image = Image.new('RGB', self.dims)
        photo = ImageTk.PhotoImage(image)
        self.label = Label(image=photo)
        self.label.image = photo
        # keep a reference!
        self.label.pack()
        self.t = threading.Thread(target=run)
        self.t.start()
        self.root.mainloop()
        kill()

    def setImage(self, img):
        img = ImageTk.PhotoImage(img.copy().resize(
            [a * self.scale for a in self.dims], Image.ANTIALIAS))
        self.label.configure(image=img)
        self.label.image = img
        self.root.update()
