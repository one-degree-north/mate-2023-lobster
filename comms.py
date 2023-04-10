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

        # self.thrusters = {
        #     "FL": b'\x10',
        #     "FR": b'\x12',
        #     "BL": b'\x14',
        #     "BR": b'\x16',
        #     "SL": b'\x18',
        #     "SR": b'\x20'
        # }

        self.THRUSTERS = (
            b'\x10',
            b'\x12',
            b'\x14',
            b'\x16',
            b'\x18',
            b'\x20'
        ) # fl, fr, bl, br, sl, sr

        self.speed = 100 # speed - [100, 500]

    def up(self):
        self.__write_thruster(0)
        self.__write_thruster(1)
        self.__write_thruster(2)
        self.__write_thruster(3)

    def down(self):
        self.__write_thruster(0, rev=True)
        self.__write_thruster(1, rev=True)
        self.__write_thruster(2, rev=True)
        self.__write_thruster(3, rev=True)

    def forward(self):
        self.__write_thruster(4)
        self.__write_thruster(5)

    def backward(self):
        self.__write_thruster(4, rev=True)
        self.__write_thruster(5, rev=True)

    def roll_left(self):
        self.__write_thruster(0, rev=True)
        self.__write_thruster(1)
        self.__write_thruster(2, rev=True)
        self.__write_thruster(3)

    def roll_right(self):
        self.__write_thruster(0)
        self.__write_thruster(1, rev=True)
        self.__write_thruster(2)
        self.__write_thruster(3, rev=True)

    def pitch_up(self):
        self.__write_thruster(0)
        self.__write_thruster(1)
        self.__write_thruster(2, rev=True)
        self.__write_thruster(3, rev=True)

    def pitch_down(self):
        self.__write_thruster(0, rev=True)
        self.__write_thruster(1, rev=True)
        self.__write_thruster(2)
        self.__write_thruster(3)

    def yaw_left(self):
        self.__write_thruster(4, rev=True)
        self.__write_thruster(5)

    def yaw_right(self):
        self.__write_thruster(4)
        self.__write_thruster(5, rev=True)

    def set_speed(self, mode: int): # mode: 1, 2, 3, 4, 5 = 100, 200, 300, 400, 500
        self.speed = mode * 100

    def stop_thrusters(self, vertical: bool = False, side: bool = False):
        if vertical:
            thrusters = list(range(4))
        elif side:
            thrusters = list(range(4, 6))
        else:
            thrusters = list(range(6))

        for ti in thrusters:
            self.__write_thruster(ti, 1500)

    def __write_thruster(self, index: int, speed: int = None, rev: bool = False):
        self.serial.write(self.HEADER)

        if not speed:
            if rev:
                speed = 1500 - self.speed
            else:
                speed = 1500 + self.speed            

        self.serial.write(struct.pack(">cH", self.THRUSTERS[index], speed))
        self.serial.write(self.FOOTER)

if __name__ == "__main__":
    comms = Comms("/dev/cu.usbmodem112301", 9600)
    
    while True:
        thruster, speed = input("Thruster (ex: FL 1600): ").split()

        comms.stop_all()