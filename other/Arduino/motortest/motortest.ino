
#define BLYNK_PRINT Serial

#include <MotorDriver.h>
#include <SoftwareSerial.h>
SoftwareSerial SwSerial(10, 11); // RX, TX
    
#include <BlynkSimpleSerialBLE.h>
#include <SoftwareSerial.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "e0be073c3da248769a265193f3b7c85a";

SoftwareSerial SerialBLE(14, 15); // RX, TX

MotorDriver m;
int LeftMotorSpeed = 0;
int RightMotorSpeed = 0;

// This function will be called every time Slider Widget
// in Blynk app writes values to the Virtual Pin V1
BLYNK_WRITE(V1)
{
  int pinValue = param.asInt(); // assigning incoming value from pin V1 to a variable
  Serial.println(pinValue);
  // process received value
}

BLYNK_WRITE(V2) {
  int x = param[0].asInt();
  int y = param[1].asInt();
  LeftMotorSpeed = x;
  RightMotorSpeed = y;
  if(x == 128 && y == 128){
    m.motor(3,RELEASE,0);
    m.motor(4,RELEASE,0);
  } else {
    m.motor(3,BACKWARD,x);
    m.motor(4,FORWARD,y);
  }
  // Do something with x and y
  Serial.print("X = ");
  Serial.print(x);
  Serial.print("; Y = ");
  Serial.println(y);
}


void setup()
{
  // Debug console
  Serial.begin(9600);

  SerialBLE.begin(9600);
  Blynk.begin(SerialBLE, auth);

  Serial.println("Waiting for connections...");
}

void loop()
{
  Blynk.run();
}
