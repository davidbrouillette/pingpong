
int pinA = 2;
int pinB = 3;
int pinC = 4;
int pinD = 5;
int pinE = 6;
int pinF = 7;
int pinG = 8;
int D1 = 9;
int D2 = 10;
int D3 = 11;
int D4 = 12;

int num_array[10][7] = {  { 1,1,1,1,1,1,0 },    // 0
                          { 0,1,1,0,0,0,0 },    // 1
                          { 1,1,0,1,1,0,1 },    // 2
                          { 1,1,1,1,0,0,1 },    // 3
                          { 0,1,1,0,0,1,1 },    // 4
                          { 1,0,1,1,0,1,1 },    // 5
                          { 1,0,1,1,1,1,1 },    // 6
                          { 1,1,1,0,0,0,0 },    // 7
                          { 1,1,1,1,1,1,1 },    // 8
                          { 1,1,1,0,0,1,1 }};   // 9


void TurnOn(int digitPin){
  digitalWrite(digitPin, LOW);
}

void TurnOff(int digitPin){
  digitalWrite(digitPin, HIGH);
}

void setup() {
  pinMode(pinA , OUTPUT);
  pinMode(pinB , OUTPUT);
  pinMode(pinC , OUTPUT);
  pinMode(pinD , OUTPUT);
  pinMode(pinE , OUTPUT);
  pinMode(pinF , OUTPUT);
  pinMode(pinG , OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
//
//  digitalWrite(D1, HIGH);
//  digitalWrite(D2, HIGH);
//  digitalWrite(D3, LOW);
//  digitalWrite(D4, HIGH);
//  displayNumber(3);
//  
//  digitalWrite(D1, HIGH);
//  digitalWrite(D2, HIGH);
//  digitalWrite(D3, HIGH);
//  digitalWrite(D4, LOW);
//  displayNumber(5);
}

void loop() {
//
//  TurnOff(D1);
//  TurnOff(D2);
//  TurnOff(D3);
//  TurnOff(D4);

//  for(int count = 19; count > 0; --count){
////    boolean ones = ((count - 1)%10);
////    boolean tens = (((count - 1)/10)%10);
////    boolean hundreds = (((count - 1)/100)%10);
//
//    int tens = floor((count-1) / 10);
//    int ones = (count - 1) - tens;
//
//    
//    
//    delay(1000);
//  //}
//  delay(3000);

  //1
  digitalWrite(D1, LOW);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, LOW);
  digitalWrite(D4, LOW);
  digitalWrite(pinA, LOW);
  digitalWrite(pinB, HIGH);
  digitalWrite(pinC, HIGH);
  digitalWrite(pinD, LOW);
  digitalWrite(pinE, LOW);
  digitalWrite(pinF, LOW);
  digitalWrite(pinG, LOW);

  digitalWrite(D1, HIGH);
  digitalWrite(D2, LOW);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(pinA, HIGH);
  digitalWrite(pinB, HIGH);
  digitalWrite(pinC, HIGH);
  digitalWrite(pinD, LOW);
  digitalWrite(pinE, LOW);
  digitalWrite(pinF, LOW);
  digitalWrite(pinG, LOW);

  delay(1000);
//
//  // 4
////  digitalWrite(D1, HIGH);
////  digitalWrite(D2, HIGH);
////  digitalWrite(D3, HIGH);
////  digitalWrite(D4, LOW);
//  digitalWrite(pinA, LOW);
//  digitalWrite(pinB, HIGH);
//  digitalWrite(pinC, HIGH);
//  digitalWrite(pinD, LOW);
//  digitalWrite(pinE, LOW);
//  digitalWrite(pinF, HIGH);
//  digitalWrite(pinG, HIGH);
//
//  delay(1000);
}

void displayNumber(int number){
  
  
  int pin = 2;
  for(int i = 0; i < 7; i++){
    digitalWrite(pin, num_array[number][i]);
    pin++;     
  }
}
