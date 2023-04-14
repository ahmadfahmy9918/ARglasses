import pyglet
import import_ipynb
import Capstone.ipynb
import ssd1309
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import board
#import circuitpython
#from circuitpython.shared_bindings 
import audiobusio
import digitalio
import time
import numpy
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import tables  
import librosa
import librosa.display
import tensorflow


data_in = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate=16000, bit_depth=16)

wave_file = open("recording.wav", "wb")
wave_file.write(b'RIFF****WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x80\x00\x00\x02\x00\x10\x00data****')

start_time = time.monotonic()

while time.monotonic() - start_time <5:
    sample = data_in.record(160)
    wave_file.write(sample)

wave_file.close()

#dataset = 

window = pyglet.window.Window()

@window.event
def on_draw():
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        label.draw()
        
        
        


