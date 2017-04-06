[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)

## Setting up RPi3 for the IoT 110,210,320 Classes

### Summary of Setup Steps
* [OPT] Download OS from RaspberryPi Foundation
* ( 1) Set Hardcoded Screen Resolution for mini HDMI monitor
* ( 2) Expand the filesystem
* ( 3) Setup WiFi connection
* ( 4) Establish a Command Line Interface (CLI)
* ( 5) Ensure a US Keyboard mapping
* ( 6) Set up a hostname unique for your PI (using its last 4 digits MAC address for wlan)
* ( 7) Enable Serial Ports and GPIO for Labs
* ( 8) Set up local hostname resolution for the IOT class (or home) network
* ( 9) SSH -> iot1234
* (10) Mapping PI filesystem into host's
* (11) Update OS and install a few utilities and check versions

<hr>
### [OPTIONAL] Downloading and burning a new image (if you wish to have the latest OS or burn your own image)
[RASPBIAN JESSIE WITH PIXEL](https://www.raspberrypi.org/downloads/raspbian/)
Image with PIXEL desktop based on Debian Jessie

[RASPBIAN JESSIE LITE](https://www.raspberrypi.org/downloads/raspbian/)
Minimal image based on Debian Jessie

[Optional Configuration Link](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-2-first-time-configuration/using-the-whole-sd-card?view=all)
<hr>
### STEP 1: Mini Display 480x800 pixels

**Skip this step if using a desktop HDMI display (as opposed to the the one used in Class IoT 110A.**

This display will not boot a screen on default.  The config.txt file must be
modified according to the instructions on Adafruit.  (config.txt is located on the SD card and you must insert the card into your host computer to edit)
[Display Config Changes](https://learn.adafruit.com/adafruit-5-800x480-tft-hdmi-monitor-touchscreen-backpack/raspberry-pi-config)
In case that site goes down, here's a summary of the changes in config.txt:
```
# uncomment if hdmi display is not detected and composite is being output
hdmi_force_hotplug=1

# uncomment to force a specific HDMI mode (here we are forcing 800x480!)
hdmi_group=2
hdmi_mode=87
hdmi_cvt=800 480 60 6 0 0 0
```
<hr>
#### [GENERAL INFO] Check the Raspberry PI Settings/Preferences
Start > Preferences > Raspberry Pi Configuration
![Raspberry Pi Settings](https://gitlab.com/Gislason/iot-210B-student/raw/master/images/Preferences.png)

<hr>

### STEP 2: Expanding Filesystem
**Objective:** The default SD card operating systems shipped out of the box
often are not expanded to the full extent of the size of the SD card.  This is
also true if you have downloaded an operating system image (see above) and
burned it onto the card.  The image size may only be 1-2GB but the card might be
8GB to 64GB for example.  We therefore will want to have ALL of the SD card
file system available to the RPi. It is very important to do this at the **VERY
BEGINNING OF SETUP** otherwise you may find yourself out of disk space and in a
"bricked" state.  In this case, you will need to perform the OPTIONAL step above
and start over with a fresh image install.<br><br>
![Expand File System](https://gitlab.com/Gislason/iot-210B-student/raw/master/images/expand.png)

After expanding and rebooting as required, open a terminal and check to ensure
that the filesystem was indeed expanded.<br><br>
![File System Size Check](https://gitlab.com/Gislason/iot-210B-student/raw/master/images/df_dash_h.png)
<br>
<hr>
### STEP 3: Setup WiFi Connection
Apple Airport access points have been configured for our IoT classroom.  There
are 2 access points because they each have a limit of 50 client connections.  
To attempt to keep things simple we will join to only one of the access points
(UW-IoT110-R) until we either have:<br>
a) run out of 50 client connections<br>
  or<br>
b) we have a failure on one access point.<br>

Using the mouse and hovering over the WiFi connection ICON, select SSID and
enter the password given below:<br>
Airports have SSIDs of UW-IoT110-R (primary) and UW-IoT110-L (secondary).  
Password: **piIoT110**  (Note: "I" in IoT is  "capital I" and not "capital L")
<br><br>
![WiFi Settings Panel](https://gitlab.com/Gislason/iot-210B-student/raw/master/images/SSID.png)
<br>
<hr>
### STEP 4: Command line shell ###
For MacOSX or Linux users, just use the normal "terminal" for your Command Line
Interface (CLI).<br>

For Windows users, it maybe best to download the GIT Bash tool (git is built
into Linux and MacOSX terminal shells).
[Download GIT](https://git-scm.com/downloads)

NOTE: For the following command line entries we use the following to
indicate which machine you are on.
```
pi$  => this is a command on the RPi3

host$ => this is a command on your development host (Windows PC or MAC)
```

#### Check to see if connected to the public Internet
```
pi$ ping google.com
```

#### Determine IP address of RPi
```
pi$ ifconfig | grep "inet addr"
=> inet addr:192.168.10.19  Bcast:192.168.1.255  Mask:255.255.255.0
```


### Step 5: Ensure a US Keyboard Mapping
![Keyboard Setting](https://gitlab.com/Gislason/iot-210B-student/raw/master/images/Keyboard.png)


### Step 6: Setup a unique hostname based on wlan MAC
```
pi$ ifconfig | grep wlan0  
=> wlan0     Link encap:Ethernet  HWaddr b8:27:eb:e9:12:34  
=> choose the last 4 digits of the MAC => [1234]

pi$ sudo vi /etc/hostname

=> remove current hostname and replace with "iot1234"
=> using the [HWaddr] from above network queries
```
Alternatively the hostname can be set from the Preferences panel.
![Hostname Preferences UI](https://gitlab.com/Gislason/iot-210B-student/raw/master/images/hostname.png)

### Step 7: Enable I2C Serial Port (and GPIO if Pixel OS) for Labs
![Raspberry Pi I/O Port Settings](https://gitlab.com/Gislason/iot-210B-student/raw/master/images/interfaces.png)

#### Reboot
```
pi$ reboot
```

<hr>
### STEP 8: Using Hostname Resolution on Network
```
// start the avahi-daemon network service
pi$ systemctl status avahi-daemon
  => Verify that the hostname matches the name changed to above
Loaded: loaded (/lib/systemd/system/avahi-daemon.service; enabled)
Active: active (running) since Sun 2016-11-13 23:15:20 UTC; 15min ago
Main PID: 438 (avahi-daemon)
  Status: "avahi-daemon 0.6.31 starting up."
  CGroup: /system.slice/avahi-daemon.service
          ├─438 avahi-daemon: running [iot1234.local]
          └─465 avahi-daemon: chroot helper

host$ ping iot1234
PING iot1234.home (192.168.10.19): 56 data bytes
64 bytes from 192.168.10.19: icmp_seq=0 ttl=64 time=10.863 ms
64 bytes from 192.168.10.19: icmp_seq=1 ttl=64 time=7.657 ms
64 bytes from 192.168.10.19: icmp_seq=2 ttl=64 time=7.024 ms      

```
<hr>
### STEP 9: Setting up SSH
**Objective:** Establishing ssh connection is the most universal way to connect
two computers together over a network (local or global).  This also automatically
provides public key infrastructure (PKI) security which is the standard for
Internet Security.  Establishing SSH keys allows for password free log in
between systems which is not only convenient (when a trust is established) but
essential when automating connectivity --as we will be doing for our class.  We
will be using SSH to routinely log into our machines as well as utilizing a
capbility known as SSHFS (i.e. File System mapping over SSH).

```
// ------- RPi KEY SETUP ----------
// log into RPi iot1234 (with password => "raspberry")
host$ ssh pi@iot1234  // answer yes to the one time prompt for host signature
                            // passwd default: "raspberry"
pi$ cd .ssh                 // change dir to .ssh if it exists, mkdir if it doesn't
pi$ ssh-keygen              // generate an ssh key (RSA)
=> Enter file in which to save the key (/home/pi/.ssh/id_rsa):
                            // hit <enter> 3 times

pi$ cp id_rsa.pub  id_rsa_iot1234.pub
pi$ exit                    // success! now exit and set up an SSH key for host
```

**(IF YOU ALREADY HAVE AN SSH HOST KEY PLEASE SKIP THE HOST PORTION)**

```
// ------- HOST KEY SETUP ----------
// generatate (or use) a ssh key on the host (IF YOU ALREADY HAVE A KEY
host$ cd ~/.ssh
host$ ssh-keygen            
=> Enter file in which to save the key (/home/pi/.ssh/id_rsa):
                            // hit <enter> 3 times

host$ cp id_rsa.pub id_rsa_XYZ.pub  // Use a unique XYZ id from your host machine
host$ scp id_rsa_XYZ.pub pi@iot1234:.ssh
host$ ssh pi@iot1234                // enter passwd (for the last time!)

// install the ssh host key on iot708c
pi$ cd .ssh
pi$ cat id_rsa_XYZ.pub >> authorized_keys
pi$ exit  

// test the ssh key
host$ ssh pi@iot1234  // should be passwd free now!
pi$ exit  
```
<hr>
### STEP 10: Mapping PI filesystem into host's
**Objective:** It is *very convenient* to map the RPi's filesystem into your
development host as if it is just another folder on your host.  This allows the
use of native and powerful code friendly editors (e.g. Atom or Sublime) in which
to edit source code.  Because the RPi's file system is mapped there is no need
to transfer code back and forth to the RPi.  In Linux-speak mapping a target
filesystem like this is known as *mounting the file system*.

Create a folder on the RPi under ```Documents/``` called ```GIT_REPOS``` 
(e.g. Documents/GIT_REPOS)

Must install sshfs capability in order to mount file system then...
#### sshfs for MacOSX
[FUSE for macOS](https://osxfuse.github.io/)   // install **BOTH** fuse and sshfs pkgs

Create directories on development host to mount each PI (e.g. PI_MOUNT_1234)
then mount them using sshfs.

``` sh
host$ sshfs pi@iot1234:Documents/GIT_REPOS PI_MOUNT_1234/ -C

```

disconnect from the PI file systems
```
host$ umount PI_MOUNT_1234/
```

#### sshfs for Windows 7/8/10
[SSHFS Win10](https://igikorn.com/sshfs-windows-10/)   // install Win sshfs pkg

Follow the instructions to set up a GUI based SSHFS capability for Windows
development hosts.

<hr>
### STEP 11: Update OS and install a few utilities and check versions
**Objective:** It is always a good idea to keep Linux systems such as the
Debian OS (Raspbian) updated with the latest improvements coming from the large
open source community such as enjoyed by the Raspberry Pi platform.  As a final
stage of our PI setup we will make sure we have an updated OS.

``` bash
host$ ssh pi@iot1234

pi$ sudo apt install rpi-update
pi$ sudo rpi-update
pi$ uname -a

```

[IOT STUDENT HOME](https://gitlab.com/Gislason/iot-210B-student/blob/master/README.md)
