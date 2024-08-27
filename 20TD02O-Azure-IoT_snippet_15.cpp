#include <Servo.h>

Servo myservo;  // Opprett en servomotorobjekt
int pos = 0;    // Variabel for servoposisjonen

void setup() {
  myservo.attach(9);  // Tilkoble servomotoren til pinne 9
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) { // Bevege seg fra 0 til 180 grader
    myservo.write(pos);              // Angi servoposisjonen
    delay(15);                       // Vent 15 ms
  }
  for (pos = 180; pos >= 0; pos -= 1) { // Bevege seg fra 180 til 0 grader
    myservo.write(pos);              // Angi servoposisjonen
    delay(15);                       // Vent 15 ms
  }
}