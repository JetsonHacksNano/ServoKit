from colorsys import hsv_to_rgb

from approxeng.input import Controller, Button, CentredAxis, TriggerAxis, BinaryAxis
from approxeng.input.sys import write_led_value, read_power_level

DS4_VENDOR_ID = 1356
DS4_PRODUCT_ID = 2508
DS4V2_PRODUCT_ID = 1476


# Battery status at /sys/class/power_supply/sony_controller_battery_xx:xx:xx:xx:xx:xx/capacity, where xx:xx... is the
# bluetooth MAC of the controller.


class DualShock4(Controller):
    """
    Driver for the Sony PlayStation 4 controller, the DualShock4
    """

    def __init__(self, dead_zone=0.05, hot_zone=0.05):
        """
        Create a new DualShock4 driver

        :param float dead_zone:
            Used to set the dead zone for each :class:`approxeng.input.CentredAxis` in the controller.
        :param float hot_zone:
            Used to set the hot zone for each :class:`approxeng.input.CentredAxis` in the controller.
        """
        super(DualShock4, self).__init__(vendor_id=DS4_VENDOR_ID,
                                         product_id=DS4_PRODUCT_ID,
                                         controls=[
                                             Button("Circle", 305, sname='circle'),
                                             Button("Cross", 304, sname='cross'),
                                             Button("Square", 308, sname='square'),
                                             Button("Triangle", 307, sname='triangle'),
                                             Button("Home (PS)", 316, sname='home'),
                                             Button("Share", 314, sname='select'),
                                             Button("Options", 315, sname='start'),
                                             Button("Trackpad", 'touch272', sname='ps4_pad'),
                                             Button("L1", 310, sname='l1'),
                                             Button("R1", 311, sname='r1'),
                                             Button("L2", 312, sname='l2'),
                                             Button("R2", 313, sname='r2'),
                                             Button("Left Stick", 317, sname='ls'),
                                             Button("Right Stick", 318, sname='rs'),
                                             CentredAxis("Left Horizontal", 0, 255, 0, sname='lx'),
                                             CentredAxis("Left Vertical", 0, 255, 1, invert=True, sname='ly'),
                                             CentredAxis("Right Horizontal", 0, 255, 2, sname='rx'),
                                             CentredAxis("Right Vertical", 0, 255, 5, invert=True, sname='ry'),
                                             TriggerAxis("Left Trigger", 0, 255, 3, sname='lt'),
                                             TriggerAxis("Right Trigger", 0, 255, 4, sname='rt'),
                                             BinaryAxis("D-pad Horizontal", 16, b1name='dleft', b2name='dright'),
                                             BinaryAxis("D-pad Vertical", 17, b1name='dup', b2name='ddown'),
                                             # CentredAxis("Motion 3", -1, 1, 'motion3', sname='zm3'),
                                             CentredAxis("Yaw rate", -2097152, 2097152, 'motion4', sname='yaw_rate',
                                                         invert=True),
                                             # CentredAxis("Motion 5", -1, 1, 'motion5', sname='zm5'),
                                             CentredAxis("Roll", -8500, 8500, 'motion0', sname='roll', invert=True),
                                             # CentredAxis("Motion 1", -1, 1, 'motion1', sname='zm1'),
                                             CentredAxis("Pitch", -8500, 8500, 'motion2', sname='pitch',
                                                         invert=True),
                                             CentredAxis("Touch X", 0, 1920, 'touch53', sname='tx'),
                                             CentredAxis("Touch Y", 0, 942, 'touch54', sname='ty', invert=True)

                                         ],
                                         node_mappings={
                                             'Sony Interactive Entertainment Wireless Controller Touchpad':
                                                 'touch',
                                             'Sony Interactive Entertainment Wireless Controller Motion Sensors':
                                                 'motion',
                                             'Wireless Controller Touchpad': 'touch',
                                             'Wireless Controller Motion Sensors': 'motion'},
                                         dead_zone=dead_zone,
                                         hot_zone=hot_zone)
        self.axes['roll'].hot_zone = 0.2
        self.axes['pitch'].hot_zone = 0.2

    def __repr__(self):
        return 'Sony DualShock4 (Playstation 4) controller'

    def set_leds(self, hue=0.0, saturation=1.0, value=1.0):
        """
        The DualShock4 has an LED bar on the front of the controller. This function allows you to set the value of this
        bar. Note that the controller must be connected for this to work, if it's not the call will just be ignored.

        :param hue:
            The hue of the colour, defaults to 0, specified as a floating point value between 0.0 and 1.0.
        :param saturation:
            Saturation of the colour, defaults to 1.0, specified as a floating point value between 0.0 and 1.0.
        :param value:
            Value of the colour (i.e. how bright the light is overall), defaults to 1.0, specified as a floating point
            value between 0.0 and 1.0
        """
        r, g, b = hsv_to_rgb(hue, saturation, value)
        write_led_value(self.device_unique_name, 'red', r * 255.0)
        write_led_value(self.device_unique_name, 'green', g * 255.0)
        write_led_value(self.device_unique_name, 'blue', b * 255.0)

    @property
    def battery_level(self):
        return float(read_power_level(self.device_unique_name)) / 100.0
