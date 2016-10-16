# there is something wrong with GPIO.output ()

import RPi.GPIO as GPIO
import time

pin = 23

time.sleep(3)
print "GPIO.setmode(GPIO.BCM)"
GPIO.setmode(GPIO.BCM)

# this will switch the relay on
time.sleep(3)
print "GPIO.setup(pin, GPIO.OUT)"
GPIO.setup(pin, GPIO.OUT)

# it doesn't work
# time.sleep(3)
# print "GPIO.output(pin, 0)"
# GPIO.output(pin, 0)

# this will switch the relay off
time.sleep(3)
print "GPIO.cleanup()"
GPIO.cleanup()

time.sleep(3)
print "GPIO.setmode(GPIO.BCM)"
GPIO.setmode(GPIO.BCM)


# this will switch the relay on
time.sleep(3)
print "GPIO.setup(pin, GPIO.OUT)"
GPIO.setup(pin, GPIO.OUT)

# it doesn't work
# time.sleep(3)
# print "GPIO.output(pin, 1)"
# GPIO.output(pin, 1)


# this will switch the relay off
time.sleep(3)
print "GPIO.cleanup()"
GPIO.cleanup()

time.sleep(3)
print "end"
