int micPin = A0;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int val = analogRead(micPin);
    Serial.println(val);
    delay(5);  
}