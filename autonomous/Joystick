from threading import Thread
import serial
import controls
import gui
import struct

maxCoordinates = 100

class Comms:
    def __init__(self, port: str, baud_rate: int):
        self.port = port
        self.baud_rate = baud_rate
        ser = serial.Serial(self.port, self,baud_rate)
        self.ser.close()
        self.ser.open()

    def send_value(self,value):
        #preq: -100<=value<=100
        self.value = round(value*1.27)
        if self.value<0:
            self.value = 255+self.value
        return self.value 

    def run(self):
        while True: 
            self.packetControls = self.packetControls.Controls() #modify later
            #leftJoy_LR = packetControls.packet[0] #will finalize once I know what values will come
            self.leftJoy_UD = self.packetControl.packet[1]
            self.rightJoy_LR = self.packetControls.packet[2]
            #rightJoy_UD = packetControls.packet[3]
            self.servoRotate = self.packetControls.packet[4]
            self.servoGrab = self.packetControls.packet[5]
            self.LB_up = self.packetControls.packets[6]
            self.RB_down = self.packetControls.packet[7]

            #coordinate => [x,y]
            if (self.leftJoy_UD[1] > 0.5*maxCoordinates):
                #joystick has been moved up; tell both thrusters to move forward 
                self.value = self.send_self.value(self.leftJoy_UD)
                packet_rightThruster = chr(1) + chr(6) + chr((self.value).encode("latin")) + chr(255)
                self.ser.write(packet_rightThruster)
                packet_leftThruster = chr(1) + chr(7) + chr((self.value).encode("latin")) + chr(255)
                self.ser.write(packet_leftThruster)
            elif (self.leftJoy_UD[1] < 0.5*maxCoordinates):
                    self.value = self.send_value(self.leftJoy_UD)
                    packet_rightThrus = chr(1) + chr(6) + chr((self.value).encode("latin")) + chr(255) 
                    self.ser.write(packet_rightThrus)
                    packet_leftThurs = chr(1) + chr(7) + chr((self.value).encode("latin")) + chr(255) 
                    self.ser.write(packet_leftThurs)
            #have to specify to elimate packets being sent when joystick is at (0,0)

            #coding left and right movement
            if (self.rightJoy_LR[0] > 0.5*maxCoordinates):
                #joystick has been moved to the right
                self.value = self.send_value(self.leftJoy_UD)
                packet_rightThruster = chr(1) + chr(6) + chr((self.value).encode("latin")) + chr(255)
                self.ser.write(packet_rightThruster)
                packet_leftThruster = chr(1) + chr(7) + chr((self.value).encode("latin")) + chr(255)
                self.ser.write(packet_leftThruster)
            elif (self.rightJoy_LR[0] < 0.5*maxCoordinates):
                #joystick has been moved to the left
                self.value = self.send_value(self.leftJoy_UD)
                packet_rightThruster = chr(1) + chr(6) + chr((self.value).encode("latin")) + chr(255)
                self.ser.write(packet_rightThruster)
                packet_leftThruster = chr(1) + chr(7) + chr((self.value).encode("latin")) + chr(255)
                self.ser.write(packet_leftThruster)

            '''
            #previous code (reviewed and accepted - IGNORE)
            while True:
                #coding the thrusters forward and back (sendSystemsLes)
                if leftJoy_UD < [43,43]:
                    value = self.send_value(leftJoy_UD)
                    packet_leftJoy_stopped = chr(1) + chr(7) + chr((self.value).encode("latin")) + chr(255)
                    self.ser.write(packet_leftJoy_stopped)
                else:
                    value = self.send_value(leftJoy_LR)
                    packet_leftJoy = chr(1) + chr(7) + chr((self.value).encode("latin")) + chr(255) 
                    self.ser.write(packet_leftJoy)

                #coding the Right thruster
                if rightJoy_LR < [43,43]:
                    value = self.send_value(rightJoy_LR)
                    packet_rightJoy_stopped = chr(1) + chr(6) + chr((self.value).encode("latin")) + chr(255)
                    self.ser.write(packet_rightJoy_stopped)
                else:
                    packet_rightJoy = chr(1) + chr(6) + chr((self.value).encode("latin")) + chr(255) 
                    self.ser.write(packet_rightJoy) '''

                #servo claw code - finalized with packet value. chr(11) tells systems to switch off the servo and chr(12) is an empty byte
            if (self.servoRotate == True):
                self.value = self.send_value(self.servoRotate)
                packet_servoRotate = chr(1) + chr(8) + chr(12) + chr(255)
                self.ser.write(packet_servoRotate)
            else:
                packet_servoRotate_off = chr(1) + chr(8) + chr(11) + chr(255)
                self.ser.write(packet_servoRotate_off)

            if (self.servoGrab == True):
                self.value = self.send_value(self.servoGrab)
                packet_servoGrab = chr(1) + chr(9) + chr(12) + chr(255)
                self.ser.write(packet_servoGrab)
            else:
                packet_servoGrab_off = chr(1) + chr(9) + chr(11) + chr(255)
                self.ser.write(packet_servoGrab_off)

            #[-127,127]

            #4 up and down motors 
            if (self.LB_up == True):
                packet_LB_up = chr(1) + chr(13) + chr(127) + chr(255)
                self.ser.write(packet_LB_up)
            elif (self.RB_up == True):
                    packet_RB_up = chr(1) + chr(13) + chr(254) + chr(255)
                    self.ser.write(packet_RB_up)
            #systems will read chr(13) and turn all 4 up-down motors up, and the chr(14) will turn them all down.

            #to recieve the gyroscope information from systems
            packet_IMUdata = self.Serial.read(size=4)
            header, self.orien.x, self.orien.y, self.orien.z, self.gyro.x, self.gyro.y, self.gyro.z, self.accel.x, self.accel.y, self.accel.z = struct.unpack('ccfffffffff')                

    def start_thread(self):
        start_thread = self.threading.Thread(target = self.run)  
        start_thread.start()
    
    #display_GUI = gui.GUI()