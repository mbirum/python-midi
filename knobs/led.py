from RPi import GPIO
import sys

def power(switch):
    ledPin = 21
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, switch)

def powerOn():
    power(GPIO.HIGH)

def powerOff():
    power(GPIO.LOW)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    arg = sys.argv[1]
    if "on" == arg:
        powerOn()
    if "off" == arg:
        powerOff()
    GPIO.cleanup()

