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

So to begin with, i will present a table below containing the materials used for my project. I will also add a table below the first one that describes possible additions and alternatives to some of the devices i used.

| **Item**        | **Cost**           | **Description**  |
| :------------ |--------------:| :-----|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |
