#!/usr/bin/env python

import time
from pymouse import PyMouse
import midi
from pprint import pprint
import sys


#pattern = midi.read_midifile('/home/claudio/Downloads/EspanjaPrelude.mid')
# pattern = midi.read_midifile('/home/claudio/Development/python-midi/mary.mid')

# events = []
# for track in pattern:
#   for event in track:
#     if isinstance(event, midi.events.NoteOnEvent):
#       print(type(event))
#       events.append(event)
# events.sort()
# pprint(events)
# sys.exit()


mouseButton = 1 # 1 for left 2 for right click

mouse = PyMouse()
screenSize = mouse.screen_size()

scaleFactor = 32
scaledMaxValue = int(screenSize[1] / scaleFactor + 1)
pause = 1

for i in range(0, scaledMaxValue):
  currentPosition = mouse.position()
  y = i * scaleFactor
  x = currentPosition[0]
  print(y)
  #mouse.move(currentPosition[0], y)
  mouse.click(x, y, 2)
  time.sleep(pause)
