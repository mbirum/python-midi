from RPi import GPIO
from time import sleep
import sys
import os


swPin1 = int(sys.argv[1])
swPin2 = int(sys.argv[2])
swPin3 = int(sys.argv[3])

GPIO.setup(swPin1, GPIO.IN)

try:
    sw = GPIO.input(swPin1)
    print sw
    #os.system('echo %s > /sys/class/gpio/export'%(swPin1))
    #os.system('echo %s > /sys/class/gpio/export'%(swPin2))
    #os.system('echo %s > /sys/class/gpio/export'%(swPin3))

    #while True:
        #os.system('/devl/midi/update %s %s %s'%(swPin1,swPin2,swPin3))
    
        #sleep(0.01)


finally:
    print "done"
