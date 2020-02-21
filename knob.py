from RPi import GPIO
from time import sleep
import sys
import os
import led

clkPin = int(sys.argv[1])
dtPin = int(sys.argv[2])
swPin = int(sys.argv[3])
knobIncrement = int(sys.argv[4])
channel = sys.argv[5]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(clkPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dtPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(swPin, GPIO.IN)

min = 0
max = 127
pos = min
clkLast = GPIO.input(clkPin)
dtLast = GPIO.input(dtPin)
swLast = GPIO.input(swPin)
posLast = pos

try:

    led.power(GPIO.HIGH)

    increment = 0.0001
    counter = 0.0
    while True:
	
	c = int(counter * 10000)
	if 100 == c:
		counter = 0.0
		sw = GPIO.input(swPin)
		if sw != swLast:
			if sw == GPIO.LOW:
				#print "Pressed!"
				message='9%s 01 7f'%(channel)
				os.system('amidi --port="hw:1,0,0" -S \'%s\''%(message))

		swLast = sw

	clk = GPIO.input(clkPin)
        dt = GPIO.input(dtPin)
        full = True

        #half or full click
        if clk != dt:
            full = False
            
        if full:
            #left click
            if clkLast != clk and dtLast == dt:
                pos -= knobIncrement
                if pos < min:
                    pos = min
            #right click
            elif dtLast != dt and clkLast == clk:
                pos += knobIncrement
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
	counter += increment
        sleep(increment)

finally:
    os.system('/devl/midi/midichan reset %s'%(channel))
    GPIO.cleanup()
    print "done"
