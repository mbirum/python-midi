import time
import sys
import os
import busio
import digitalio
import board
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# set up pins for push buttons
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

channel = sys.argv[1]

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)

last_read = 0
tolerance = 250
left_pressed = False
right_pressed = False

def remap_range(value, left_min, left_max, right_min, right_max):
    left_span = left_max - left_min
    right_span = right_max - right_min

    valueScaled = int(value - left_min) / int(left_span)
    
    return int(right_min + (valueScaled * right_span))

while True:

    if GPIO.input(12) == GPIO.HIGH and not left_pressed:
      left_pressed = True
      print("Left pressed")
    else:
      left_pressed = False
        
    if GPIO.input(18) == GPIO.HIGH and not right_pressed:
      right_pressed = True
      print("Right Pressed")
    else:
      right_pressed = False
    
    trim_pot_changed = False

    # read the analog pin
    trim_pot = chan0.value

    # how much has it changed since the last read?
    pot_adjust = abs(trim_pot - last_read)

    if pot_adjust > tolerance:
        trim_pot_changed = True

    if trim_pot_changed:
        # convert 16bit adc0 (0-65535) trim pot read into 0-127 midi control level
        pedalValue = remap_range(trim_pot, 0, 65535, 0, 127)
        
        code=hex(pedalValue).split('x')[1]
        message='B%s 02 %s'%(channel,code)
        #print(message)
        os.system('amidi --port="hw:1,0,0" -S \'%s\''%(message))

        last_read = trim_pot

    time.sleep(0.0001)

