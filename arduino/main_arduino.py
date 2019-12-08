from arduino.arduino_request import TemperaturePollutionSensor
from helpers.task_thread import TaskThread


class MainArduinoReader(TaskThread):
    def __init__(self, interval, temp_poll_sensor: TemperaturePollutionSensor):
        super().__init__(interval=interval)
        self.temp_poll_sensor = temp_poll_sensor

    def task(self):
        super().task()
        print(self.temp_poll_sensor.arduino_serial.request_temperature())
