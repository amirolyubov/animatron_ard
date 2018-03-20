#include <VAL.h>
#include <VarSpeedServo.h>


VarSpeedServo LEye;
VarSpeedServo REye;
VarSpeedServo LArm;
VarSpeedServo RArm;
VarSpeedServo Lhand;
VarSpeedServo Rhand;
VarSpeedServo LLeg;
VarSpeedServo RLeg;
VarSpeedServo Ass;

unsigned long start_time;
unsigned long start_time2;
unsigned long start_time3;
unsigned long start_time4;
unsigned long start_time5;
unsigned long start_time6;
unsigned long start_time7;
unsigned long start_time8;
unsigned long start_time9;
unsigned long currentMillis;
unsigned long start_timeMillis;
const long Interval = 20;


int Step = 0;

void setup()
{

  LEye.attach(9);
  REye.attach(8);
  LArm.attach(10);
  RArm.attach(7);
  Lhand.attach(6);
  Rhand.attach(3);
  LLeg.attach(4);
  RLeg.attach(5);
  Ass.attach(11);

LEye.write(0, 200, false);
REye.write(180, 200, false);
LArm.write(0, 200, false);
RArm.write(0, 200, false);
Lhand.write(0, 200, false);
Rhand.write(0, 200, false);
LLeg.write(180, 200, false);
RLeg.write(180, 200, false);

  Serial.begin(9600);

}

void loop()
{


  start_timeMillis = millis();

label:
  if (start_timeMillis >= KeyArray[Step])

  {
    currentMillis = millis();

    if (currentMillis - start_time >= Interval)
    {
      start_time = currentMillis;
      LEye.write(LEyeArray[Step], speed_row[Step], false);

    }

    currentMillis = millis();

    if (currentMillis - start_time2 >= Interval)
    {
      start_time2 = currentMillis;
      REye.write(REyeArray[Step], speed_row[Step], false);

    }


    currentMillis = millis();

    if (currentMillis - start_time3 >= Interval)
    {
      start_time3 = currentMillis;
      RArm.write(RArmArray[Step], speed_row[Step], false);

    }


    currentMillis = millis();

    if (currentMillis - start_time4 >= Interval)
    {
      start_time4 = currentMillis;
      LArm.write(LArmArray[Step], speed_row[Step], false);

    }

    currentMillis = millis();

    if (currentMillis - start_time5 >= Interval)
    {
      start_time5 = currentMillis;
      Lhand.write(LhandArray[Step], speed_row[Step], false);

    }

    currentMillis = millis();

    if (currentMillis - start_time6 >= Interval)
    {
      start_time6 = currentMillis;
      Rhand.write(RhandArray[Step], speed_row[Step], false);

    }

    currentMillis = millis();

    if (currentMillis - start_time7 >= Interval)
    {
      start_time7 = currentMillis;
      LLeg.write(LLegArray[Step], speed_row[Step], false);

    }

    currentMillis = millis();

    if (currentMillis - start_time8 >= Interval)
    {
      start_time8 = currentMillis;
      RLeg.write(RLegArray[Step], speed_row[Step], false);

    }

    currentMillis = millis();

    if (currentMillis - start_time9 >= Interval)
    {
      start_time9 = currentMillis;
      Ass.write(AssArray[Step], speed_row[Step], false);

    }

    if (start_timeMillis >= KeyArray[Step])
    {

      Step = Step + 1;
      Serial.println(start_timeMillis);
      goto label;
    }

  }


}
