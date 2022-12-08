from machine import Pin
import time

# pico W specific
led = Pin("LED", Pin.OUT)

while True:
  led(1)
  time.sleep(1)
  led(0)
  time.sleep(1)