#!/bin/bash
# Exit if we encounter an error
set -e
# Set permissions for us to access GPIO and I2C from user space
sudo ./scripts/setPermissions.sh $USER
# Then install servokit
sudo apt-get install python3-pip -y
# for jetson user on python 3.6.x
# if you get a Adafruit-PlatformDetect > 3.19.6
# you need to remove current version before install the working version
# sudo -H pip3 uninstall Adafruit-PlatformDetect
# sudo -H pip3 uninstall Adafruit_CircuitPython_BusDevice
sudo -H pip3 install adafruit-circuitpython-servokit
sudo -H pip3 install Adafruit-PlatformDetect==3.19.6
sudo -H pip3 install Adafruit_CircuitPython_BusDevice==5.1.5
# for NameError: name 'I2C' is not defined
sudo -H pip3 install adafruit-circuitpython-typing

echo ""
echo "Adafruit CircuitPython ServoKit installed."
echo "Please logoff/logon or reboot in order for I2C permissions to take effect."
echo ""


