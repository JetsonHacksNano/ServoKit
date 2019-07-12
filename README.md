# ServoKit
Install the Adafruit ServoKit Circuit Python library on the NVIDIA Jetson Nano Developer Kit

Here are some convenience scripts to get servo motors working with the NVIDIA Jetson Nano Developer Kit using a PCA9685 breakout board over I2C.

<h3>installServoKit.sh</h3>
installServoKit.sh first sets the permissions for i2c and gpio so that they can be accessed in user space by the current user. Next, pip is installed. Finally, the adafruit-circuitpython-servokit library (along with its supporting libaries) are installed. To run the script:<br>

<blockquote>$ ./installServoKit.sh</blockquote>

<h3>installGamePad.sh</h3>
Installs the approxeng.input gamepad input library using pip. This provides support for a variety of gamepad controllers. In particular, the Sony Dual Shock PS4 game controller. The script also installs a fix to the dual shock controller for the mapping of the right joystick.<br>

<blockquote>$ ./installGamePad.sh</blockquote>

<h3>servoPlay.py</h3>
A simple example of controlling two servos with a game controller. For testing, two servos are connected to an Adafruit PCA9685 breakout board in positions 0 and 1. For testing, a Sony PS4 game controller was used.<br>

<blockquote>$ python3 servoPlay.py</blockquote>

For the servo attached to port 0, the left gamepad joystick X direction controls the position of the servo. For the other servo, the right joystick in the Y direction controls the position.

<h4>Wiring</h4>
On the Jetson Nano, pins 27 (SDA) and 28 (SCL) on the J41 GPIO header are connected to I2C Bus 0. Pins 3 (SDA) and 4 (SCL) are connected to I2C Bus 1. The demo servoPlay.py uses pins 27 and 28.

Here's the wiring diagram:

![Wiring Diagram](images/NanoI2CWiringDiagram.jpg)

<h2>Releases</h2>
Current Work in Progress
