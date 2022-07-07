char userInput;
#include "SparkFun_AS7265X.h" //Download library from https://github.com/sparkfun/SparkFun_AS7265x_Arduino_Library
AS7265X sensor;

#include <Wire.h>

void setup() {
  Serial.begin(9600);

  if(sensor.begin() == false)
  {
    Serial.println("Sensor does not appear to be connected. Please check wiring. Freezing...");
    while(1);
  }

  sensor.disableIndicator(); //Turn off the blue status LED

}

void loop() {
  if(Serial.available() > 0){
    
    userInput = Serial.read();

      if(userInput == 'g'){
        sensor.takeMeasurementsWithBulb(); //This is a hard wait while all 18 channels are measured

        Serial.print(sensor.getCalibratedA());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedB());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedC());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedD());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedE());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedF());
        Serial.print(" ");

        Serial.print(sensor.getCalibratedG());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedH());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedI());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedJ());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedK());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedL());
        Serial.print(" ");

        Serial.print(sensor.getCalibratedR());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedS());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedT());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedU());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedV());
        Serial.print(" ");
        Serial.print(sensor.getCalibratedW());
        Serial.print(" ");

        Serial.println();
      }
   }
   delay(50);
}
