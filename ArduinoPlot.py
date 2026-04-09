import serial
import matplotlib.pyplot as plt
from collections import deque

PORT = 'COM3'
BAUD = 115200

ser = serial.Serial(PORT, BAUD)

# Store last 500 samples
data = deque([0]*500, maxlen=500)

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(data)

ax.set_ylim(0, 1000)  
ax.set_title("Microphone Signal")
ax.set_xlabel("Samples")
ax.set_ylabel("Amplitude")

while True:
    try:
        value = ser.readline().decode().strip()
        if value:
            data.append(int(value))

            line.set_ydata(data)
            plt.draw()
            plt.pause(0.001)

    except KeyboardInterrupt:
        break

ser.close()