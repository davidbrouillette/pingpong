/*
  DigitalReadSerial
 Reads a digital input on pin 2, prints the result to the serial monitor 
 
 This example code is in the public domain.
 */


#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 

// digital pin 2 has a pushbutton attached to it. Give it a name:
int pushButton = 8;
int stayOpenButton = 10;
int servoControlPin = 3;
int val = 0;

// the setup routine runs once when you press reset:
void setup() {
  myservo.attach(servoControlPin);  // attaches the servo on pin 9 to the servo object 
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
  pinMode(pushButton, INPUT);
  pinMode(stayOpenButton, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input pin:
  int pushButtonState = digitalRead(pushButton);
  // print out the state of the button:
  if(stayOpenButton == HIGH && val!= 180){
    val = 180;
    myservo.write(val);
  } else{
    if(pushButtonState == LOW && val != 20){
      val = 20;
      myservo.write(val);
      delay(100);        // delay in between reads for stability
    } else if (pushButtonState == HIGH && val != 175) {
      val = 175;
      myservo.write(val);
      delay(100);        // delay in between reads for stability
    }
  }
  Serial.println(buttonState);

}



