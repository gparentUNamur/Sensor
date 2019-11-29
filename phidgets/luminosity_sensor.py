from Phidget22.Devices.VoltageRatioInput import VoltageRatioInput


class LuminositySensor:
    voltageRatio = VoltageRatioInput()

    def __init__(self, channel):
        self.channel = channel
        self.voltageRatio.setChannel(channel)

    def get_luminosity(self):
        return self.voltageRatio.getVoltageRatio() * 200
