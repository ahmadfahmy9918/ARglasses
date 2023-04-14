import numpy as np


import bluetooth

import pyglet
import sounddevice as sd

########## Audio Processing Code 
# Define the sample rate and number of samples to record
fs = 44100  # Sample rate
duration = 5  # Duration in seconds

# Record audio data
recording = sd.rec(int(fs * duration), samplerate=fs, channels=1)
sd.wait()  # Wait for recording to complete

# Apply a Fast Fourier Transform to the audio data
fft_data = np.fft.fft(recording)

# Print the FFT data
print(fft_data)




########### BT CODE
# Create a socket to handle the Bluetooth communication
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

# Bind the socket to a port
port = 1
server_sock.bind(("",port))

# Start listening for incoming connections
server_sock.listen(1)

# Accept an incoming connection
client_sock,address = server_sock.accept()
print("Accepted connection from ",address)

# Send data to the connected device
client_sock.send("Hello World!")

# Close the connection
#client_sock.