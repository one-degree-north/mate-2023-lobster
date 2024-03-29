import serial
import struct

class Comms:
    def __init__(self, port, baud):
        self.serial = serial.Serial(port=port, baudrate=baud)
        
        self.HEADER = b'\xab'
        self.FOOTER = b'\xb3'

        self.THRUSTERS = (
            b'\x16', 
            b'\x20',
            b'\x14',
            b'\x12',
            b'\x18',
            b'\x10',
        ) # fl, fr , bl, br, sl, sr ------ bry top to bottom

        self.speed = 200

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
        # while True:
        #     self.stop_thrusters()
        #     self.__write_thruster(int(input("t: ")), 2000)
        #     input()

    def backward(self):
        self.__write_thruster(4, rev=True)
        self.__write_thruster(5, rev=True)

    def roll_left(self):
        self.__write_thruster(0)
        self.__write_thruster(1, rev=True)
        self.__write_thruster(2)
        self.__write_thruster(3, rev=True)

    def roll_right(self):
        self.__write_thruster(0, rev=True)
        self.__write_thruster(1)
        self.__write_thruster(2, rev=True)
        self.__write_thruster(3)

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

        for v in thrusters:
            self.__write_thruster(v, 1500)
 
    def __write_thruster(self, index: int, speed: int = None, rev: bool = False):
        self.serial.write(self.HEADER)

        if not speed:
            if index in list(range(5)):
                rev = not rev

            if index == 1:
                rev = not rev

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