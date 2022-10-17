from machine import Pin
from utime import sleep

red = Pin(22, Pin.OUT)
yellow = Pin(21, Pin.OUT)
green = Pin(19, Pin.OUT)

while True:
  red.toggle()
  sleep(5)
  red.toggle()
  yellow.toggle()
  sleep(1)
  yellow.toggle()
  green.toggle()
  sleep(2)
  green.toggle()
  yellow.toggle()
  sleep(1)
  yellow.toggle()
