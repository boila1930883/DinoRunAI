int c1 = A0 ;
int c2 = A1 ;

String toPrint = "" ;

void setup() {
  // put your setup code here, to run once:
  Serial.begin (9600) ;
  pinMode (c1, INPUT) ;
  pinMode (c2, INPUT) ;
}

void loop() {
  // put your main code here, to run repeatedly:
  toPrint = String (String (analogRead (c1)) + "|" + String (analogRead (c2))) ;
  Serial.println (toPrint) ;
}
