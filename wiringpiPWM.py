import wiringpi

#https://raspberrypi.stackexchange.com/questions/4906/control-hardware-pwm-frequency

pin = 18
wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(pin, 2)
#wiringpi.pinMode(pin, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS) #put PWM in mark-space mode, required to set frequency
wiringpi.pwmSetClock(400) #pwmFrequency in Hz = 19.2e6 Hz / pwmSetClock / pwmSetRange.
wiringpi.pwmSetRange(800) # TOP value for PWM counter

wiringpi.pwmWrite(pin, 50)    # duty cycle between 0 and 1024. 0 = off, 1024 = fully on 
