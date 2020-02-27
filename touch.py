import Adafruit_MPR121.MPR121 as MPR121
from time import sleep
import sys
import os
import led

channel = sys.argv[1]

strength = 115
increment = 0.01

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device
if not cap.begin():
    print('Error initializing MPR121')
    sys.exit(1)
    
pin_mapping = {
  5: '58',
  10: '59',
  1: '60',
  3: '61',
  4: '62',
  0: '63',
  6: '64',
  7: '57',
  8: '56',
  9: '55',
  2: '54',
  11: '53',
}

#led.powerOn()

last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    for i in range(12):
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            velocity=hex(strength).split('x')[1]
            note=hex(pin_mapping.get(i)).split('x')[1]
            message='9%s %s %s'%(channel,note,velocity)
            #print(message)
            os.system('amidi --port="hw:1,0,0" -S \'%s\''%(message))

    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    sleep(increment)