from Tkinter import *
from PIL import Image, ImageTk
import threading
from time import sleep


class display():
    def run(self, t, k):
        self.root = Tk()
        image = Image.open("test.gif")
        photo = ImageTk.PhotoImage(image)
        self.label = Label(image=photo)
        self.label.image = photo
        # keep a reference!
        self.label.pack()
        self.t = threading.Thread(target=t)
        self.t.start()
        self.root.mainloop()
        k()

    def setImage(self, img):
        img = ImageTk.PhotoImage(img)
        self.label.configure(image=img)
        self.label.image = img


def test():
    sleep(2)
    disp.setImage(Image.open("test1.gif"))


def kill():
    pass

if __name__ == '__main__':
    disp = display()
    disp.run(test, kill)
