import pigpio
import time

pi=pigpio.pi()

#pi.hardware_PWM(19, 50, 50000) #PWM on pin 13 at 50Hz with 5% duty cycle
pi.set_mode(18, pigpio.OUTPUT)
pi.hardware_PWM(18, 60000, 200000) #PWM on pin 18
