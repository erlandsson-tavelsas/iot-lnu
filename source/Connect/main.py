import socket
import time

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)


# Your old code from main.py should be here

# EXAMPLE: Create a DHT object, collect data in the loop and send it

while True:
    temperature = 23    # Mock value
    humidity = 40       # Mock value
    s.send(bytes([temperature, humidity]))
    print('sent temperature:', temperature)
    print('sent humidity:', humidity)
    time.sleep(900)     # wait 900 seconds (15 minutes) before sending again
