# -Hongseong Technology Center 
**PROJECT : STARWBERRY MONITORING SYSTEM**

# -Read Me
**Raspberry Pi ID Map**
- Raspberry 5 : SB01 , 1234
- Raspberry 4 IO Board : SB02 , 1234

**Raspberry 5 Wifi info**
- 2.4ghz : Smartfarm , hong4321
- 5.0Ghz : Smartfarm 5G , hong4321
- SSH : Dongyang IP: 192.168.0.61 / Hongseong IP: ***.***.***.** port *****
- VNC : Dongyang IP: 192.168.0.61 / Hongseong IP: ***.***.***.** port *****
- DDNS :
- NAS :***.***.***.** port ***** VPN 10.8.0.1

**Raspberry 4 Compute Module Wifi info**
- 2.4ghz : Smartfarm , hong4321
- 5.0Ghz : Smartfarm 5G , hong4321
- SSH : Dongyang IP: 192.168.0.86 / Hongseong IP: ***.***.***.** port *****
- VNC : Dongyang IP: 192.168.0.86 / Hongseong IP: ***.***.***.** port *****
- DDNS :
- NAS : ***.***.***.** port ***** VPN 10.8.0.1

# System info 
**Axis**
- Y , Z 
- Y Length : 8m
- Z Length : 1m


# CODE

**VPN**
- INFO: OpenVPN , IP x,x,x,x , Port xxxxx
**VPN Setup**
- sudo apt-get install openvpn
- sudo apt upgrade
- pip install smbprotocol
- sudo openvpn --config /home/SB01/VPNConfig.ovpn (install : Window CMD -> pscp -P 58001 C:\Users\LEEHONGJU\Downloads\open\VPNConfig.ovpn SB01@라즈베리파이_IP:/home/SB01/ *Start the pscp.exe (PuTTy))
- sudo openvpn --config /home/SB01/VPNConfig.ovpn --daemon
- sudo mount -t cifs -o username=SB01,password=********\*,uid=pi,gid=pi //10.8.0.1/homes/SB01 /home/SB01/Photo
  Mount Complete

**Camera (Rasp 5)**
 - INFO: Camera IMX296 , GS camera x2
 - Readme: https://www.raspberrypi.com/documentation/computers/compute-module.html#attaching-a-raspberry-pi-camera-module
 - sudo nano /boot/firmware/config.txt: ALL [dtoverlay=imx296,cam0 dtoverlay=imx296,cam1]
 - sudo apt install libcamera-apps
 - 
**Camera (Rasp 4)**
 - INFO: Camera IMX296 , GS camera x2
 - Readme: https://www.raspberrypi.com/documentation/computers/compute-module.html#attaching-a-raspberry-pi-camera-module
 - sudo nano /boot/firmware/config.txt: ALL [dtoverlay=imx296,cam0 dtoverlay=imx296,cam1]
 - sudo raspi-config : Interfacing Options -> P1 Camera -> Enable
 - sudo apt install libcamera-apps

**VPN Config**
 - conf file Address : /etc/openvpn/client/VPNConfig.conf
 - Service file Address : /lib/systmed/system/openvpn-client@.service
 - ovpn flie Address : /etc/openvpn/client/VPNConfig.ovpn

