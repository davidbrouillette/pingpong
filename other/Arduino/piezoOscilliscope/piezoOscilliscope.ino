
const int piezoPin = A0;
const int ledPin = 8;
bool ledOn = false;
unsigned long t0 = 0;
unsigned long t1;
unsigned long tDelay = 100;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int piezoADC = analogRead(piezoPin);
  float piezoV = piezoADC / 1023.0 * 5.0;
  Serial.print(-1);
  Serial.print(" ");
  Serial.print(1);

  Serial.print(" ");
  Serial.println(piezoV);
  if(piezoV > 0){
    if(t0 != 0 && !ledOn){
      t1 = millis();
        if(t1 - t0 >= tDelay){
          digitalWrite(ledPin, HIGH);
          ledOn = true;
        }
    } else if(t0 == 0){
      t0 = millis();
    }
    
  } else {
    if(t0 != 0 && ledOn){
      t1 = millis();
      if(t1 - t0 >= 1000){
        digitalWrite(ledPin, LOW);
        ledOn = false;
        t0 = 0;
      }
    }
  }

}
