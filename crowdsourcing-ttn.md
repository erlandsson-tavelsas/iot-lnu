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


# The things network (TTN) demystified

The things network is a crowd sourced LoRa network ... where there are others like Helium ... each of them with a goal
of increasing coverage which for some locations might be the only option ... but also to provide a backend collector of 
things data.

## How to setup a TTN gateway and using a TTN mapper to measure coverage

Give a short and brief overview of what your project is about.
What needs to be included:

- [ ] Title
- [ ] Your name and student credentials (xx666xxx)
- [ ] Short project overview
- [ ] How much time it might take to do (approximation)

### Objectives

Describe why you have chosen to build this specific device. What purpose does it serve? What do you want to do with the data, and what new insights do you think it will give?

- [ ] Why you chose the project
- [ ] What purpose does it serve
- [ ] What insights you think it will give

### Material

You really don't need your own TTN gateway but my original problem was the lack of LoRa presence so to start working
I did purchase a cheaper variant, the The Things Indoor Gateway for approximately EUR 80 (incl VAT). There are plenty
of other gateways you can use but this one comes with a automatic setup for TTN. 

One might notice the difference between the TTN version 2 and version 3 where the latter has abandoned the simplified 
Semtech UDP Packet Forwarder setup which I first started to test with a cheaper (1-channel) gateway, the Dragino LG01-N. 
I did manage to get this up and running but the lack of features in the TTN stack ... 

Measure the coverage requires sensors able to provide GPS coordinates, where the Pytrack fit well together with the LoPy4
micro controller, the combination would end up in a very neat and slim hardware configuration. I also invested some money 
in the LoRa and GPS antenna to ensure that both the GPS as well as the LoRa coverage measure would not depend on the mapper but
rather the gateway itself.

Explain all material that is needed. All sensors, where you bought them and their specifications. Please also provide pictures of what you have bought and what you are using.

| Component | Capabilities | Price (incl VAT, excl freight) | Vendor link | 
| --------- | ---------------- | ---------| ------- |
| [Pycom Lopy4](https://pycom.io/product/lopy4/)   | Microcontroller | SEK 480 | [Digikey](https://www.digikey.se/products/sv?keywords=lopy4) |
| [Pytrack 2.0.x Expansion board](https://pycom.io/product/pytrack-2-0-x/)  | GPS | SEK 460 | [Mouser](https://www.mouser.se/ProductDetail/Pycom/604565286017?qs=sGAEpiMZZMv0NwlthflBi98X9085w8V%252BtWaXU%252BemDPA%3D) |
| Pycom LoRa/Sigfox antenna | Send/receive | SEK 180 | [Digikey](https://www.digikey.se/product-detail/sv/pycom-ltd/SIGFOX-LORA-ANTENNA-KIT/1871-1005-ND/7721843) |
| External GPS antenna  | Increased GPS receiver | SEK 225 | [Mouser](https://www.mouser.se/ProductDetail/Pycom/604565430465?qs=sGAEpiMZZMv0NwlthflBi%252BaVk7F50MhHRCD37BDS1ng%3D) |
| [The Things Indoor Gateway](https://connectedthings.store/gb/lorawan-gateways/indoor-lorawan-gateways/the-things-indoor-gateway-868-mhz.html) | LoRaWAN gateway | SEK 750 | [RS-Components](https://se.rs-online.com/web/p/communication-wireless-development-tools/2018876) |

At the time, some components where hard to find and as the idea of the project shifted I had to purchase material from 
more than one vendor, however the freight cost from Mouser was 0 for orders exceeding SEK 500 so an additional GPS antenna
make that on free of charge. You should also have in mind that all the vendors above have a Swedish interface but is 
located outside EU (except RS-Components) which means that you have to be aware of taxes required when importing this.

You should also know that when this report was written, there was a global lack of semi-conductors and the brexit 
grinded the gear when it comes to transports within UK. Even though that I only ordered items in stock, the Digikey 
order took more than 2 weeks from confirmed to when it was delivered.

>In this project I have chosen to work with the Pycom LoPy4 device as seen in Fig. 1, it's a neat little device programmed by MicroPython and has several bands of connectivity. The device has many digital and analog input and outputs and is well suited for an IoT project.
>
>![LoPy!](https://pycom.io/wp-content/uploads/2018/08/lopySide-1.png)
>Fig. 1. LoPy4 with headers. Pycom.io


### Environment setup

The development environment I've used is atom.io with the pymakr plugin which works very well with the selected hardware. 
Setting up the environment is a straight forward task and instructions can be found here. However, if you like me, 
doesn't read the instructions in details you might find the error from atom.io hard to understand as they aren't always 
complaining about the actual problems but rather wrap it some other mysterious error message. 
 
LINK here

The installation of the Indoor gateway is a straight forward task, where I first registered an acccunt at The things network.
From there I opened up the Console and selected the cluster node Europe 1. 
...
...

Screenshot (listed gateways)

I you can see there I've two registered gateways, the TTIG and the previously mentioned 1-channel Dragino LG01-N. 
The difference is the cluster association where the older one can't be registered for the Europe 1 cluster but only 
"Other cluster" which is a dumpster for obsolete gateways (in this case a UDP package forwarder), still usable but very 
limited in TTN.

Once setup I needed to configure the gateway itself so it can connect to the TTN backend. 

Screenshot (Map before connected)

Once connected I expect to appear in the ttnmapper.org map as a connected but without coverage data gateway. 
We are now public and open for business...free of charge.

Screenshot (Map after connected)

### Putting everything together

The TTN mapper is a neat task to put together where wiring the antenna is the only externals that has to be attached 
to the Lopy4 resp. Pytrack expansion shield. As I previously mentioned the Lopy4 and Pytrack is a very compound unit easy 
to encapsulate and therefor as an experiment easy to be mobile. Mobility is a key concept for this kind of device as not 
being mobile would gain much when it comes to measure LoraWAN coverage.    

PICTURE HERE 

One should know that building a TTN mapper by yourself is about having fun more than filling in a gap in the market. 
With that in mind you might also consider cheaper(https://sensebox.de/projects/en/2020-03-06-ttn-mapper) hardware and 
perhaps a higher energy efficiency but the pycom parts has good documentation and with the pymakr plugin I would say 
that I'm happy with using these components.

The device desing is simple but we need to consider how to power the device and reason about the power source. 
Using a deep sleep approach to preserve battery requires us to wait before getting coordinates as the GPS locator required 1 - 2 minutes to be accurate. 
So, why did we then choose the Pytrack at all? The reason is simple, this is the nature of the GPS itself so regardless if we are using the Pytrack or 
any other disintegrated GPS locator we need to wait for it after it is powered up. With Pytrack we don't need an shield, like Expansion Board (link here) and a circuit board 
used for wiring the sensor so the Pytrack is quite cheap even though the GPS capability itself could be found slight cheaper. 
So back to problem with the power consumption ...

To achieve a lot of coverage data we would probably need to travel by some kind of vehicle, preferably a car or something. This means that we would probably power the device 
from the cars cigarette outlet by a simple USB cable. Even though if we would change our preferred way to travel around using a bicycle we could use the same connector
(USB) and power the device with a cheap power bank or similar, in my case a very cheap power bank (6700 mAh) bought years ago at Clas Ohlsson.
The sensor would also most certainly return to home every day so a long lived autonomous existence would not be necessary. 

However, even though we have a continuous power supply, there are still design consideration about the actual communication which we need to address 
when it comes to TTN platform.

Finally, the GPS sensor is quit sensitive when it comes to locating satellites, if you like me, sitting at your office you should 
use an external GPS antenna which allows you to sit inside and still being able to have GPS coverage. Attaching the antenna listed above
is "a-cannot-do-it-wrong-task" but as the antenna is an active antenna you need to place a jumper connecting the two pins below. 
The Pytrack comes without this jumper so you need to borrow it from elsewhere 

How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

- [ ] Circuit diagram (can be hand drawn)
- [ ] Electrical calculations
- [ ] Limitations of hardware depending on design choices.
- [ ] Discussion about a way forward - is it possible to scale?

### Platforms and infrastructure

Describe your choice of platform(s). You need to describe how the IoT-platform works, and also the reasoning and motivation about your choices. Have you developed your own platform, or used 

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

- [ ] Describe platform in terms of functionality
- [ ] Explain and elaborate what made you choose this platform
- [ ] Provide a pricing discussion. What are the prices for different platforms, and what are the pros and cons of using a low-code platform vs. developing yourself?

### The code

Import core functions of your code here, and don't forget to explain what you have done. Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.


```python=
import this as that

def my_cool_function():
    print('not much here')

s.send(package)

# Explain your code!
```

### The physical network layer

How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

- [ ] How often is the data sent? 
- [ ] Which wireless protocols did you use (WiFi, LoRa, etc ...)?
- [ ] Which transport protocols were used (MQTT, webhook, etc ...)
- [ ] Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.
- [ ] What alternatives did you evaluate?
- [ ] What are the design limitations of your choices?

### Visualisation and user interface

Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

- [ ] Provide visual examples on how the visualisation/UI looks. Pictures are needed.
- [ ] How often is data saved in the database. What are the design choices?
- [ ] Explain your choice of database. What kind of database. Motivate.
- [ ] Automation/triggers of the data.
- [ ] Alerting services. Are any used, what are the options and how are they in that case included.

### Finalizing the design

Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

- [ ] Show final results of the project
- [ ] Pictures
- [ ] *Video presentation

---