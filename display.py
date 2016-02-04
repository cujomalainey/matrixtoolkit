from Tkinter import *
from PIL import Image, ImageTk
import threading
from time import sleep
import os
import inspect


class display():
    def __init__(self, matrix_height, chain_length):
        """
        run: function to run once setup is complete
        kill: deconstructor once simulation is closed
        scale: integer to scale dims by
        dims: tuple of matrix dimensions in pixels (x, y)
        """
        self.root = Tk()
        self.scale = 6
        self.dims = (32*chain_length, matrix_height)
        self.image = Image.new('RGB', self.dims)
        photo = ImageTk.PhotoImage(self.image)
        self.label = Label(image=photo)
        self.label.image = photo
        # keep a reference!
        self.label.pack()

    def start(self, run, kill):
        self.t = threading.Thread(target=run)
        self.t.start()
        self.root.mainloop()
        kill()

    def SetImage(self, img, x=0, y=0):
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

    def SetPWMBits(self, n):
        """
        Not applicable to simulation
        """
        pass

    def SetPixel(self, x, y, r, g=None, b=None):
        """
        draws a pixel on the matrix at x,y
        """
        try:
            r = int(r)
        except TypeError:
            pass
            # r, g, b = *r

    def SetBuffer(self):
        """
        """
        pass

    def Fill(self, color):
        """
        """
        pass
