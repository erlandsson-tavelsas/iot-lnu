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
from machine import RTC
from machine import SD
from L76GLNSV4 import L76GNSS
from pycoproc_2 import Pycoproc

pycom.heartbeat(False)
pycom.rgbled(0xFFFF00) # Yellow, setting things up

time.sleep(2)
gc.enable()

# setup rtc
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print('\nRTC Set from NTP to UTC:', rtc.now())
utime.timezone(7200)
print('Adjusted from UTC to EST timezone', utime.localtime(), '\n')

py = Pycoproc()
if py.read_product_id() != Pycoproc.USB_PID_PYTRACK:
    raise Exception('Not a Pytrack')

time.sleep(1)
#l76 = L76GNSS(py, timeout=30, buffer=512)
l76 = L76GNSS(py)

# Blue light indicating getting a fix
pycom.rgbled(0x0000FF)

l76.get_fix()

# Yellow light indicating that we have a fix and are about to get the job done
pycom.rgbled(0xFFFF00)

while (True):
    # Check if the GPS is awake and have a reading
    if l76.fixed() :
        lat = float(l76.gps_message('GGA',debug=False)['Latitude'])
        long = float(l76.gps_message('GGA',debug=False)['Longitude'])
        sv = float(l76.gps_message('GGA',debug=False)['NumberOfSV'])
        hdop = float(l76.gps_message('GGA',debug=False)['HDOP'])

        # Make sure we have a valid reading and that the quality is good enough
        # for the mapper integration
        if hdop is not None and hdop < 1.0:
            # Open socket only if GPS is fixed and with a correct reading
            s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
            s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
            s.setblocking(False)
            s.send(struct.pack('<10f',lat,long,sv,hdop))
            # Signal success, green light
            pycom.rgbled(0x00FF00)
            time.sleep(5) # Sleep 5 seconds

            # Keep the GPS powered even though the machine is in deepsleep, which allows us
            # for a faster "fix" and with satellites still in sight
            py.go_to_sleep(gps=True)
            machine.deepsleep(120000) # Sleep for 2 minutes
        else:
            # Red light means waiting for GPS or quality is poor
            pycom.rgbled(0xFF0000)
            time.sleep(30) # Sleep 30 seconds before retrying
    else :
        # Red light means waiting for GPS
        pycom.rgbled(0xFF0000)
        time.sleep(30) # Sleep 30 seconds before retrying
    # Blue light lit to indicate retrying
    pycom.rgbled(0xFFFF00)

"""
# sleep procedure
time.sleep(3)
py.setup_sleep(10)
py.go_to_sleep()
"""
