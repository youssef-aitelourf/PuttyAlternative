import serial
import time

# Configure the serial port and baud rate to match your Arduino settings
ser = serial.Serial('/dev/tty.usbmodem1101', 460800)  # Change 'COM3' to your Arduino's serial port

# Give some time for the serial connection to establish
time.sleep(2)

# Open the text file for writing
with open('output.txt', 'w') as file:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(line)
            file.write(line + '\n')
            file.flush()
