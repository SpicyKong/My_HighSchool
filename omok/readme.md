# 프로그램 작동 영상


[![Video Label](http://img.youtube.com/vi/P7MU_o5z-Ac/0.jpg/0.jpg)](https://youtu.be/P7MU_o5z-Ac)
<!--
# #step 1. 영상을 이진화 합니다.
> <div>
  <img src="https://github.com/SpicyKong/My_HighSchool/blob/master/rsp/%EA%B7%B8%EB%A6%BC1.png" width="30%"></img>
  <img src="https://github.com/SpicyKong/My_HighSchool/blob/master/rsp/%EA%B7%B8%EB%A6%BC2.png" width="30%"></img>
  </div>
YCrCb 색체계를 이용해 살색만 추출해 영상을 이진화하고 복사본을 하나 만듭니다. (OpenCv에서 사용하는 BGR 색공간 보다는 YCrCb 색공간이 피부색 추출에 더욱 적합하다고 합니다.)

피부색 영역 Cb : 77~127, Cr : 133 ~ 173
# #step 2. 이진화된 영상을 모폴로지 변환을 합니다.
> <div>
  <img src="https://github.com/SpicyKong/My_HighSchool/blob/master/rsp/%EA%B7%B8%EB%A6%BC3.png" width="30%"></img>
  </div>
2번 이미지를 복사합니다. 그후 모폴로지 기법처럼 침식과 팽창을 반복합니다. 단, 침식값을 좀더 크게 주어야합니다.(저는 약 1.15배를 주었습니다.) 그러면 위와 같이 손가락이 사라진 영상을 얻을수 있습니다.


# #step 3. 2번이미지와 3번이미지를 더합니다.
> <div>
  <img src="https://github.com/SpicyKong/My_HighSchool/blob/master/rsp/%EA%B7%B8%EB%A6%BC4.png" width="30%"></img>
  </div>
2번이미지와 3번이미지를 합치면 위와 같이 손가락만 남게 되는것을 볼수있습니다. 그후 findContours()함수를 이용해 손가락의 개수를 셉니다. 하지만 위와 같은 이미지 파일과 다르게 실제로 캠을 통해 받아 오는 영상은 잡음이 좀 있을수도 있기에 이 부분은 따로 처리 해주어야 합니다.

저는 이미지의 흰색부분의 면적을 구한후 면적과 비례하는 임계값을 정하고 입계값보다 작은 흰 면적은 무시해 주는 방법을 사용했습니다.
-->
