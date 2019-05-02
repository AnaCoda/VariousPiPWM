import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)
p.start(50)
raw_input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()
