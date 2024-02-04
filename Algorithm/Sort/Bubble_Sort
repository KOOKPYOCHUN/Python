import time #타임 모듈 임포트
import random #랜덤 모듈 임포트

t = time.time() #현재 시각

num_List=[]
num_List = random.sample(range(1,101),100)
print("#############랜덤 난수#############")
print(num_List)


def bubble_sort(list):
    length = len(list)-1 #리스트 길이에서 -1값 만큼 넣음, 비교 횟수 = List 길이 -1
    for i in range(length): #리스트에서 -1 값만큼 for문을 돌림
        for j in range(length-i): #
            if list[j] > list[j+1]: #
                list[j], list[j+1] = list[j+1], list[j]
            
# 버블정렬= 큰 값을 계속 오른쪽으로 뺌
# 정렬을 하다가 제일 큰 값이 오른쪽에 쌓이면 그 값 고정
# j위치 값과 j+1위치값을 비교 j값이 더 크면 j값과 j+1값을 바꿈
print("#############Bubble Sort#############")
bubble_sort(num_List)
print(num_List)

elapsed = time.time() - t
print("정렬 시간:",elapsed)
