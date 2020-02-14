from RPi import GPIO
from time import sleep
import sys
import os

clkPin = int(sys.argv[1])
dtPin = int(sys.argv[2])
swPin = int(sys.argv[3])
channel = sys.argv[4]

GPIO.setmode(GPIO.BCM)
GPIO.setup(clkPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dtPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(swPin, GPIO.IN)

min = 3
max = 123
pos = min
clkLast = GPIO.input(clkPin)
dtLast = GPIO.input(dtPin)
swLast = GPIO.LOW
swToggle = False
swPressed = False
posLast = pos

try:

    increment = 0.0001
    while True:

	sw = GPIO.input(swPin)
	if GPIO.LOW == sw:
		swPressed = True
	elif swPressed:
		swToggle = not swToggle
		print swToggle
		swPressed = False

	clk = GPIO.input(clkPin)
        dt = GPIO.input(dtPin)
        full = True

        #half or full click
        if clk != dt:
            full = False
            
        if full:
            #left click
            if clkLast != clk and dtLast == dt:
                pos -= 6
                if pos < min:
                    pos = min
            #right click
            elif dtLast != dt and clkLast == clk:
                pos += 6
                if pos > max:
                    pos = max

            if posLast != pos:
                code=hex(pos).split('x')[1]
                message='B%s 01 %s'%(channel,code)
                #print('B%s 01 %s'%(channel,code))
                os.system('amidi --port="hw:1,0,0" -S \'%s\''%(message))

        clkLast = clk
        dtLast = dt

        posLast = pos
        sleep(increment)

finally:
    os.system('midichan reset $channel')
    GPIO.cleanup()
    print "done"
