#include <Servo.h>

int HEADER = 0xAB;
int FOOTER = 0xB3;

Servo thruster1;
Servo thruster2;
Servo thruster3;
Servo thruster4;
Servo thruster5;
Servo thruster6;

struct Input{
  uint8_t command;
  uint16_t value;
};

Input inputValue;
int packetIndex;

void processCommand() {
  switch(inputValue.command) {
    case 0x10:
      thruster1.writeMicroseconds(inputValue.value);
      Serial.print("FL: ");
    break;
    case 0x12:
      thruster2.writeMicroseconds(inputValue.value);
      Serial.print("FR: ");
    break;
    case 0x14:
      thruster3.writeMicroseconds(inputValue.value);
      Serial.print("BL: ");
    break;
    case 0x16:
      thruster4.writeMicroseconds(inputValue.value);
      Serial.print("BR: ");
    break;
    case 0x18:
      thruster5.writeMicroseconds(inputValue.value);
      Serial.print("SL: ");
    break;
    case 0x20:
      thruster6.writeMicroseconds(inputValue.value);
      Serial.print("SR: ");
    break;
  }

  Serial.println(inputValue.value);
}

void readInput() {
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

void resetReadInput() {
  packetIndex = 0;
  inputValue.value = 0;
}


void setup() {
  Serial.begin(9600);

  thruster1.attach(7);
  thruster2.attach(8);
  thruster3.attach(9);
  thruster4.attach(10);
  thruster5.attach(11);
  thruster6.attach(12);
  
  resetReadInput();

  Serial.println("Ready...");
}


void loop() {
  readInput();
}