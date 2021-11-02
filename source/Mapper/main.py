#!/usr/bin/env python
#
# Copyright (c) 2020, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#
import machine
import math
import network
import os
import time
import utime
import gc
import pycom
import socket
import struct
import binascii
from network import LoRa
from machine import RTC
from machine import SD
from L76GLNSV4 import L76GNSS
from pycoproc_2 import Pycoproc

# Turn of the default blinking every 4 seconds
pycom.heartbeat(False)

# Red while connecting to LORA
pycom.rgbled(0xFF0000)
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = binascii.unhexlify('0000000000000000')
app_key = binascii.unhexlify('4C19D2CE8B3B94393C44AB29E6A31D2B')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

for x in range(20):
    if not lora.has_joined():
        print('Not joined yet...attempt, (x+1))
        time.sleep(2.5)

if not lora.has_joined():
    print('Could not join network, will try again later')
    machine.deepsleep(60000);
else:
    print('Network joined!')

 # Yellow while checking satellites
pycom.rgbled(0xFFFF00)

time.sleep(2)
gc.enable()

# Borrowed code, unsure if this is required by the Pytrack to have
# correct readings from the satellites. Need to understand...
# setup rtc
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print('\nRTC Set from NTP to UTC:', rtc.now())
utime.timezone(7200)
print('Adjusted from UTC to EST timezone', utime.localtime(), '\n')

# Borrowed code, could be removed if you are sure you have
# setup the hardware correctly
py = Pycoproc()
if py.read_product_id() != Pycoproc.USB_PID_PYTRACK:
    raise Exception('Not a Pytrack')

time.sleep(1)
l76 = L76GNSS(py)

# Blocking wait until the GPS is fixated and have a reading
l76.get_fix()

# Green light indicating that we have a fix and are about to get
# the job done
pycom.rgbled(0x00FF00)

while (True):
    # Check if the GPS is awake and have a reading
    if l76.fixed() :
        # Read values one by one and convert them to floats
        # Could be more efficient by reading them all at the same time
        lat = float(l76.gps_message('GGA',debug=False)['Latitude'])
        long = float(l76.gps_message('GGA',debug=False)['Longitude'])
        sv = float(l76.gps_message('GGA',debug=False)['NumberOfSV'])
        hdop = float(l76.gps_message('GGA',debug=False)['HDOP'])

        # Make sure we have a valid reading and that the quality is good enough
        # for the mapper integration, otherwise we should not spend any airtime
        if hdop is not None and hdop < 1.0:
            # Open socket only if GPS is fixed and with a correct reading
            s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
            s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
            s.setblocking(False)

            # Payload size is 16 bytes (4*4) but can be optimized by omitting the sv (-4 bytes) or convert
            # sv to an unsigned integer (-2 bytes but requires additional logic at recipient transformation)
            s.send(struct.pack('<10f',lat,long,sv,hdop))

            # Signal success, blue light
            pycom.rgbled(0x0000FF)
            time.sleep(5) # Sleep 5 seconds so you can

            # Keep the GPS powered up even though the machine is in deepsleep, this will result
            # a faster "fix" and keep satellites "in sight"
            py.go_to_sleep(gps=True)
            machine.deepsleep(60000) # Sleep for 1 minute
        else:
            # Red light means waiting for GPS or quality is poor
            pycom.rgbled(0xFF0000)
            time.sleep(30) # Sleep 30 seconds before retrying
    else :
        # Red light means waiting for GPS
        pycom.rgbled(0xFF0000)
        time.sleep(30) # Sleep 30 seconds before retrying

    # Yellow light lit to indicate retrying
    pycom.rgbled(0xFFFF00)
