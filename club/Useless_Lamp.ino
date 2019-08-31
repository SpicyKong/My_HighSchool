#include <Adafruit_NeoPixel.h>              // 네오픽셀 라이브러리를 불러옵니다.
#include <MD_TCS230.h> 
#include <FreqCount.h>

#define PIN 0                                   // 디지털핀 어디에 연결했는지 입력
#define LEDNUM 1                                // 연결된 네오픽셀의 숫자입력
#define  S2_OUT  12 
#define  S3_OUT  11 
#define  LED     13

Adafruit_NeoPixel strip1 = Adafruit_NeoPixel(LEDNUM, 4, NEO_GRB + NEO_KHZ800);
MD_TCS230 CS(S2_OUT, S3_OUT, /* S0_OUT, S1_OUT, */ LED);
sensorData sdBlack = { 120, 70, 80 };
sensorData sdWhite = { 4110, 3270, 3290 };
colorData rgb;

void setup() {
  
   
  Serial.begin(115200); 
 
  // 컬러 센서 초기화: begin() 함수를 이용하여 초기화를 하고, 
  // 영점 조정을 위한 검정색과 흰색 값을 설정합니다  
  CS.begin(); 
  CS.setDarkCal(&sdBlack); 
  CS.setWhiteCal(&sdWhite);
  strip1.begin();  
}

void loop() {
  CS.read(); 
   
  // 읽어들일 데이터가 준비될 때까지 기다립니다 
  while(!CS.available()) ; 
   
  // RGB 데이터 값을 읽어 들입니다 
  CS.getRGB(&rgb); 
   
  // 쉼표로 분리된 값으로 출력합니다 
  
  Serial.print(rgb.value[TCS230_RGB_R]); 
  Serial.print(","); 
  Serial.print(rgb.value[TCS230_RGB_G]); 
  Serial.print(","); 
  Serial.println(rgb.value[TCS230_RGB_B]); 
   
  // 잠시 기다렸다가 다시 시작합니다
strip1.setPixelColor(0,rgb.value[TCS230_RGB_R],rgb.value[TCS230_RGB_G],rgb.value[TCS230_RGB_B]);
strip1.show();
delay(1);
}
