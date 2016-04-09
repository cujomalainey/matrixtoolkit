#!/usr/bin/env python

from distutils.core import setup

setup(name='matrixtoolkit',
      version='0.5',
      description='LED Matrix Emulation Package',
      author='Curtis Malainey',
      author_email='curtis@malainey.com',
      url='https://github.com/cujomalainey/matrixtoolkit',
      packages=['matrixtoolkit'],
      requires=['pillow', 'tkinter'],
      license='MIT License',
      )
