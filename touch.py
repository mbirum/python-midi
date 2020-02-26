import Adafruit_MPR121.MPR121 as MPR121
from time import sleep
import sys
import os
import led

channel = sys.argv[1])

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device
if not cap.begin():
    print('Error initializing MPR121')
    sys.exit(1)
    
pin_mapping = {
  5: '05',
  10: '10',
  1: '01',
  3: '03',
  4: '04',
  0: '00',
  6: '06',
  7: '07',
  8: '08',
  9: '09',
  2: '02',
  11: '11',
}

led.powerOn()

last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    
    for i in range(12):
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            code=hex(100).split('x')[1]
            print('9%s %s %s'%(channel,pin_mapping.get(pin_bit),code))

    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    time.sleep(0.01)