#!/bin/bash
# Exit if we encounter an error
# Install the Approxeng.input library
set -e
sudo -H pip3 install approxeng.input
# For the Sony PS4, the joysticks are mapped incorrectly
# Need to copy dualshock4.py to /usr/local/lib/python3.6/dist-packages/approxeng/input/dualshock4.py
sudo cp ./scripts/dualshock4.py /usr/local/lib/python3.6/dist-packages/approxeng/input/dualshock4.py
echo ""
echo "Gamepad support installed."
echo ""

