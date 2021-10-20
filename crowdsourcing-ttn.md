# Expertkompetens 

## Project report - IoT report template 

###### tags: `planning` `examination`
---
**Table of Contents**


[TOC]

## How to write your report

We have chosen to streamline your assignment as a tutorial, written in the Markdown language using a standard template (below). The main reason behind this is to make it as simple as possible, still flexible and easy to share between all classmates and other peers.

The report should be available on a public Github repository.

```
Information want's to be free - let's keep everything open, shall we?
```

## Github

Publish your project directly to Github. In that case write your tutorial in the `README.md` file. If you have no prior experience with Github this is a very good first time to learn. Easiest is to use the Github Desktop application, or you can also do everything from the web browser (editing and uploading etc.). Also, there are Git-plugins for VSCode and Atom which also makes things very easy.

Make sure you create a public repository and also that you write the report in the `README.md` file.

![](https://i.imgur.com/mp596wk.png)
![](https://i.imgur.com/DwkCnGE.png)


## Some examples for inspiration

**Note these are from the basic courses.**

Check out this link: [Good examples from previous summer courses](https://hackmd.io/@lnu-iot/good-examples)



----

Some additional examples for inspiration.

- [GPS Car tracker with notification](https://www.instructables.com/id/GPS-Car-Tracker-With-SMS-Notification-and-Thingspe/)
- [Blynk style button](https://www.instructables.com/id/Arduino-Tutorial-BLYNK-Style-Button-and-ESP-01-Rel/)
- [IoT weather station](https://www.hackster.io/rijk_meurs/iot-weather-station-4c29c6)
- [Mini IoT weather station](https://www.hackster.io/FunguyPro/how-to-make-an-mini-iot-weather-station-58252d)
- [Distance sensor](https://community.mydevices.com/t/nodemcu-esp8266-hc-sr04/2872)

---


# The things network (TTN) ... at your place

My first idea of this project was to build some smart device for the agricultural sector where a later could use the data for predicting the future using Machine Learning. This is probably the most straight forward idea, collect data and then analyze it which is a less technical aspect but more about valuation. However, the idea ends abrupt before I really start working with it, where I realize that covering 20 acres of agricultural landscape requires something else than an WiFi. So, in order to got it to work I needed an alternative bearer able to send data to a collector where I decided to got for the LoRaWAN approach which seems to be well-balanced choice. 

Växjö Energi AB, VEAB, have a gateway for LoraWAN setup in the city area but the signal is not in sight where I live, 10 km away, so the project become a task to setup my own LoraWAN and evaluate the coverage per monetary unit (i.e. the amount of covered acres per Krona). To achieve such understanding I need to create a tool able to pick up the signal and measure it's strength and the device location and put this recording into a map which visualize these findings. Fortunately, there are a couple of community networks already having such features which allowed me to focus at the actual coverage and less at visualizing data. The choice fell at The Things Network (TTN) where the The Things Network Mapper application provided me with the visualization. Connecting to the TTN also allows me to work with The Things Stack (TTS) a back end stack which makes it possible to store and/or forward sensor data to other locations with both predefined but also custom made integrations where the above TTN Mapper is one of the predefined.    

TTN is a so called crowd sourced project where you could say that bring your own gateway helps extending the areas covered, in other words, if you don't have LoraWAN coverage at your location, setup your own gateway and share it.

### Objectives

Building a TTN Mapper is more fun than valuable but for me it's important to understand how far away from the gateway it would be possible to put sensors and using static locations (i e a fixed sensor location) wouldn't make it possible to walk around in the terrain and get an idea what causes a degradation in the coverage. 

A mobile TTN Mapper device is probably not an per-year autonomous device, nor is it a device that need to support military accuracy when it comes to geolocation, in my point of view a couple of meters would be fine as it still will give you a relevant score for the coverage. With that said, I down prioritize power consumption and exact position when the message was sent (based on the theoretically speed of a vehicle hosting the device), i e the time between GPS read and sending the message through LoraWAN.  

To be honest, I bought an indoor gateway and hoped that if I put it close to a window I might be able to have coverage a couple of meters from the house ... but I was wrong.

### Material

You really don't need your own TTN gateway but my original problem was the lack of LoraWAN presence so to start working I need such a transport gateway. I bought a cheaper variant, the The Things Indoor Gateway for approximately EUR 80 (incl VAT), but there are plenty
of other gateways you can use but this one comes with a automatic setup for TTN.

*When I first started I didn't realized that there is a new version (3) of the TTN where the simplified*
*Semtech UDP Packet Forwarder protocol has been abandoned something I realized as I first started to test with a cheaper (1-channel) gateway, the Dragino LG01-N. I did manage to get this up and running but the lack of support in the TTS forced me to abandon this setup quite fast.*

Measure the coverage requires a sensor able to provide the device with GPS coordinates, where the *Pytrack* fit well together with the *LoPy4* micro controller, the combination would end up in a very neat and slim hardware configuration. I also invested some money in the LoRa and GPS antenna to ensure that both the GPS as well as the LoRaWAN coverage measure would not depend on the TTN Mapper but rather the gateway itself.

Below you can find a list of the required hardware I used for the project and from where I order them.

| Component | Capabilities | Price (incl VAT, excl freight) | Vendor link | 
| --------- | ---------------- | ---------| ------- |
| [Pycom Lopy4](https://pycom.io/product/lopy4/)   | Microcontroller | SEK 480 | [Digikey](https://www.digikey.se/products/sv?keywords=lopy4) |
| [Pytrack 2.0.x Expansion board](https://pycom.io/product/pytrack-2-0-x/)  | GPS | SEK 460 | [Mouser](https://www.mouser.se/ProductDetail/Pycom/604565286017?qs=sGAEpiMZZMv0NwlthflBi98X9085w8V%252BtWaXU%252BemDPA%3D) |
| Pycom LoRa/Sigfox antenna | Send/receive | SEK 180 | [Digikey](https://www.digikey.se/product-detail/sv/pycom-ltd/SIGFOX-LORA-ANTENNA-KIT/1871-1005-ND/7721843) |
| External GPS antenna  | Increased GPS receiver | SEK 225 | [Mouser](https://www.mouser.se/ProductDetail/Pycom/604565430465?qs=sGAEpiMZZMv0NwlthflBi%252BaVk7F50MhHRCD37BDS1ng%3D) |
| [The Things Indoor Gateway](https://connectedthings.store/gb/lorawan-gateways/indoor-lorawan-gateways/the-things-indoor-gateway-868-mhz.html) | LoRaWAN gateway | SEK 750 | [RS-Components](https://se.rs-online.com/web/p/communication-wireless-development-tools/2018876) |

At the time, some components where hard to find and as the idea of the project shifted I had to purchase material from 
several vendors, however the freight cost from Mouser was 0 for orders exceeding SEK 500 so an additional GPS antenna
make that one free of charge. You should also have in mind that most of the vendors have a Swedish website but they are
located outside EU (except *RS-Components*) which means that you have to be aware of taxes required when importing this.

You should also know that when this report was written (autumn 2021), there was a global lack of semi-conductors and the brexit grinded the gears when it comes to transports within UK. Even though that I only ordered items in stock, the *Digikey* order took more than 2 weeks from confirmed to when it was delivered.

>![LoPy!](https://pycom.io/wp-content/uploads/2018/08/lopySide-1.png)
>Fig. 1. LoPy4 with headers. Pycom.io


### Environment setup

The development environment I've used is atom.io with the pymakr plugin which works very well with the selected hardware. 

Setting up the environment is a straight forward task and instructions can be found here. However, if you like me, 
doesn't read the instructions in details you might find the error from atom.io hard to understand as they aren't always 
complaining about the actual problems but rather wrap it some other mysterious error message. 

[Setting up the ENV LINK here]()

The installation of the Indoor gateway is a straight forward task, where I first registered an acccunt at The things network. From there I opened up the Console and selected the cluster node Europe 1 and then claim my newly purchased gateway.

[Claiming your gateway LINK here]()

...
...

Screenshot (listed gateways)

As you can see there I've two registered gateways, the TTIG and the previously mentioned 1-channel Dragino LG01-N. 
The difference is the cluster association where the older one can't be registered for the Europe 1 cluster but only 
"Other cluster" which is a dumpster for obsolete gateways (in this case a UDP package forwarder), still usable but very 
limited in TTS.

Once setup I needed to configure the gateway itself so it can connect to the TTN backend. 

Screenshot (Map before connected)

Once connected I expect to appear in the ttnmapper.org map as a connected but without coverage data gateway. 
We are now public and open for business...free of charge.

Screenshot (Map after connected)

### Putting everything together

The TTN mapper is a neat task to put together where wiring the antenna is the only externals that has to be attached 
to the Lopy4 resp. Pytrack expansion shield. As I previously mentioned the Lopy4 and Pytrack is a very compound unit easy 
to encapsulate and therefor as an experiment easy to be mobile. Mobility is a key concept for this kind of device as not being mobile would gain much when it comes to measure LoraWAN coverage.

PICTURE HERE 

One should know that building a TTN mapper by yourself is about having fun more than filling in a gap in the market. 
With that in mind you might also consider cheaper(https://sensebox.de/projects/en/2020-03-06-ttn-mapper) hardware and perhaps a higher energy efficiency but the pycom parts has good documentation and with the pymakr plugin I would say that I'm happy with using these components.

The device desing is simple but we need to consider how to power the device and reason about the power source. 
Using a deep sleep approach to preserve battery requires us to wait before getting coordinates as the GPS locator required 1 - 2 minutes to be accurate. 
So, why did we then choose the Pytrack at all? The reason is simple, this is the nature of the GPS itself so regardless if we are using the Pytrack or any other disintegrated GPS locator we need to wait for it after it is powered up. With Pytrack we don't need an shield, like Expansion Board (link here) and a circuit board used for wiring the sensor so the Pytrack is quite cheap even though the GPS capability itself could be found slight cheaper. 

So back to problem with the power consumption ...

To achieve a lot of coverage data we would probably need to travel by some kind of vehicle, preferably a car or something. This means that we would probably power the device from the cars cigarette outlet by a simple USB cable. Even though if we would change our preferred way to travel around using a bicycle we could use the same connector (USB) and power the device with a cheap power bank or similar, in my case a very cheap power bank (6700 mAh) bought years ago at *Clas Ohlsson*. The sensor would also most certainly return to home every day so a long lived autonomous device would not be necessary. 

However, even though we have a continuous power supply, there are still design consideration about the actual communication which we need to address when it comes to TTN platform.

Finally, the GPS sensor is quite sensitive when it comes to locating satellites, if you like me, sitting at your office you should use an external GPS antenna which allows you to sit inside and still being able to have GPS coverage. Attaching the antenna listed above is "a-cannot-do-it-wrong-task" but as the antenna is an active antenna you need to place a jumper connecting the two pins highlighted in the picture below. The Pytrack comes without this jumper so you need to borrow it from elsewhere.

![](C:\Users\tomerl001\OneDrive - Växjö kommun\Documents\IoT\ttnmapper\2021-10-18 10_12_06-Pytrack 2.0X.png)



### Platforms and infrastructure

The problem definition is about having LoraWAN coverage at the countryside but also sharing why the TTIG gateway was used for this project. TTIG is naturally connected with the TTN so using its TTS as backend is more about using what we already have. 

TTN is about to connect data using some standard communication or storage solution which makes it generic when it comes to connecting a device with an application, so you can think of TTN as middleware or service bus. There are many predefined configurations, MQTT, Webhooks but also vendor specific in Azure IoT Hub, AWS Iot to mention some. 

For this project we need to connect it to the TTN Mapper application which helds a storage for coverage metrics contributed by idealists (and perhaps one or two commercial actors) in a true crowndsourced community. So, the overall setup is quite simple, the device connects to (a) gateway using its device EUI and this is forwarded to the TTN mapper. 

The contract for the TTN mapper requires at least Latitude and Longitude together with a quality measure to get accepted by the TTN Mapper. These attributes needs to be commited by device and in our case we transformed then it to json format using a TTN payload formatter which is applied before transmitting the final payload to TTN Mapper. The transformer source can find below in the code section. 

Once done with the transformation we can switch on the TTN Mapper integration which in version 3 is done by a predefined webhook, this webhook defaults with necessary configuration where the recommendation is to add an "experiment" header when you start up your transmission. Experiments can be search for and seen at the TTN mapper web but will not appear in the public map. So, tuning it before removing the experiment name can be a good idea. 

The public community network uses a "fair use policy" which limits the airtime to 30 seconds every 24 hours per node (or device) which is small number and might not be useful for all devices. It also limits the number of downlink messages to 10/day and node. During the elaboration I used more than 30 seconds and day to test how it was reacting to an consumption exceeding the "fair use policy" but it seems like it is based on trust rather than an enforcing policy as all packages went through. 


### The code

Typically you put a lot of connectivity boot.py but I had hard times to light the Lopy RGB from there so instead I moved all the logic into the main.py file. I use the Lopy RGBLed as a indicator easy to spot when carry it around in the field. First we try to join the LoraWAN but as we probably aren't always in range we will retry 20 times before sleeping 60 seconds. Once joined we indicate by lighting the yellow color at the RGB which means we are open for business. 

```python
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

for x in range(20):
    if not lora.has_joined():
        print('Not joined yet...attempt ', (x+1))
        time.sleep(2.5)

if not lora.has_joined():
    print('Could not join network, will try again later')
    machine.deepsleep(60000);
else:
    print('Network joined!')

 # Yellow while checking satellites
pycom.rgbled(0xFFFF00)
```



And then we just carry on with the machine awake sending coordinates, satellites and hdop values as bytes, if and only if  the reading is accurate enough. We use the RGB light to monitor the state where blue is "waiting", green is "sending" and red indicates a "GPS accuracy problem", which typically happens the first 2 - 3 iterations while the GPS is fixating the satellites.



```python
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

            # Open socket only if GPS is fixed and with a correct reading with high quality
            s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

            try:
                s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
                s.setblocking(False)

                # Payload size is 16 bytes (4*4) but can be optimized by omitting the sv (-4 bytes) or convert
                # sv to an unsigned integer (-2 bytes but requires additional logic at recipient transformation)
                s.send(struct.pack('<10f',lat,long,sv,hdop))

            finally:
                # Close socket as we are done here
                s.close()

            # Signal success, blue light
            pycom.rgbled(0x0000FF)
        else:
            # Red light means waiting for GPS or quality is poor
            pycom.rgbled(0xFF0000)
    else :
        # Red light means waiting for GPS
        pycom.rgbled(0xFF0000)

    # Sleep 30 seconds before retrying
    time.sleep(30)

    # Green light lit to indicate next transmit window
    pycom.rgbled(0x00FF00)
```

There are two implementation, the [continuous on](https://github.com/erlandsson-tavelsas/iot-lnu/tree/main/source/Mapper%20-%20Always%20on) and the [deep sleep/awake](https://github.com/erlandsson-tavelsas/iot-lnu/tree/main/source/Mapper)

The deep sleep/awake is better suited for autonomous operations like being placed in a car and wake up every X minutes and perform a check. To avoid unnecessary start up time for the GPS, which takes 1 - 2 minutes to get accurate readings, there is a feature where you can put the machine in deep sleep but preserve the GPS powered. This is more or less the only difference between the two projects and could be summarized by these two line of code 

```python
# Keep the GPS powered up even though the machine is in deepsleep, this will result
# a faster "fix" and keep satellites "in sight"
py.go_to_sleep(gps=True)
machine.deepsleep(60000) # Sleep for 1 minute
```

### The physical network layer

The problem definition at first was how you could connect multiple devices for agricultural measures spread across 20 acres or more where some long range bearer was needed.  The lack of such bearer made me shifting focus and use some kind of self-service approach i e bring your own network and try to it as cheap as possible. So both Lora and Sigfox would have been candidates but Lora seems to be more "open" or better documented than Sigfox. It also might have been influenced by previous class of the course where there were a lot of samples connecting with Lora. 

For the Mapper device I started with the idea of a 1 minute execution cycle where the device was put in deep sleep between the send windows. 
The Pygate can be kept awake while the machine is into deep sleep which saves time when it wakes up. The GPS will need 1 - 2 minutes before having a so called "fix" at the satellites. Sending a message every 6 minute would have cost us 1 second airtime each hour (~0.1 seconds for each message) which allows us to have the device powered up 24/7. The source for this "machine deep sleep/ GPS keep awake" configuration could be found in the source catalog.

Depending on the speed you are traveling with there might be a potential problem like a scew between the GPS readings and the payload transmission, I also find it a little bit boring waiting for the wake up call and therefor made some adjustments making it better for walking. In this scenario I never put the machine into deep sleep unless it couldn't find a LoraWAN network to join. Instead we keep the device join and pumping events every X seconds. 

Starting with 10 seconds it allows us to rapidly create a pretty fine grained view over the coverage for my TTIG. Sending a message every 10 seconds consumes 0.6 seconds airtime every minute which allows us to map for only 50 minutes a day, a 4 km walk. With this configuration I noticed that we got "double-taps" or paired readings close to each other but still with a 10 seconds difference in time. This symptom is caused by internal caching in the used library, where GPS reads will eventually be *slight* stale at the time when data is requested from the driver.  Elaborating with the timing made me select a longer interval, every 30 seconds, which ended up as a well-balanced TTN Mapper device for walking, which allows us to use it for approximately 150 minutes a day or a 12 km walk with readings that are more accurate for each point than the 10 seconds approach. 

<img src="C:\Users\tomerl001\OneDrive - Växjö kommun\Documents\IoT\ttnmapper\2021-10-18 13_05_12-TTN Mapper.png" alt="Double taps highlighted in yellow boxes" style="zoom:50%;" />

![Evenly distributed, every 30 seconds](C:\Users\tomerl001\OneDrive - Växjö kommun\Documents\IoT\ttnmapper\2021-10-18 13_09_29-TTN Mapper.png)

The payload itself is kept at a bare minimum of 16 bytes, describing 4 float values, Longitude, Latitude, HDOP and Number of visible Satellites. 
There are still some optimization possible regarding passing a count (number of satellites) as float instead of an unsigned integer but as our device both had a power source and was not intended to be autonomous for longer than a day I decided to spare complexity at the transformer at server-side rather than save those 2 extra bytes. 

```python
# Payload size is 16 bytes (4*4) but can be optimized by omitting the sv (-4 bytes) or convert
# sv to an unsigned integer (-2 bytes but requires additional logic at recipient transformation)
s.send(struct.pack('<10f',lat,long,sv,hdop))
```

In the TTN console we can then easily pick up and transform the message by the built-in javascript formatter utility, one would notice that I've hardwired the altitude but this is on purpose as we most of time holding the device a meter above ground so we don't need to send this information in every request. This formatter is defined below the Applications section, selecting Payload formatters and then Uplink (incoming requests transformation).

```javascript
function decodeUplink(input) {
  function bytesToFloat(bytes) {
    var bits = bytes[3] << 24 | bytes[2] << 16 | bytes[1] << 8 | bytes[0];
    var sign = (bits >>> 31 === 0) ? 1.0 : -1.0;
    var e = bits >>> 23 & 0xff;
    var m = (e === 0) ? (bits & 0x7fffff) << 1 : (bits & 0x7fffff) | 0x800000;
    var f = sign * m * Math.pow(2, e - 150);
    return f;
  }
  
  return {
    data: {
      latitude : bytesToFloat(input.bytes.slice(0,4)),
      longitude : bytesToFloat(input.bytes.slice(4,8)),
      altitude : 1,
      sats : bytesToFloat(input.bytes.slice(8,12)),
      hdop : bytesToFloat(input.bytes.slice(12))
    },
    warnings: [],
    errors: []
  };
}
```



### Visualisation and user interface

The Things Stack (TTS) comes with a predefined Webhook for integrating with TTN Mapper application and it can also be found below the Application section (1) and Integrations (2) where you can find the template when you create a Webhook (3). 

<img src="C:\Users\tomerl001\OneDrive - Växjö kommun\Documents\IoT\ttnmapper\2021-10-19 12_25_40-Add custom webhook - LOPY4 General - The Things Network.png" style="zoom:50%;" />

Note, you can set an experimental name (4) which allows you to publish these values without promoting them to the public coverage map, very useful if you, let's say mixing up longitude and latitude values which is very common where I live ;)

When you finally start mapping coverage you will can see that everything works as expected by watching the Live data stream for the device (or application). You should see a stream of events with the type "Forward uplink data message" containing a JSON payload with the transformed values that we have recorded 

![](C:\Users\tomerl001\OneDrive - Växjö kommun\Documents\IoT\ttnmapper\2021-10-19 12_31_38-Application data - LOPY4 General - The Things Network.png)

The visualization in the [mapper](https://ttnmapper.org/) application is immediately available if you search for device EUI, gateway or experiment name in tab [Advanced maps](https://ttnmapper.org/advanced-maps/), the where the search result could be visualized in a [map](https://ttnmapper.org/devices/?device=eui-70b3d5499eca445d&startdate=&enddate=&gateways=on&lines=on&points=on) or exported as a [csv](https://ttnmapper.org/devices/csv-pg.php?device=eui-70b3d5499eca445d&startdate=&enddate=&gateways=on&lines=on&points=on) resultset. 

### Finalizing the design

With a couple of mapping sessions, trying to cover the the same distance for north, south, east and west directions from the gateway, I'm stunningly realize that the Indoor gateway way exceeded my expectations concerning range. Picking up points at each direction gives me an average of at least 400 meters with the best strength which means 400 * 400 * 3,14 ~= 500000 square meters which translates into 50 ha or 100 acres.   

![](C:\Users\tomerl001\OneDrive - Växjö kommun\Documents\IoT\ttnmapper\2021-10-19 13_39_56-TTN Mapper.png)

Within this range I also tested the Lora join capability a couple of times where it successfully manage to join the network. This means that within this range it would work setting sensor in deep sleep and wake up able to send data through the gateway. 

The cost per acres then ends up with SEK 7,50 for a low fare gateway. 

This means that costs of manage your own LoraWAN network wouldn't be an issue as the sensors themselves way exceeds the gateway cost. However, there are of course a couple of concerns that needs to be covered. 

First, setting up a gateway for professional use is probably better done with an outdoor gateway with a constant power supply compared to an indoor ditto plugged in into a random power outlet. Mounted at a high place will also extends the range multiple times and provide a more reliable situation for the scenario. Still affordable with a list price between SEK 4000 - 6000 cover at least 500 acres (yes, such linear approximation is stupid) but probably more. 

For agriculture measures the covered area would more or less exist as a open place, but many of the farms today is a mixed between agricultural and forrestry   



Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

- [ ] Show final results of the project
- [ ] Pictures
- [ ] *Video presentation

---