from Phidget22.Devices.VoltageRatioInput import *


def on_sensor_change(self, sensor_value, sensor_unit):
    print("SensorValue: " + str(sensor_value))
    print("SensorUnit: " + str(sensor_unit.symbol))
    print("----------")


def on_voltage_change(self, voltage):
    print("Voltage: " + str(voltage))
    print("Lumen : " + str(voltage * 200))


def main():
    voltage_ratio_input4 = VoltageRatioInput()
    voltage_ratio_input1 = VoltageRatioInput()
    voltage_ratio_input4.setChannel(0)
    voltage_ratio_input1.setChannel(1)

    # voltage_ratio_input4.setOnSensorChangeHandler(onSensorChange)
    # voltage_ratio_input1.setOnVoltageRatioChangeHandler(onVoltageChange)
    voltage_ratio_input4.openWaitForAttachment(5000)
    voltage_ratio_input1.openWaitForAttachment(5000)

    voltage_ratio_input4.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1124)

    try:
        request = input("Press Enter to Stop\n")
        if request == "T":
            print(voltage_ratio_input4.getSensorValue())
        elif request == "L":
            print(voltage_ratio_input1.getVoltageRatio()*200)
    except (Exception, KeyboardInterrupt):
        pass

    voltage_ratio_input4.close()


main()
