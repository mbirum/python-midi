from RPi import GPIO
from time import sleep
import sys
import os

swPin1 = int(sys.argv[1])
swPin2 = int(sys.argv[2])
swPin3 = int(sys.argv[3])

GPIO.setup(swPin1, GPIO.IN)

try:

    while True:
        sw1 = GPIO.input(swPin1)
        sw2 = GPIO.input(swPin2)
        sw3 = GPIO.input(swPin3)

        if sw1 == 0 and sw2 == 0 and sw3 == 0:
            os.system('/devl/midi/update')
    
        sleep(0.01)


finally:
    print "done"
