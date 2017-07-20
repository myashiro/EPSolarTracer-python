class Register(object):
    """
    Defines a register
    """
    def __init__(self, address, description, unit, times):
        """
        Constructor
        :param address: Address of the register
        :param description: Description given in the documentation
        :param unit: Unit the returned value is in
        :param times: Multiplication factor
        """
        self.times = times
        self.unit = unit
        self.description = description
        self.address = address


class Coil(object):
    """
    Defines a coil
    """
    def __init__(self, address, description):
        """
        Constructor
        :param address: Address of the coil
        :param description: Description given in the documentation
        """
        self.address = address
        self.description = description


# region registers
class RatedDatum(object):
    ArrayRatedVoltage = Register(0x3000, "PV array rated voltage", "V", 100)


class RealtimeDatum(object):
    pass


class RealtimeStatus(object):
    pass


class StatisticalParameters(object):
    pass


class SettingParameters(object):
    pass


# endregion
# region coils
class SwitchValues(object):
    ChargingDeviceOnOff = Coil(0, "1 Charging device on\n"
                                  "0 Charging device off")


class DescreteValues(object):
    pass

# endregion
