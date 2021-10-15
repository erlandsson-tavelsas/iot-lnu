
#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

import time
import pycom
from onewire import DS18X20
from onewire import OneWire
from dht import DTH

#DS18B20 data line connected to pin P10
#ow = OneWire(Pin('P10'))
#temp = DS18X20(ow)
#DHT11 connected to pin P9
dht = DTH('P9', 0)

while True:
#    temp.start_conversion()
#    time.sleep(10)
#    print('DS18: ', temp.read_temp_async())
    result = dht.read()
    while not result.is_valid():
        print('Not valid, will try again shortly')
        time.sleep(.5)
        result = dht.read()
    temp = result.temperature
    humidity = result.humidity

    if temp < 20 and humidity > 40:
        pycom.rgbled(0x0004ff)
    elif temp > 20 and humidity < 40:
        pycom.rgbled(0x00ff04)
    else:
        pycom.rgbled(0xe5ff00)

    time.sleep(10)
