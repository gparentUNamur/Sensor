from Phidget22.Devices.VoltageRatioInput import VoltageRatioInput
from Phidget22.VoltageRatioSensorType import VoltageRatioSensorType


class TemperatureSensor:
    voltageRatioInput = VoltageRatioInput()

    def __init__(self, channel):
        self.channel = channel
        self.voltageRatioInput.setChannel(channel)
        self.voltageRatioInput.setSensorType(SensorType=VoltageRatioSensorType.SENSOR_TYPE_1124)

    def get_temperature(self):
        return self.voltageRatioInput.getSensorValue()
