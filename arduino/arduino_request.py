import requests

from arduino.arduino_reading import SerialReader


class TemperaturePollutionSensor:
    """
    localisation : Place where is the sensor
    path : Path for the Arduino Serial port (typically /dev/ttyACM0)
    url: base url for requesting web Server
    """
    def __init__(self, localisation: str, path: str, url: str):
        self.localisation = localisation
        self.arduino_serial = SerialReader(path)
        self.url = url

    def request_temperature(self):
        temp = self.arduino_serial.request_temperature()
        data = {"temp": temp, "loc": self.localisation}
        r = requests.get(self.url, data)

    def request_co2(self):
        co2 = self.arduino_serial.request_co2e()
        data = {"co2": co2, "loc": self.localisation}
        r = requests.get(self.url, data)
