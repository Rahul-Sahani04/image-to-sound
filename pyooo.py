from pyo import *

# Start the server
s = Server().boot()
s.start()

# Create a sine wave with a frequency of 440 Hz
a = Sine(freq=440, mul=0.1).out()

# Keep the server running to play the sound
s.gui(locals())
