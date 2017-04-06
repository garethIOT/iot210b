[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)

# Lab1 - PartC (Sockets)

In this section of the lab you will

* Learn the difference between TCP/IP and UDP/IP
* Learn how to use sockets from both a Client and Server Perspective

These apps can be run from the Raspberry Pi in terminal windows, or on your PC

## UDP

From `iot-210B-student/Lab1/src` 

In one terminal window, run:  
```
$ python ipv4_udp_server.py
```

The server will sit and wait for incoming packets

In another terminal window, run:  
```
$ python ipv4_udp_client.py
```

Experiment with different IP ports and messages. You can even send a message to someone else's
PI.

```
$ python ipv4_udp_client.py message ip_addr port
```

Ports can be anything from 1024 - 65000. Ports < 1024 are reserved for various services.


## TCP

From `iot-210B-student/Lab1/src` 

In one terminal window, run:  
```
$ python ipv4_tcp_server.py
```

The server will sit and wait for an incoming connection

In another terminal window, run:  
```
$ python ipv4_tcp_client.py
```

Experiment with different IP ports and messages. You can even send a message to someone else's
PI.

```
$ python ipv4_tcp_client.py message ip_addr port
```

Ports can be anything from 1024 - 65000. Ports < 1024 are reserved for various services.

## Lab Links

[PART A](https://gitlab.com/Gislason/iot-210B-student/tree/master/Lab1/LabPartA.md) Setup  
[PART B](https://gitlab.com/Gislason/iot-210B-student/tree/master/Lab1/LabPartB.md) RPi3 SenseHat and Autoboot  
[PART C](https://gitlab.com/Gislason/iot-210B-student/tree/master/Lab1/LabPartC.md) Sockets  
[Homework](https://gitlab.com/Gislason/iot-210B-student/tree/master/Lab1/homework.md) Run through all the labs (Parts A, B and C)  

[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)
