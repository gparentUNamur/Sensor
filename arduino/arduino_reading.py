from serial import Serial


class SerialReader:
    class __SerialReader:
        def __init__(self, path: str):
            self.path = path
            self.serial = Serial(path, 9600)

        def __str__(self):
            return repr(self) + self.path

        def get_temperature(self):
            self.serial.write('T'.encode())
            return float(self.serial.readline())

        def get_co2e(self):
            self.serial.write('C'.encode())
            return int(self.serial.readline())

    instance: __SerialReader = None

    def __init__(self, path: str):
        if not SerialReader.instance:
            SerialReader.instance = SerialReader.__SerialReader(path)
        else:
            SerialReader.instance.path = path

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def request_temperature(self) -> float:
        return self.instance.get_temperature()

    def request_co2e(self) -> int:
        return self.instance.get_co2e()
