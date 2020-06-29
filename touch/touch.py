import Adafruit_MPR121.MPR121 as MPR121
from time import sleep
import sys
import os
import touchmap

channel = sys.argv[1]

increment = 0.01
updatePin = 11

cap = MPR121.MPR121()
if not cap.begin():
    print('Error initializing MPR121')
    sys.exit(1)

last_touched = cap.touched()
while True:
    
    current_touched = cap.touched()
    
    for i in range(12):    
        pin_bit = 1 << i

        # If transitioning to touched from not touched
        if current_touched & pin_bit and not last_touched & pin_bit:
            n = touchmap.getNote(i)
            note = hex(int(n)).split('x')[1]
            message='9%s %s 7f'%(channel,note)
            os.system('amidi --port="hw:1,0,0" -S \'%s\''%(message))
        
        if not current_touched & pin_bit and last_touched & pin_bit:
            n = touchmap.getNote(i)
            note = hex(int(n)).split('x')[1]
            message = '8%s %s 7f'%(channel,note)
            os.system('amidi --port="hw:1,0,0" -S \'%s\''%(message))

    last_touched = current_touched
    sleep(increment)
