from Tkinter import *
from PIL import Image, ImageTk
import threading
from time import sleep
import os
import inspect


class display():
    def __init__(self, run, kill, scale, dims):
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

    def SetImage(self, img):
        """
        Takes an image, copies it then scales it and displays
        """
        img = ImageTk.PhotoImage(img.copy().resize(
            [a * self.scale for a in self.dims], Image.ANTIALIAS))
        self.label.configure(image=img)
        self.label.image = img
        self.root.update()

    def Clear(self):
        """
        clears display to black
        """
        self.SetImage(Image.new('RGB', self.dims))

    def SetPWMBits(self):
        """
        Not applicable to simulation
        """
        pass

    def SetPixel(self):
        """
        """
        pass

    def SetBuffer(self):
        """
        """
        pass

    def Fill(self):
        """
        """
        pass
