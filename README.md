# matrixtoolkit
A simple toolkit for testing python led matrix scripts without the matrix

This simple toolkit allows users to emulate an LED matrix in a Tkinter window without any of the required hardware for deployment.

## How to use

The diplay object replaces the Adafruit_RGBMatrix object in your code with three exceptions.

1. When you would call ```matrix.SetImage(image.im.id, 0, 0)``` you actually call ```matrix.SetImage(image, 0, 0)```
2. call ```matrix.start(run, kill)``` right before you want to start your main loop but after your done initializing, anything after this command will not get run until tk quits, the next thing that will get run is what you passed in as your first parameter. The reason is, tkinter must hold the main thread, so the package hijacks it and creates a new one for your code to run on. If tk quits before your code, you can be alerted by the function pointer you pass in as the second function.
3. When you initialize the matrix object, you can pass in an optional scale parameter, by default it is 6. See the example for usage.

All other commands in the package have the same parameters and do the exact same operations (where applicable.)
