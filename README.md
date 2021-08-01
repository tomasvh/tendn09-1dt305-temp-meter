# Tutorial on how to build an Air and Water temperature meter powered by solar-panel and battery
A simple project for a water and air temperature meter and tutorial how to implement it and transfer data to pybytes.

Author: Tomas Marx-Raacz von Hidvég

Student credentials: tend09(Linneaus University)

Approximate time consumption to finish with tutorial: From scratch, 4-6 hours


# 1 Project Overview

This tutorial will show you how to build a simple temperature meter for monitoring air temperature from a sensor on the breadboard
as well as water temperature from a digital waterproof sensor.

The tutorial will show you how to wire your device, how to set up your IDE(programming environment) to mirror mine, how to program your device using python with the help of both 
built in and imported libraries as well as how to connect it to Pybytes platform to display the data.

Furthermore I aim to introduce a way of getting this piece of hardware to be almost self sufficient when it comes to power.

This project was spawned and realised during the summer course 1dt305 at Linnaeus University of Kalmar in Sweden.


# 2 Project Objectives

Now to get started lets ask ourselves why you would build such a device?

When sitting on your laptop out in the yard with a cold beer(or other beverage), you might want to know the temperature of the outside air aswell as the temperature of the beer(or other beverage)?

While this is indeed a honorable and viable reason, it is mainly a joke from my part. 

My reason to build this device and application was first and foremost to monitor
outside temperature and water temperature at our households hottub from a distance instead of walking the 8 flights of stairs to the point where said hot tub is situated just to 
check when the bathing temperature has been reached.

Now, this intention back-fired slightly due to delivery issues(for LTE connection) as well as the fact that my house, although it is in an area where LoRa and SigFox exists, is in a deep valley and as such in radio shadow (unable to connect to these types of services) the end result for my actual project, due to the distance to above mentioned hot-tub, is more towards the first comical description off application.

That being said, for individuals that do live in an area with LoRa or SigFox coverage(without being in radio shadow) this project can still be a basis for an even better implementation of a more long range sensor.

However, for individuals that do not have their hot-tub, beach, pier or other measurement point where this type of dual sensor might come in handy outside wifi range, the current implementation will work marvelously.


# 3 Project Materials

So to begin with, i will present a table below containing the materials used for my project along with a description and links to where you can buy them(mostly in Sweden or from the main supplier). I will also add a table below the first one that describes possible additions and alternatives to some of the devices i used.

| **Item**        | **Cost**           | **Description**  |
| :------------ |:-------------| :-----|
| [Fipy](https://pycom.io/product/fipy/)      | 65 Euro | The actual development platform |
| [Expansion board](https://pycom.io/product/expansion-board-3-0/)      | 17,5 Euro      |   Expansion board with powersupply and usb connector as well as sockets for pins. |
| [Analog temperature sensor](https://www.electrokit.com/produkt/mcp9700a-to-92-temperaturgivare/) | 1.5 euro      |    A simple analog temperature sensor with pins. |
| [Digital temperature sensor](https://www.electrokit.com/produkt/temperatursensor-vattentat-ds18b20/) | 18 Euro | A digital temperature sensor in water tight casing. |
| [170 mA 5.5v solar panel](https://www.tinytronics.nl/shop/en/power/solar-panels/seeed-studio-solar-panel-5.5v-170ma-80x100mm-with-jst-ph-connector) | 4.5 Euro | 80x100mm solar panel with JST-PH female connector. |
| [Battery charger(max 500mA) with JST-PH male connectors](https://www.tinytronics.nl/shop/en/power/bms-and-chargers/li-ion-and-li-po/without-protection-circuit/cn3065-li-ion-solar-charger-500ma) | 4 Euro | A board with battercharging capabilities and throughput of power to main device. |
| [Resistor 4,7kohm](https://www.electrokit.com/produkt/motstand-kolfilm-0-25w-4-7ohm-4r7/) | 0,1 Euro | Resistor needed for the digital sensor. |
| [Connector wires between breadboard and expansionboard](https://www.electrokit.com/produkt/kopplingstrad-byglar-for-kopplingsdack-mjuka-65st/) | 3,9 Euro | Wires needed to connect sensors to the micro-computer. |
| [Bread board(Connector board)](https://www.electrokit.com/produkt/kopplingsdack-400-anslutningar/) | 5,9 Euro | Breadboard used to connect sensors to the device. |
| [IP 65 devicebox(a bit oversized)](https://www.electrokit.com/produkt/apparatlada-gra-med-flans-222x146x75mm/) | 17,9 Euro | A plastic box for containing the device and protect it from water. |
| [Micro USB cord(data))](https://www.electrokit.com/produkt/usb-kabel-a-hane-micro-b-5p-hane-1-8m/) | 3,9 Euro | 1,8 meter Micro USB cord for communication with device during development. |
| [Insulation tape)](https://www.electrokit.com/produkt/eltejp-19mm-x-25m-svart/) | 2,5 Euro | Used to keep pins in place and protect solderings.  |
| [Soldering set](https://www.electrokit.com/produkt/lodset-starter-kit/) | 14,9 Euro | Basic soldering set.  |
| [JST-PH cord between charger and device](https://www.electrokit.com/produkt/batterisladd-jst-ph-2-pol-100mm/) | 1 Euro | Cord with 1 female JST-PH connector  |
| [JST-PH female connector](https://www.electrokit.com/produkt/kontakthus-ph-2-pol-2mm/) | 0.2 Euro | Female JST-PH connector  |



Above mentioned items are exactly everything used to realise this project, however, due to the fact that i did not manage to get my hands on a LTE Antenna in time for this project report you can actually get by with Pycoms LoPy microcomputer instead of the FiPy.


| **Alternative Item**        | **Cost**           | **Description**  |
| :------------ |:-------------| :-----|
| [LoPy](https://pycom.io/product/lopy4/)      | 38,5 Euro | The cheaper kind of development platform |
| [LTE antenna kit](https://pycom.io/product/lte-m-antenna-kit/)      | 9 Euro | The Antenna that never arrived |
| [AAA Batterypack](https://www.electrokit.com/produkt/batterihallare-3xaaa-med-strombrytare-och-jst-kontakt/)      | 2.9 Euro | Alternative powersupply |

**Observe** that this tutorial will in no way explain how to implement and connect the LTE connection.


# 3.1 Further material motivation and considerations

So after this brief overview of the materials it is time to explain the choices.
I went with the FiPy initially for the LTE capability due to the fact that, before stepping in to the course, i thought the other communication protocols lacked the range.
However, in hindsight a LoPy is quite enough to produce the project described. Along with this development platform an expansion board and breadboard is added for ease of use. 

I then went with the two sensors, one analog for placement on the breadboard and one digital waterproof sensor with a cord. The latter of the two requires a 0,25w 4.7kohm resistor to work.

Along with this comes the wires to connect the FiPy/LoPy to the breadboard and sensors, the one linked above is a set and contains all the wires needed for this project.

My aim for this project has always been to create a sort of "fire and forget" device that continues to work without constantly exchanging batteries. In that perspective i choose to invest in a solarpanel and a rechargeable battery. It is however easier and slightly less costly to buy the alternative AAA batterypack listed in the second table.
The solar panel and charger does not come with a double female connector cord needed to connect it to the actual device, and hence a single cord with a female, as well as a seperate JST-PH female connector was needed(I.e you will have to actually produce your own cord) becase this form of cord was virtually impossible to find.


# 4 Computer and IDE setup

Moving on from the actual physical part of the materials it is time to discuss the development environment.

For this project i used a Windows 10 Pro based computer with the IDE Virtual Studio Code as my development environment/Code editor and Pymakr plugin.

To set this up i would like to point your attention to [Pycoms own tutorial](https://docs.pycom.io/gettingstarted/) for setting this up with a few additions.
I will link to subsections and additional sites below.

1. First attach the FiPy to the expansion board the right way(i did not in the beginning which produced a very unneeded headache):
![Expansionboard setup](https://pycom.io/wp-content/uploads/2020/03/Website-Product-Shots-ExpB-front-LoPy4.png "Physical setup")
Notice the way the text is oriented on the FiPy and the expansion board, this is a very good indication on the right direction to put it.
2. Connect the USB/Micro USB connector to the computer and to the expansion board.
3. Download and Install [Visual Studio Code](https://code.visualstudio.com/)(From this point abrevated VS Code), During the installation, make sure the installer adds VS Code to "PATH".
4. Download and Install the [Node LTS version](https://nodejs.org/en/), During the installation, make sure the installer adds node to "PATH".
5. Now, hit the windows button and enter "Device Manager" in the search field and enter it. Manouver down to the ports section and check which COM port is connected.
6. Update [Device](https://docs.pycom.io/updatefirmware/device/) and [Expansionboard](https://docs.pycom.io/updatefirmware/expansionboard/) firmware using these guides.
7. Now start VS code and install the [Pymakr plugin](https://docs.pycom.io/gettingstarted/software/vscode/) using this guide.
8. Inside VS code Hold down CTRL+SHIFT+P on your keyboard to open command palette in VS Code and type "list", further commands will be listed below the input field, choose "Pymakr > Extra's > List serial ports". This will list all the com ports and most likely also copy the one it wants to the clipboard. Hold down CTRL+SHIFT+P again and enter "GLobal settings", chose the only option listed. This will open the global settings for Pymakr. Find the section "adress" and change it to the COM port you recieved in this process. press CTRL+S to save the settings.
9. Now in VS code, go upp to the Terminal menu and choose new terminal. In the section that pops up in the bottom of the program window there is a subsection to the right. It should say list "Pymakr console", choose that one. Below said terminal is a colored board with a number of buttons, on the left hand side you should now have "Pymakr console" button with an "X" before it, push that button and it should now connect to the device.
10. Congratulations, if everything is according to plan you should now be connected to the device and have the environment set up for the next steps.

# 5 Physical Wiring of the device.

Now to replicate my exact project you need to follow the following Schema:


![How to connect](https://github.com/tomasvh/tendn09-1dt305-temp-meter/blob/main/Pictures/fritzingDone.png "How to connect")

1. To start off with a disclaimer, in the upper left corner is the battery and solarpanel solution that i am utilizing, this can easily be exchanged towards a standard, non rechargable batterypack as mentioned earlier.

The connection of the the solution is very self explanatory, on the charger there is a "solar panel in", a "Battery in" and a "system out". The system out cord needs assembling from the parts mentioned in the materials section.

2. As you can see from the image i am using 2 power draws from the expansion board, 3v3 to the upper lane on the breadboard and VIN to the lower. This is due to the fact that the digital temperature sensor (DS18B20) does not work with the 3v3, it needs more power. The analog sensor however works absolutely fine with the 3v3, in fact, it is recommended to use it.

3. From the horizontal power lanes where you connected the power you should now draw the power(red) to the vertical device lanes. Same goes for the ground(GND, black/blue) For the Analog sensor there is a slight issue on how to put it on the board, and which pin is supposed to be power and ground(i.e which way to face the sensor). Look at the datasheet for the sensor to figure out which way to turn it and what pin is what. For the digital sensor it is self explenatory as this sensor comes with colored cords where red is power, black is ground(gnd) and white is data.

4. The data is then connected, Digital sensor to Pin 10 and Analog sensor to pin 16. Important is also the resistor that needs to be connected between the power lane for the digital sensor and the data lane.

# 5.1 Quick electrical calculation




