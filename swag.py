import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(1, gpio.OUT)

try:
    while(True):
        gpio.output(22, gpio.HIGH)   # 3.3v
        time.sleep(5)
        gpio.output(22, gpio.LOW)    # 0v
        time.sleep(1)
        
        





except KeyboardInterrupt:
    gpio.cleanup()
