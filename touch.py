import Adafruit_MPR121.MPR121 as MPR121
from time import sleep
import sys
import os
import led
import touchmap

channel = sys.argv[1]

strength = 115
increment = 0.01
updatePin = 10

cap = MPR121.MPR121()
if not cap.begin():
    print('Error initializing MPR121')
    sys.exit(1)
    
#led.powerOn()

last_touched = cap.touched()
while True:
    
    current_touched = cap.touched()
    
    for i in range(12):    
        pin_bit = 1 << i

        # If transitioning to touched from not touched
        if current_touched & pin_bit and not last_touched & pin_bit:
            if (updatePin == i):
                os.system('/bin/bash -c /home/pi/devl/midi/update')
            else:
                velocity=hex(strength).split('x')[1]
                note=hex(int(touchmap.pinValue(i))).split('x')[1]
                message='9%s %s %s'%(channel,note,velocity)
                os.system('amidi --port="hw:1,0,0" -S \'%s\''%(message))

    last_touched = current_touched
    sleep(increment)