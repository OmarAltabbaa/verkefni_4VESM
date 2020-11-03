

// analog pin 0
#define PHOTOCELL_PIN A0

// photocell state
int current = 0;
int last = -1;



void setup() {
 
  // start the serial connection
  Serial.begin(115200);
 
 
}

void loop() {
  
  // grab the current state of the photocell
  current = analogRead(PHOTOCELL_PIN);
 
  // return if the value hasn't changed
  if(current == last)
    return;

  Serial.println(current);
  last = current;
  // wait one second (1000 milliseconds == 1 second)
  delay(1000);
 
}
