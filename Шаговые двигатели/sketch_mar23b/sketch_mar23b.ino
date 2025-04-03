
int IN3 = 5;
int IN4 = 6; 
int IN1 = 3;
int IN2 = 4;
void setup() {
  pinMode(IN2, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
}
void stop_(){
  
  digitalWrite(IN3,0 );
  digitalWrite(IN4, 0);
  digitalWrite(IN1,0);
  digitalWrite(IN2, 0); 
}
void forward(){
  digitalWrite(IN3,0 );
  digitalWrite(IN4, 1);
  digitalWrite(IN1,1);
  digitalWrite(IN2, 0);
}
void backward(){
  digitalWrite(IN3,1 );
  digitalWrite(IN4, 0);
  digitalWrite(IN1,0);
  digitalWrite(IN2, 1);
}
void right(){
  digitalWrite(IN3,0 );
  digitalWrite(IN4, 0);
  digitalWrite(IN1,1);
  digitalWrite(IN2, 0);
}
void left(){
  digitalWrite(IN3,0 );
  digitalWrite(IN4, 1);
  digitalWrite(IN1,0);
  digitalWrite(IN2, 0);
}
void  square(){
  forward();
  delay(2000);
  left();
  delay(1500);
  forward();
  delay(2000);
  left();
  delay(1500);
  forward();
  delay(2000);
  left();
  delay(1500);
  forward();
  delay(2000);
  stop_();
}
void loop() {
  square();
}