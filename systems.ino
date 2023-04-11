#include <Servo.h>

int HEADER = 0xAB;
int FOOTER = 0xB3;

Servo frontLeft;
Servo frontRight;
Servo backLeft;
Servo backRight;
Servo sideLeft;
Servo sideRight;

struct Input{
  uint8_t command;
  uint16_t value;
};

Input inputValue;
int packetIndex;

void processCommand(){
  switch(inputValue.command){
    case 0x10:
      frontLeft.writeMicroseconds(inputValue.value);
      Serial.print("FL: ");
    break;
    case 0x12:
      frontRight.writeMicroseconds(inputValue.value);
      Serial.print("FR: ");
    break;
    case 0x14:
      backLeft.writeMicroseconds(inputValue.value);
      Serial.print("BL: ");
    break;
    case 0x16:
      backRight.writeMicroseconds(inputValue.value);
      Serial.print("BR: ");
    break;
    case 0x18:
      sideLeft.writeMicroseconds(inputValue.value);
      Serial.print("SL: ");
    break;
    case 0x20:
      sideRight.writeMicroseconds(inputValue.value);
      Serial.print("SR: ");
    break;
  }

  Serial.println(inputValue.value);
}

void readInput(){
  if (Serial.available() > 0){
    int input = Serial.read();
    
    if (packetIndex <= 0){
      if (input != HEADER){
        packetIndex--;
      }
    }
    else if (packetIndex == 1){
      inputValue.command = input;
    }
    else if (packetIndex == 2){
      inputValue.value = input * 256;
    }
    else if (packetIndex == 3){
      inputValue.value += input;
    }
    if (packetIndex >= 4){
      if (input == FOOTER){
        processCommand();
      }
      packetIndex = -1;
    }
    packetIndex++;
  }
}

void resetReadInput(){
  packetIndex = 0;
  inputValue.value = 0;
}


void setup(){
  Serial.begin(9600);

  frontLeft.attach(7);
  frontRight.attach(8);
  backLeft.attach(9);
  backRight.attach(10);
  sideLeft.attach(11);
  sideRight.attach(12);
  
  resetReadInput();

  Serial.println("Ready...");
}


void loop(){
  readInput();
}