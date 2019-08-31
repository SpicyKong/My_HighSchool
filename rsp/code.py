import numpy as np
import cv2
import serial
arduino = serial.Serial('COM3', 9600) # 아두이노와 연결할 시리얼 포트를 선택해 줍니다.
x1,x2,y1,y2,end=0,0,0,0,False

def mouse_callback(event, x, y, flags, param): # 영상속에서 이미지 영역을 선택하기 위한 함수 입니다.
    global x1,x2,y1,y2,end
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x,y
    if event == cv2.EVENT_LBUTTONUP:
        x2, y2 = x,y
        end = True
def tracking():
    try:
        print("start")
        cap = cv2.VideoCapture(1) # 노트북에는 기본 내장 캠이 있기 때문에 다른 내장 캠을 사용하려면 적절히 숫자를 입력해줍니다.
        cap.set(cv2.CAP_PROP_BRIGHTNESS, 230)
        cap.set(cv2.CAP_PROP_HUE, 230)
    except:
        print("stop")
        return
    while True:
        ret, frame = cap.read() # 캠의 영상을 받아옵니다.
        cv2.imshow('roi', frame)
        cv2.namedWindow('roi')
        cv2.setMouseCallback('roi', mouse_callback) # 마우스로 영역을 설정합니다.
        k = cv2.waitKey(1) & 0xFF
        if k == 27: # esc를 누르면 종료가 됩니다.
            break
    print(x1)
    cv2.destroyAllWindows()
    while True:
        ret, frame1 = cap.read() 캠의 영상을 받아옵니다.

        frame = frame1[y1:y2,x1:x2] # 그후 아까 선택했던 영역의 영상만 슬라이싱 합니다.

        
        #print(frame.shape)
        kernel = np.ones((3, 3), np.float32)

        blur = cv2.GaussianBlur(frame, (5,5), 0)

        blur1 = cv2.dilate(blur, kernel, iterations = 3) # 모폴로지 기법 , 침식
        blur1 = cv2.erode(blur1, kernel, iterations = 5) # 팽창

        blur2 = cv2.erode(blur, kernel, iterations = 35)
        blur2 = cv2.dilate(blur2, kernel, iterations = 40)

        #YCrCb 변환
        ycrcb1 = cv2.cvtColor(blur1,cv2.COLOR_BGR2YCrCb)
        ycrcb2 = cv2.cvtColor(blur2,cv2.COLOR_BGR2YCrCb)

        #Cr:133~173, Cb:77~127
        mask_1 = cv2.inRange(ycrcb1,np.array([0,115,70]),np.array([255,185,140])) # 살색만 추출합니다.
        mask_2 = cv2.inRange(ycrcb2,np.array([0,115,70]),np.array([255,185,140]))

        hsv1 = cv2.cvtColor(blur1, cv2.COLOR_BGR2HSV)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

        res1 = cv2.bitwise_and(frame, frame, mask=mask_1) # and연산
        res1 = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
        _, thr1 = cv2.threshold(res1, 40, 255, cv2.THRESH_BINARY)

        res2 = cv2.bitwise_and(frame, frame, mask=mask_2)
        res2 = cv2.cvtColor(res2, cv2.COLOR_BGR2GRAY)
        _, thr2 = cv2.threshold(res2, 40, 255, cv2.THRESH_BINARY_INV)

        res = cv2.bitwise_and(thr1, thr2)

        blur3 = cv2.erode(res, kernel, iterations = 3)
        blur3 = cv2.dilate(blur3, kernel, iterations = 2)

        con = cv2.findContours(blur3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0] # 처음 손가락 개수를 구합니다.
        size_finger = sum([cv2.contourArea(con[a]) for a in range(len(con))]) # 전체 면적을 구합니다
        finger_num = len([cv2.contourArea(con[a]) for a in range(len(con)) if cv2.contourArea(con[a]) > size_finger/16]) # 흰부분이 일정 크기보다 작다면 손가락 개수를 -1 합니다 
        #print(finger_num)
        con1 = cv2.findContours(thr1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
        size_hand = sum([cv2.contourArea(con1[a]) for a in range(len(con1))])

        
        #print(finger_num)
        cv2.imshow('org', blur3)
        cv2.imshow('org1', frame1)
        cv2.imshow('roi', frame)
        if finger_num:
            if size_hand/14 > size_finger:
                arduino.write(b'p') # 주먹: 아두이노와 시리얼 통신을 하는 코드입니다.
                #print("p")
            elif 0<=finger_num<=1:
                arduino.write(b'p') # 주먹
                #print("p")
            elif 1<finger_num<=3:
                arduino.write(b'r') # 가위
                #print("r")
            else:
                arduino.write(b's') # 보자기
                #print("s")
        
        #if finger_num:
        #    if size_hand/14 > size_finger:
        #        print("주먹")
        #    elif 0<=finger_num<=1:
        #        print("주먹")
        #    elif 1<finger_num<=3:
        #        print("가위")
        #    else:
        #        print("보자기")
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    
    cv2.destroyAllWindows()
    


    


tracking()
