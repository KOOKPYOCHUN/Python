import time #타임 모듈 임포트
import random #랜덤 모듈 임포트

t = time.time() #현재 시각

num_List=[]
num_List = random.sample(range(1,101),100)
print("#############랜덤 난수#############")
print(num_List)

#두 번째 값부터 시작, 그 앞의 값과 비교하여 삽입할 위치를 지정
#원소를 한칸 뒤로 옮기고 지정된 자리에 삽입

def  insertion_Sort(num): ##삽입정렬
    for i in range(len(num)): #리스트의 길이만큼 for문 돌림
        
        play = num[i] #리스트[i]값(위치값) play에 넣음
        key = i - 1 #i값의 -1값 만큼 key에 넣음 ex) i가 3이면 key=2,
        print(key)
        while key >= 0 and num[key] > play: # key 값이 0이상, i-1위치에 있는 값이 play에 들어있는 값보다 크면
            num[key + 1] = num[key] #i-1위치와 key + 1위치를 바꿈
            #print(num[key])
            key = key -1 # 값을 비교 하면서 최소값 될때까지 왼쪽으로 이동
        num[key + 1] = play
        #print(play)#
        #print(num)
    return num

print("#############Insertion  Sort#############")
insertion_Sort(num_List)
print(num_List)

elapsed = time.time() - t
print("정렬 시간:",elapsed)
