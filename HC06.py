import time
import board
import busio
import digitalio
import bluetooth

# Create a software serial instance for GP16 and GP17
uart = busio.UART(board.GP16, board.GP17, baudrate=9600)

# Create a digital output for the HC-06
hc06_key = digitalio.DigitalInOut(board.GP18)

# Turn on the HC-06 module
hc06_key.switch_to_output(value=True)
time.sleep(1)

# Create a Bluetooth serial instance
bt = bluetoothio.BluetoothSerialConnection()

# Connect to the device
bt.start_client('00:11:22:33:44:55', port=1)

# Send data to the device
while True:
    data = 'Hello, World!'
    bt.write(data)
    time.sleep(1)
