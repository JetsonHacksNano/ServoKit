#!/bin/bash
usermod -aG i2c $USER
groupadd -f -r gpio
usermod -a -G gpio $USER
cp /opt/nvidia/jetson-gpio/etc/99-gpio.rules /etc/udev/rules.d/
udevadm control --reload-rules && sudo udevadm trigger

