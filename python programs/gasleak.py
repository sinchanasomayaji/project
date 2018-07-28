import RPi.GPIO as x
import time

pulse=0
x.setmode(x.BCM)
x.setwarnings(False)
x.cleanup()

x.setup(12,x.OUT)
x.setup(24,x.IN,pull_up_down=x.PUD_UP)

def blink():
        x.output(12,x.HIGH)
        time.sleep(1)
        x.output(12,x.LOW)
        time.sleep(1)

def pcallback(channel):
        print(channel)
        global pulse
        pulse+=1
        print(pulse)
        print('water in liter',pulse/42.0)

x.add_event_detect(24,x.FALLING,callback=pcallback)
try:
        while(1):
                blink()

except:
        print('stopped')
        x.cleanup()



