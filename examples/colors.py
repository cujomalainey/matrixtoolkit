from PIL import Image, ImageDraw
from time import sleep

OFF_TARGET = True

if OFF_TARGET:
    from matrixtoolkit import Adafruit_RGBmatrix
else:
    from rgbmatrix import Adafruit_RGBmatrix


class drawer():
    """
    controls what is being drawn
    """

    def __init__(self):
        # this config switch is optional as scale is by default 6
        if OFF_TARGET:
            self.matrix = Adafruit_RGBmatrix(32, 4, scale=5)
        else:
            self.matrix = Adafruit_RGBmatrix(32, 4)
        self.alive = True

    def run(self):
        if OFF_TARGET:
            self.matrix.start(self.main, self.kill)
        else:
            self.main()

    def main(self):
        self.image = Image.new('RGB', (64, 32))
        draw = ImageDraw.Draw(self.image)
        try:
            while self.alive:
                self.matrix.Fill((0, 255, 0))
        except KeyboardInterrupt:
            # hook in to make sure any future deconstructors are called
            self.kill()

    def updateMatrix(self, image):
        self.matrix.SetImage(image if OFF_TARGET else
                             image.im.id, 0, 0)

    def kill(self):
        self.alive = False

if __name__ == '__main__':
    d = drawer()
    d.run()
