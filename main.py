from time import sleep

from arduino.arduino_reading import SerialReader
from arduino.arduino_request import TemperaturePollutionSensor
from arduino.main_arduino import MainArduinoReader

ser = SerialReader("/dev/ttyACM0")


# print("Hello, world!")


def main():
    sleep(10)
    temp = TemperaturePollutionSensor("CASINO", "/dev/ttyACM0", "localhost")
    print(temp.arduino_serial.request_temperature())
    main_arduino_reader = MainArduinoReader(60.0, temp)
    main_arduino_reader.run()


main()
