import serial
import time

ser = serial.Serial('COM4', 9600, timeout = 0)

class Weighing_Scale:

    def __init__(self):
        self.port = ser.port
        self.baudrate = ser.baudrate
        self.timeout = ser.timeout

    def read_weight(self, duration, interval):
        start_time = time.time()
        weight = []

        while (time.time() - start_time) < duration:
            ser.write(b'R')
            time.sleep(0.1)
            weight.append(float(ser.readline()[:10]))
            time.sleep(interval)
        
        return weight
        
    def zero(self):
        ser.write(b'Z')
    
    def tare(self):
        ser.write(b'T')

    def cancel_tare(self):
        ser.write(b'C')

ser1 = Weighing_Scale()

mass = ser1.read_weight(1,1)
print(mass)
