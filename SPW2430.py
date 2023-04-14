import time
import board
import analogio

# Create an analog input instance for GP15
mic = analogio.AnalogIn(board.GP15)

# Read the microphone output
while True:
    # Normalize the output voltage to a value between 0 and 1
    voltage = mic.value / 65535
    # Convert the voltage to decibels (dB)
    db = 20 * (1.5 - voltage)
    # Print the dB value
    print('dB: {:.2f}'.format(db))
    # Wait for 0.1 seconds before reading again
    time.sleep(0.1)



