from RPi import GPIO
import sys

def power(switch):
    ledPin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, switch)
    GPIO.cleanup()


if __name__ == '__main__':
    arg = sys.argv[1]
    if "on" == arg:
        power(GPIO.HIGH)
    if "off" == arg:
        power(GPIO.LOW)

