#include <Servo.h>
Servo servomotor;
int data= digitalRead(2);
int a=0;
int c=0; // c 라는 변수로 if문이 계속 동작하는 걸 막은것 같다. (예전 코드라서 기억이 잘 안남..)
int mode=0;
void setup() {
  servomotor.attach(11);
  Serial.begin(9600); // 시리얼 통신 시작
  pinMode(2, INPUT); // 토글 스위치 연결 핀 : 2번
  pinMode(11, OUTPUT); // 서보모터 연결 핀 : 11번
  servomotor.write(10); // 서보모터 각도 조정
  delay(250);
  servomotor.detach(); //서보모터와의 연결 해지, 서보모터가 대기시에 소리가 나는 문제 해결


}

void loop() {
  data= digitalRead(2);
  
  
  if(data==0&&c==0){ // 스위치가 눌렸다면
    
    Serial.println(mode);
    servomotor.attach(11);
    servomotor.write(179); // 서보모터 동작
    c=1;
    delay(250);
    }
     
     
     
     
     
  
  else if(data==1&&c==1){ // 스위치가 꺼져있다면
    c=0;
    servomotor.write(10); // 서보모터 원래 위치로
    delay(250);
    servomotor.detach(); // 서보모터 연결 해지
  }
  //Serial.println(data);
  
}
