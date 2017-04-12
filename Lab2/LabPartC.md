[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)

Lab2 Part B - IPv6 vs IPv4

# Use ifconfig to find out your 

```
$pi ifconfig | grep inet

  inet 127.0.0.1 netmask 0xff000000 
  inet6 ::1 prefixlen 128 
  inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1 
  inet6 fe80::494:eaba:18ea:2955%en0 prefixlen 64 secured scopeid 0x4 
  inet 172.27.40.103 netmask 0xffffff00 broadcast 172.27.40.255
  inet6 fc00:1::c38:b3d9:1366:80a2 prefixlen 64 autoconf secured 
  inet6 fc00:1::75b2:dd8:f250:2de9 prefixlen 64 autoconf temporary 
  inet6 fc00:1::d932 prefixlen 64 dynamic 
  inet6 fe80::3072:afff:febc:95b1%awdl0 prefixlen 64 scopeid 0x8 
  inet6 fe80::68e4:5bb7:4b84:cd5f%utun0 prefixlen 64 scopeid 0xa 
  inet6 fe80::5b8e:9097:223c:7003%utun1 prefixlen 64 scopeid 0xb 
```

# Printing Routes

  Windows: route print

  MAC / Linux: netstat -nr


# IPv6 client and server

This lab is very simple. Take a look at the ipv6client.py and ipv6server.py

In a terminal window, run

```
$pi cd ~/Documents/Git/iot-210B-student/Lab2/src
$pi python ipv6server.py
```

In another terminal window, run

```
$pi cd ~/Documents/Git/iot-210B-student/Lab2/src
$pi python ipv6client.py
```

# Experiments

Try sending data to another server in the same classroom (on the same subnet).

Try sending data to another server across the internet (elsewhere)

[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)
