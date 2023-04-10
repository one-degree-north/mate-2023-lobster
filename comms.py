import serial
from dataclasses import dataclass
import struct

# @dataclass
# class PacketInfo:
#     thruster: int
#     speed: int


class Comms:
    def __init__(self, port, baud):
        self.serial = serial.Serial(port=port, baudrate=baud)
        
        self.HEADER = b'\xab'
        self.FOOTER = b'\xb3'

        self.thrusters = {
            "FL": b'\x10',
            "FR": b'\x12',
            "BL": b'\x14',
            "BR": b'\x16',
            "SL": b'\x18',
            "SR": b'\x20'
        }

    def write(self, thruster: str, speed: int):
        self.serial.write(self.HEADER)
        self.serial.write(struct.pack(">cH", self.thrusters[thruster], speed))
        self.serial.write(self.FOOTER)

if __name__ == "__main__":
    comms = Comms("/dev/cu.usbmodem112301", 9600)
    
    while True:
        thruster, speed = input("Thruster (ex: FL 1600): ").split()

        comms.write(thruster, int(speed))