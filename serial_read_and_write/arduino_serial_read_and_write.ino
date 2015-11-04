
String readString;
char c;

void setup()
{
  Serial.begin(9600);  // initialize serial communications at 9600 bp
}

void loop()
{
  while(!Serial.available()) {}
  
  // serial read section
    readString = ""; 
  while (Serial.available())
  {
    delay(30);
    if (Serial.available() > 0)
    {
      c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    }
  }

  if (readString.length() > 0)
  {
    Serial.print("Arduino received: ");  
    Serial.println(readString); //see what was received
  }

  delay(500);
 
  // serial write section
  char ard_sends = 'A';
  Serial.print("Arduino sends: ");
  Serial.println(ard_sends);
  Serial.print("\n");
  Serial.flush();
}
