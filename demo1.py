import time, machine

# setup
led = machine.Pin(2, machine.Pin.OUT)
button = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    led.value(0)
    time.sleep(0.2)
    led.value(1)
    time.sleep(0.5)