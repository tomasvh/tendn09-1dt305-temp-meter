# Tutorial on how to build an Air and Water temperature meter powered by solar-panel and battery
A simple project for a water and air temperature meter and tutorial how to implement it and transfer data to pybytes.

Author: Tomas Marx-Raacz von Hidvég

Student credentials: tend09(Linneaus University)

Approximate time consumption to finish with tutorial: From scratch, 4-6 hours


## Table of content 

[Project Overview](https://github.com/tomasvh/tendn09-1dt305-temp-meter/blob/main/README.md#1)
[Project Objectives]()
[Project Materials]()
[Further material motivation and considerations]()
[Computer and IDE setup]()
[Physical Wiring of the device.]()
[Quick electrical calculation]()
[Platform of choice]()
[The code]()
[Device and program connectivity]()
[My own test of the device]()
[Finisihing thoughts]()



## 1 Project Overview {#1}

This tutorial will show you how to build a simple temperature meter for monitoring air temperature from a sensor on the breadboard
as well as water temperature from a digital waterproof sensor.

The tutorial will show you how to wire your device, how to set up your IDE(programming environment) to mirror mine, how to program your device using python with the help of both 
built in and imported libraries as well as how to connect it to Pybytes platform to display the data.

Furthermore I aim to introduce a way of getting this piece of hardware to be almost self sufficient when it comes to power.

This project was spawned and realised during the summer course 1dt305 at Linnaeus University of Kalmar in Sweden.


## 2 Project Objectives {#2}

Now to get started lets ask ourselves why you would build such a device?

When sitting on your laptop out in the yard with a cold beer(or other beverage), you might want to know the temperature of the outside air aswell as the temperature of the beer(or other beverage)?

While this is indeed a honorable and viable reason, it is mainly a joke from my part. 

My reason to build this device and application was first and foremost to monitor
outside temperature and water temperature at our households hottub from a distance instead of walking the 8 flights of stairs to the point where said hot tub is situated just to 
check when the bathing temperature has been reached.

Now, this intention back-fired slightly due to delivery issues(for LTE connection) as well as the fact that my house, although it is in an area where LoRa and SigFox exists, is in a deep valley and as such in radio shadow (unable to connect to these types of services) the end result for my actual project, due to the distance to above mentioned hot-tub, is more towards the first comical description off application.

That being said, for individuals that do live in an area with LoRa or SigFox coverage(without being in radio shadow) this project can still be a basis for an even better implementation of a more long range sensor.

However, for individuals that do not have their hot-tub, beach, pier or other measurement point where this type of dual sensor might come in handy outside wifi range, the current implementation will work marvelously.


## 3 Project Materials {#3}

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


### 3.1 Further material motivation and considerations {#3.1}

So after this brief overview of the materials it is time to explain the choices.
I went with the FiPy initially for the LTE capability due to the fact that, before stepping in to the course, i thought the other communication protocols lacked the range.
However, in hindsight a LoPy is quite enough to produce the project described. Along with this development platform an expansion board and breadboard is added for ease of use. 

I then went with the two sensors, one analog for placement on the breadboard and one digital waterproof sensor with a cord. The latter of the two requires a 0,25w 4.7kohm resistor to work.

Along with this comes the wires to connect the FiPy/LoPy to the breadboard and sensors, the one linked above is a set and contains all the wires needed for this project.

My aim for this project has always been to create a sort of "fire and forget" device that continues to work without constantly exchanging batteries. In that perspective i choose to invest in a solarpanel and a rechargeable battery. It is however easier and slightly less costly to buy the alternative AAA batterypack listed in the second table.
The solar panel and charger does not come with a double female connector cord needed to connect it to the actual device, and hence a single cord with a female, as well as a seperate JST-PH female connector was needed(I.e you will have to actually produce your own cord) becase this form of cord was virtually impossible to find.


## 4 Computer and IDE setup {#4}

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

## 5 Physical Wiring of the device. {#5}

Now to replicate my exact project you need to follow the following Schema:


![How to connect](https://github.com/tomasvh/tendn09-1dt305-temp-meter/blob/main/Pictures/fritzingDone.png "How to connect")

1. To start off with a disclaimer, in the upper left corner is the battery and solarpanel solution that i am utilizing, this can easily be exchanged towards a standard, non rechargable batterypack as mentioned earlier.

The connection of the the solution is very self explanatory, on the charger there is a "solar panel in", a "Battery in" and a "system out". The system out cord needs assembling from the parts mentioned in the materials section.

2. As you can see from the image i am using 2 power draws from the expansion board, 3v3 to the upper lane on the breadboard and VIN to the lower. This is due to the fact that the digital temperature sensor (DS18B20) does not work with the 3v3, it needs more power. The analog sensor however works absolutely fine with the 3v3, in fact, it is recommended to use it.

3. From the horizontal power lanes where you connected the power you should now draw the power(red) to the vertical device lanes. Same goes for the ground(GND, black/blue) For the Analog sensor there is a slight issue on how to put it on the board, and which pin is supposed to be power and ground(i.e which way to face the sensor). Look at the datasheet for the sensor to figure out which way to turn it and what pin is what. For the digital sensor it is self explenatory as this sensor comes with colored cords where red is power, black is ground(gnd) and white is data.

4. The data is then connected, Digital sensor to Pin 10 and Analog sensor to pin 16. Important is also the resistor that needs to be connected between the power lane for the digital sensor and the data lane.

### 5.1 Quick electrical calculation {#5.1}

So how much does this device draw in terms of power, and will this little concept of self sufficiency be enough?

To begin with, as we will see later when coming down to the code there has been some issues which makes it hard to implement a power saving mode on this project(I will not say it is impossible, i am just saying that i have not found a way to implement it so that the sensors keep working).

Now, according to specifications from the [datasheet of the Fipy](https://www.mouser.com/datasheet/2/872/fipy-specsheet-1129442.pdf) these are the power drainage numbers:

Fipy with no radios: 62.7 mA

WiFi Access point(read idle): 126 mA

WiFi client (in use) : 137 mA

LoRa and SigFox modems are turned off by default if not in use and LTE has been turned off through code.

And for the sensors:

[Analog sensor](https://www.electrokit.com/uploads/productfile/41016/2243473.pdf): 12µA(Idle) and 15µA(Usage) 

[Digital sensor](https://www.electrokit.com/uploads/productfile/41010/DS18B20.pdf): 1000nA(Standby) and 1.5mA(Usage)

On Idle this would make the powerdraw: 62.7 + 126 + 0.012 = 188.712mA

On Usage this would increase to: 62.7 + 137 + 0.015 + 1.5 = 201.215mA

The program runs for about 10 seconds every 15 minutes which makes the usage negligable in the grand scheme, so we will be counting towards the idle.

The Battery charger has a maximum output of 500mA, but the solarpanel only has a maximum output of 170mA

With a rough estimation of the solarpanel working on average at optimal performance for for 12 hours what would produce an input of 85mA(wishful thinking except in summertime in Sweden, but its a estimation for the purpose of calculating).

With the idle of 188.712mA minus the produced estimated 85mA average that leaves 103.712 mA consumption.
Running this result in a [Battery life](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-battery-life) calculator results in a life expectancy of 19.2 hours, which is in no way great.

To counteract this a larger solar panel could be used, A good aim would probably be to have a solar panel with a capacity of around 400-450mA, this would let the device regain what was lost during the day and thus be or atleast be very close to self-sufficient. 
**Important to note** is that you in this case should install a overcharge protection on the battery.

## 6 Platform of choice {#6}

I chose to run this project using Pycoms own platform Pybytes. When connected to this cloud service(which is free) your data is saved for one month and can through their portal be displayed in a very nice matter. It is also extremely easy to connect your device to this platform with easy to use tutorials. Especially through WiFi which we have used in this project.

The platform also works as a point of access through which you can access and send on your data to different other cloud platforms(AWS, Google Cloud, Microsoft Azure) or by webhooks send it on to a custom service on for example your own server. This is done through the platforms "integration section".

An expansion of this application that i myself have considered, but not implemented due to lack of time is to use above mentioned webhooks. The way this works is that every time the platform recieves a signal from your device, a POST call is sent to a URL of your choice(For example a node.js server that listens to this specific URL) which in turn saves it to a suitable database and displays it in a more accessable way than through the portal.

You can also, as mentioned above use one of the existing large cloud platforms to collect the data to be accessed to external applications.

It all comes down to what types of hardware/server capabilites you have yourself and what kind of wallet space you have for the implementation.

As for this project i have chosen to stop the entire process at Pybytes and display the results there for now and will thus go no further in explaining the ways of handling the data.


## 7 The code {#7}

1. Now, Jumping off at the point of chapter 4 of this tutorial we must now create a folder from where we will upload our code to the device.
When that is done, download the four files in the "src" folder in this repository and put them in the newly created folder.

2. Now open said folder in VS code and create a folder named "lib". In this folder create a file called **"onewire.py"** and copy/paste the code from the Library section of the [Pycom deviced code](https://docs.pycom.io/tutorials/hardware/owd/). This is the library that allows for communication with this kind of sensor and is of outmost importance. Press CTRL+S to save the file.

3. You should now have 4 files in the main folder along with above mentioned file, by clicking these links you will go straight to the commented code:

* [boot.py](https://github.com/tomasvh/tendn09-1dt305-temp-meter/blob/main/src/boot.py), This is a start file that is run on boot-up, what it does is tell the device to run main.py

* [main.py](https://github.com/tomasvh/tendn09-1dt305-temp-meter/blob/main/src/main.py), this is the main file, it imports the analogTemp.py and ds18b20.py and runs them to collects the temperatures as well as sending it on to pybytes. It also controlls the idle timing, making the device wait 15 minutes between every send.

* [analogTemp.py](https://github.com/tomasvh/tendn09-1dt305-temp-meter/blob/main/src/analogTemp.py), This module controls the collection of data from the analog sensor and converts what is read into a celcius number that can be read by a human being.

* [ds18b20.py](https://github.com/tomasvh/tendn09-1dt305-temp-meter/blob/main/src/ds18b20.py), This module imports the onewire.py and uses it to collect digital signals from the sensor and convert it to a celcius number that can be read by a human being.

4. Uploading the code is done by pushing the "upload" button in the bottom colored section where you found the "Pymakr console" button before.

5. To make the application talk to pybytes you must first register an account on [their platform](https://sso.pycom.io/login/?client_id=pycom&redirect_uri=https%3A%2F%2Fpyauth.pybytes.pycom.io%2Fauth_code%2Fcallback&scope=profile&response_type=code&state=pybytes-browser), register the device and then choose WiFi as your network of choice using this very nice and clear [tutorial](https://docs.pycom.io/pybytes/gettingstarted/).
What this tutorial process does is to connect your device to Pybytes and update your device through a piece of software and a token key. It also creates a configuration file on your device which Pybytes then uses to connect through WiFi to upload data to the platform. **Observe:** During this process you will have to have your device connected through USB and VS code shut down.

6. After this you will have to define two signals on your Pybytes platform, number 1 and 2, the first signal this program and device will send is the analog temperature on the breadboard. The second is the digital waterproof sensor. Naming convention of these signals is up completely up to you.

Through the interface in the signals you can add diagrams and also "place them on dashboard" which will be your main view for the device. You can configure your dashboard in any way you would like.

7. You should now be good to go to use the device and send information to pybytes to be displayed on your dashboard.

## 8 Device and program connectivity {#8}

Now, what we have done throughout this project is set up a device and configure it to send information to Pybytes and there display it in a nice manner.
The device will send data to the platform every 15 minutes through WiFi and the MQTT protocoll using the configuration file set up by Pybytes through the provisioning section(Step 5 in the previous section). The timing for this transfer of data is easily changed by changing the "sleepTime" variable in the main.py file on line 21.
Making the device send more often will however increase the power draw slightly, but as this device does not go into Deep Sleep but only works on delay time, the difference should be slight.

WiFi as you probably know is a protocoll for short range and high traffic. It is used all around us and is a way to connect all forms of devices to the internet through access points, routers or mesh systems. Most of the time it runs on the 2,4ghz or 5ghz bands.

MQTT is a messaging standard used for connection and communication messages to and from IoT devices. It works in a Client(sender) to Broker to Client(Subscriber) way.
In this case the sender is the device and Pybytes acts as the broker aswell as the subscribing client in the form of data collection and displaying.

The service from Pybytes makes life easy when it comes to setting up the connections through their configuration file, but it is entirely possible to set up these kinds of things yourself. but it will require a lot more code and knowledge on how the device works.

## 9 My own test of the device {#9}

Part of the time spent writing this tutorial/report i ran a field test of the device using a glass of water acting as the "hot tub" and on battery power.
I had not recieved the JST-PH connector needed to create the cord between charger and device so only the battery was used for this test.
The device ran for a number of hours and was manually disconnected at one point, i.e it did not run out of power.
At one point(between 3.30 pm and 3.54 pm) i introduced a handful of ice to the glass of water to make the readings a little bit more interesting. The temperature dropped 13.5 degrees C and started to slowly climb upwards again after that.
There was also a very varied weather outside during the test(to which i had an open window) which produced some interesting variations in the air temperature of the room as well which showed in the test.

![measurement result](https://github.com/tomasvh/tendn09-1dt305-temp-meter/blob/main/Pictures/Capture.JPG)

As mentioned before Pybytes saves 1 month worth of data, so if you want a more persistant collection of temperature for statistical purposes or such matters i suggest anyone that choose to replicate this project to investigate the "Integration" section of Pybytes. This is their portal to sending data onwards to other locations as described previously. As for my own part, statistics was not interesting, as the purpose of this sensor was in fact to read the most recent reading and not to see change over time. However, this application and device, with a few modifications would most definately suit such purposes.

## 10 Finisihing thoughts {#10}






