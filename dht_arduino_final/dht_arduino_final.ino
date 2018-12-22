#include <dht.h>
#define dht_apin 10
dht DHT;
#include <SoftwareSerial.h>
SoftwareSerial temp(8,9);//(RX,TX)

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(10,INPUT);
temp.begin(38400);
}

void loop() {
 
  //while (temp.available()){
  //  delay(10);
   // char bttemp=temp.read();
     
   //}
  // if (temp.available()){
      DHT.read11(dht_apin);
     //char a= temp.read();
     //Serial.println(a);
   //if (a=='h'){
    Serial.println(DHT.humidity);
    String time=Serial.readString();
    temp.print("Humidity is: ");
    temp.println(DHT.humidity);
     //}
     //else if (a=='t'){
     temp.print("Temperature is: ");
    temp.println(DHT.temperature);
    temp.print("Estimated time to reach set threshold: ");
    temp.print(time);
    temp.println(" seconds");
     //}
//}
delay(1200);
}
