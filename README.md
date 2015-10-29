# matrixtoolkit
A simple toolkit for testing python led matrix scripts without the matrix

This simple toolkit allows users to emulate an LED matrix in a Tkinter window without any of the required hardware for deployment.

## How to use

The diplay object replaces the Adafruit_RGBMatrix object in your code with three exceptions.

1. when you would call ```matrix.SetImage(image.im.id, 0, 0)``` you actually call ```matrix.SetImage(image, 0, 0)```
2. When initializing the parameters are very different
  1. First parameter is your run function. This is the function in which your code runs its main loop.
  2. Second parameter is your kill function (ie your destructor) that runs when the window is closed
  3. Third parameter is your scale, an interger to scale the image by because it is really small otherwise
  4. Fourth is your dimensions (in pixels) of the target display (so your original LED size) in a ```(x,y)``` tuple
3. call ```matrix.run()``` right before you want to start your main loop but after your done initializing, anything after this command will not get run, the next thing that will get run is what you passed in as your first parameter. The reason is, tkinter must hold the main thread, so the package hijacks it and creates a new one for your code to run on.

All other commands in the package have the same parameters and do the exact same operations (where applicable.)
