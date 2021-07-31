# Tutorial on how to build an Air and Water temperature meter powered by solar-panel and battery
A simple project for a water and air temperature meter and tutorial how to implement it and transfer data to pybytes.

Author: Tomas Marx-Raacz von Hidvég

Student credentials: tend09(Linneaus University)

Approximate time consumption to finish with tutorial: From scratch, 4-6 hours


# Project Overview

This tutorial will show you how to build a simple temperature meter for monitoring air temperature from a sensor on the breadboard
as well as water temperature from a digital waterproof sensor.

The tutorial will show you how to wire your device, how to set up your IDE(programming environment) to mirror mine, how to program your device using python with the help of both 
built in and imported libraries as well as how to connect it to Pybytes platform to display the data.

Furthermore I aim to introduce a way of getting this piece of hardware to be almost self sufficient when it comes to power.


# Project Objectives

Now to get started lets ask ourselves why you would build such a device?

When sitting on your laptop out in the yard with a cold beer(or other beverage), you might want to know the temperature of the outside air aswell as the temperature of the beer(or other beverage)?

While this is indeed a honorable and viable reason, it is mainly a joke from my part. 

My reason to build this device and application was first and foremost to monitor
outside temperature and water temperature at our households hottub from a distance instead of walking the 8 flights of stairs to the point where said hot tub is situated just to 
check when the bathing temperature has been reached.

Now, this intention back-fired slightly due to delivery issues(for LTE connection) as well as the fact that my house, although it is in an area where LoRa and SigFox exists, is in a deep valley and as such in radio shadow (unable to connect to these types of services) the end result for my actual project, due to the distance to above mentioned hot-tub, is more towards the first comical description off application.

However, for individuals that do not have their hot-tub, beach, pier or other measurement point where this type of dual sensor might come in handy outside wifi range, the current implementation will work marvelously.


# Project Materials

So to begin with, i will present a table below containing the materials used for my project along with a description and links to where you can buy them(mostly in Sweden or from the main supplier). I will also add a table below the first one that describes possible additions and alternatives to some of the devices i used.

| **Item**        | **Cost**           | **Description**  |
| :------------ |:-------------| :-----|
| [Fipy](https://pycom.io/product/fipy/)      | 65 Euro | The actual micro computer |
| [Expansion board](https://pycom.io/product/expansion-board-3-0/)      | 17,5 Euro      |   Expansion board with powersupply and usb connector as well as sockets for pins |
| [Analog temperature sensor](https://www.electrokit.com/produkt/mcp9700a-to-92-temperaturgivare/) | 1.5 euro      |    A simple analog temperature sensor with pins |
| [Digital temperature sensor](https://www.electrokit.com/produkt/temperatursensor-vattentat-ds18b20/) | 18 Euro | A digital temperature sensor in water tight casing |
| [170 mA 5.5v solar panel](https://www.tinytronics.nl/shop/en/power/solar-panels/seeed-studio-solar-panel-5.5v-170ma-80x100mm-with-jst-ph-connector) | 4.5 Euro | 80x100mm solar panel with JST-PH female connector |
| [Battery charger(max 500mA) with JST-PH mail connectors](https://www.tinytronics.nl/shop/en/power/bms-and-chargers/li-ion-and-li-po/without-protection-circuit/cn3065-li-ion-solar-charger-500ma) | 4 Euro | A board with battercharging capabilities and throughput of power to main device |
| [Resistor 4,7kohm](https://www.electrokit.com/produkt/motstand-0-6w-1-4-7kohm-100-pack/) | 5 Euro | Resistor needed for the digital sensor(100 pack in link) |
