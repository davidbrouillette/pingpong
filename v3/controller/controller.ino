#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10,11);
int buttonState;
char btData;

int buttonPin = 4;
int ledPin = 5;

void setup() {
  BTSerial.begin(9600);
  Serial.begin(9600);

  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);

}

void loop() {
  if(BTSerial.available()){
    buttonState = digitalRead(buttonPin);
    btData = BTSerial.read();
    if(buttonState == HIGH){
      BTSerial.write('p');
    }
    if(btData && btData == 's'){
      digitalWrite(ledPin, HIGH);
    } else if (btData && btData == 'n'){
      digitalWrite(ledPin, LOW);
    }
  }
}
