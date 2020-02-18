from RPi import GPIO
import sys
import os


swPin1 = int(sys.argv[1])
swPin2 = int(sys.argv[2])
swPin3 = int(sys.argv[3])

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(swPin1, GPIO.IN)
GPIO.setup(swPin2, GPIO.IN)
GPIO.setup(swPin3, GPIO.IN)

try:
    sw1 = GPIO.input(swPin1)
    sw2 = GPIO.input(swPin2)
    sw3 = GPIO.input(swPin3)

    if sw1 == GPIO.LOW or sw2 == GPIO.LOW or sw3 == GPIO.LOW:
        command = 'cd /devl/midi/src && git pull && cd -'
        os.system(command)


finally:
    GPIO.cleanup()
