import matplotlib.pyplot as plt # matplotlib모듈 임포트, pyplot--> plt로 변환 
import matplotlib.image as mpimg # matplotlib 모듈 임포트, mage--> mpimg로 변환
from PIL import Image # 이미지 라이브러리 임포트

import numpy as np # numpy 모듈 임포트

imsi6=mpimg.imread('_7_1_1.jpg') # jpg 파일 읽음, imsi6에 저장
imsi6=imsi6[:,:,0]  # 이미지 x,y값만 추출
imsi6_edge=np.where(imsi6>100) # 이미지 값에서 100이상인 값만 찾아서 저장


WC_x=np.mean(imsi6_edge[1]) # 이미지 x축의 평균을 구함, 손 중앙점 x
WC_y=np.mean(imsi6_edge[0]) # 이미지 y축의 평균을 구함, 손 중앙점 y

WC_x=round(WC_x,1)  # x축 평균 값을 소수점 1자리 남기고 반올림 
WC_y=round(WC_y+50,1) # y축 평균 값을 소수점 1자리 남기고 반올림, y좌표 +50해줌


x =imsi6_edge[1]-WC_x # 손 가장자리 x축 값에서 손 중앙점 x축 값 빼줌
y =imsi6_edge[0]-WC_y # 손 가장자리 y축 값에서 손 중앙점 y축 값 빼줌

distance=np.sqrt(np.square(x)+np.square(y))  # 거리 구하는 공식을 이용하여 손 가장자리 점들과 손 중심점의 거리를 구함

gakdo=np.arctan2(WC_x-imsi6_edge[1],WC_y-imsi6_edge[0]) #손 중앙점에서 손 가장자리에서 직선의 각도 구함
gakdo=np.rad2deg(gakdo)+180 # 손 중앙에서 각도의 기준축이 위쪽 방향으로 되어있어서 +180하여 기준축을 아래로 돌려줌
print(gakdo)

#plt.plot([WC_x,imsi6_edge[1][0]],[WC_y,imsi6_edge[0][0]]) # 기준축

plt.scatter(imsi6_edge[1],imsi6_edge[0], c='r', marker='o') # 손 윤곽 찍기
plt.scatter(WC_x,WC_y, c='y', marker='o') #중앙 찍기
plt.imshow(imsi6) # imsi6 출력

fig2 = plt.figure() # 그래프창 출력
plt.scatter(gakdo,distance) # 그래프
plt.show() # figure창 출력
