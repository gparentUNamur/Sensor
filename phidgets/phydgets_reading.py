import requests

from phidgets.luminosity_sensor import LuminositySensor
from phidgets.temperature_sensor import TemperatureSensor


class Sender:

    def __init__(self, luminosity_sensor: LuminositySensor, temperature_sensor: TemperatureSensor):
        self.temperature_sensor = temperature_sensor
        self.luminosity_sensor = luminosity_sensor

    def request_to(self):
        temp = self.temperature_sensor.get_temperature()
        lumen = self.luminosity_sensor.get_luminosity()
        data = {"lum": lumen, "temp": temp}
        r = requests.get("http://apollo:9000/", data)
