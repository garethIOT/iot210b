[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)

# Lab1 - PartB (RPi3 SenseHat and Quiz)

![SenseHat](https://gitlab.com/Gislason/iot-210B-student/blob/master/images/rpi_sensehat.png)

In this section of the lab you will

* Learn how to get your local IP Address and autoboot into program
* Explore the SenseHat features

## Autoboot

With an embedded device, it's sometimes useful to boot the device headless (no keyboard
or screen). SSH works well as a terminal window into the device.

Source code is in the `iot-210B-student/Lab1/src` folder.

Copy the file `ipaddr.py` to the Pi3 home directory

```
scp Lab1/src/ipaddr.py pi@iotXxxx/home/pi
```

Add the following line to /etc/rc.local near the end (just before exit 0)

```
python /home/pi/ipaddr.py &
```

Cold boot your Pi3. Once Linux boots up, it should display a 'P' to help you orient
your SenseHat display. Then (after about 10 seconds), it will display your IP address

```
10.0.1.8
```

A couple of improvements that could be made to ipaddr.py:

1. Find a better way to get your local IP address other than connecting to an external site
2. Find a way to know when Wi-Fi has completed connecting and is ready for use


## Explore SenseHat

If you haven't already, install sense_hat package for python.

```
pip install sense_hat
```

In the `iot-210B-student/docs` folder you will find 'Essentials_SenseHAT_v1.pdf`

Open that file and try out the examples in your RPI3. 

Make a Python Program that does something interesting. Show your instructor (or cat
if working remotely)

## Lab Links

[PART A](https://gitlab.com/Gislason/iot-210B-student/tree/master/Lab1/LabPartA.md) Setup  
[PART B](https://gitlab.com/Gislason/iot-210B-student/tree/master/Lab1/LabPartB.md) RPi3 SenseHat and Autoboot  
[PART C](https://gitlab.com/Gislason/iot-210B-student/tree/master/Lab1/LabPartC.md) Sockets  
[Homework](https://gitlab.com/Gislason/iot-210B-student/tree/master/Lab1/homework.md) Run through all the labs (Parts A, B and C)  

[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)
