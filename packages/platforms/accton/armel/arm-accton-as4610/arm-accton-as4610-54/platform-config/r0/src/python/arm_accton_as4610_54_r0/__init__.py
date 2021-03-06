from onl.platform.base import *
from onl.platform.accton import *

class OnlPlatform_arm_accton_as4610_54_r0(OnlPlatformAccton,
                                          OnlPlatformPortConfig_48x1_4x10):
    PLATFORM='arm-accton-as4610-54-r0'
    MODEL="AS4610-54"
    SYS_OBJECT_ID=".4610.54"

    def baseconfig(self):
        self.insmod("accton_i2c_cpld")
        self.new_i2c_device("as4610_54_cpld", 0x30, 0)
        self.insmod("accton_as4610_sfp")
        self.insmod("accton_as4610_psu")
        self.insmod("accton_as4610_fan")
        self.insmod("accton_as4610_leds")
        self.insmod("ym2651y")
#        self.new_i2c_devices(
#            [
#                ("pca9548",        0x70, 1),
#                ("as4610_sfp1",    0x50, 2),
#                ("as4610_sfp2",    0x50, 3),
#                ("as4610_sfp3",    0x50, 4),
#                ("as4610_sfp4",    0x50, 5),
#                ("as4610_sfp5",    0x50, 6),
#                ("as4610_sfp6",    0x50, 7),
#                ("as4610_psu1",    0x50, 8),
#                ("as4610_psu2",    0x51, 8),
#                ("ym1921",         0x58, 8),
#                ("ym1921",         0x59, 8),
#                ("lm77",           0x48, 9),
#                ("ds1307",         0x68, 9),
#                ("24c04",          0x50, 9),
#            ]
#        )
        return True
