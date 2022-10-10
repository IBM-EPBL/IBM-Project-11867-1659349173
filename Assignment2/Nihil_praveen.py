import random
from time import sleep

def random_values():
  temperature = random.randint(5, 60)
  humidity = random.randint(5, 100)
  return humidity, temperature

humidity = temperature = 0

while True:
  humidity, temperature = random_values()
  print('Humidity:', humidity, 'Temperature:', temperature)
  if (temperature > 50):
    print("High Temperature Detected! \nAlarm Triggered")
  sleep(1)
