import platform
if platform.system() == "Darwin":
    from Tkinter import Tk, Label
elif platform.system() == "Windows":
    from tkinter import Tk, Label
from PIL import Image, ImageTk, ImageDraw
import threading


class display():
    def __init__(self, matrix_height, chain_length, scale=6):
        """
        run: function to run once setup is complete
        kill: deconstructor once simulation is closed
        scale: integer to scale dims by
        dims: tuple of matrix dimensions in pixels (x, y)
        """
        self.root = Tk()
        self.scale = scale
        self.dims = (32*chain_length*self.scale, matrix_height*self.scale)
        self.image = Image.new('RGB', self.dims)
        self.tkimage = self.image
        photo = ImageTk.PhotoImage(self.image)
        self.label = Label(image=photo)
        self.label.image = photo
        self.draw = ImageDraw.Draw(self.image)
        # keep a reference!
        self.label.pack()

    def start(self, run, kill):
        self.t = threading.Thread(target=run)
        self.t.start()
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.root.mainloop()
        kill()

    def _on_closing(self):
        self.root.destroy()

    def SetImage(self, img, x=0, y=0):
        """
        Takes an image, copies it then scales it and displays
        """
        self.image.paste(
            img.copy().convert('RGB').resize(
             [img.width * self.scale, img.height * self.scale],
             Image.ANTIALIAS), box=(x*self.scale, y*self.scale))
        self.tkimage = ImageTk.PhotoImage(self.image)
        self._update()

    def _update(self):
        self.label.configure(image=self.tkimage)
        self.label.image = self.tkimage
        self.root.update()

    def Clear(self):
        """
        clears display to black
        """
        self.Fill((0, 0, 0))

    def SetPWMBits(self, n):
        """
        Not applicable to simulation
        """
        pass

    def SetPixel(self, x, y, r, g=None, b=None):
        """
        draws a pixel on the matrix at x,y

        works with scaled displays
        """
        try:
            r = int(r)
            self.draw.rectangle(
                (x*self.scale, y*self.scale,
                 x*self.scale + self.scale - 1,
                 y*self.scale + self.scale - 1),
                fill=(r, g, b))
        except TypeError:
            pass
            # r, g, b = *r
            self.draw.rectangle((x, y, x + self.scale - 1, y + self.scale - 1),
                                fill=r)
        self.tkimage = ImageTk.PhotoImage(self.image)
        self._update()

    def SetBuffer(self):
        """
        Not applicable to simulation
        """
        pass

    def Fill(self, color):
        """
        """
        self.draw.rectangle((0, 0, self.dims[0], self.dims[1]), fill=color)
        self.tkimage = ImageTk.PhotoImage(self.image.copy())
        self._update()
