from RPi import GPIO
from time import sleep
import sys
import os

swPin1 = int(sys.argv[1])
swPin2 = int(sys.argv[2])
swPin3 = int(sys.argv[3])

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin1, GPIO.IN)
GPIO.setup(swPin2, GPIO.IN)
GPIO.setup(swPin3, GPIO.IN)

try:

    while True:
        sw1 = GPIO.input(swPin1)
        sw2 = GPIO.input(swPin2)
        sw3 = GPIO.input(swPin3)

        if sw1 == 0 and sw2 == 0 and sw3 == 0:
            os.system('/bin/bash -c /devl/midi/update')
    
        sleep(0.01)


finally:
    print "done"
