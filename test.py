#!/usr/bin/env python3

import time
from pymouse import PyMouse
from pprint import pprint
import sys

mouse = PyMouse()
screenSize = mouse.screen_size()

scaleFactor = 100
scaledMaxValue = int(screenSize[1] / scaleFactor)
pause = 1

for i in range(0, scaledMaxValue):
  currentPosition = mouse.position()
  y = i * scaleFactor
  x = currentPosition[0]
  print(y)
  #mouse.move(currentPosition[0], y)
  mouse.click(x, y, 2)
  time.sleep(pause)
