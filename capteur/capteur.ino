#include <Servo.h>

Servo servo ;
String str = "\n" ;
int c1 = A0 ;
int c2 = A1 ;

String toPrint = "" ;

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600) ;
  pinMode (c1, INPUT) ;
  pinMode (c2, INPUT) ;

  servo.attach (7) ;
  servo.write (30) ;
}

void loop() {
  // put your main code here, to run repeatedly:
  toPrint = String (String (analogRead (c1)) + "|" + String (analogRead (c2))) ;
  Serial.println (toPrint) ;

  if (Serial.available () > 0) {
      pressSpace () ;
      while (Serial.available ()>0) {
        Serial.read () ;
    }
  }
}

void pressSpace () {
  for (int i = 0 ; i < 30 ; i ++) {
    servo.write (30-i) ;
  }
  
  delay (100) ;
  servo.write (30) ;
  delay (100) ;   
}
