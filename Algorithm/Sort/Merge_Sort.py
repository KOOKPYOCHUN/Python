import random #랜덤 모듈 임포트
import time #타임 모듈 임포트

t = time.time() #현재 시각
num_List=[]
num_List = random.sample(range(1,101),100)

print("######## 랜덤 난수 ########")
print(num_List)

#####################합병정렬######################

def  mergeSort(table1):
    
    if len(table1) <=1: #테이블 길이가 1이하이면 테이블값 리턴, 테이블 길이가 1이하면 정렬되어있다고 간주
        return table1 

    mid=len(table1)//2 # 테이블 길이 측정 하고 반으로 나눠서 mid에 넣음, ex) table 길이 100이면 50 넣음, table 길이 6이면 3넣음
    left=table1[:mid] # 처음부터 미드 값까지 왼쪽에 넣음
    right=table1[mid:] # 미드값 부터 끝값까지 오른쪽에 넣음
    #print(left)
    #print("")
    #print(right)
    #print("")
    pList=[] #빈 리스트 생성
    left1=mergeSort(left) #함수 처음으로 돌아가서 1이상 까지 반복 왼쪽에 있는걸 반으로 나눔
    right1=mergeSort(right) #오른쪽에 있는걸 반으로 나눔
    #print(left1)
    #print("")
    #print(right1)
    #print("")
    while len(left1)>0 and len(right1)>0:##왼쪽 오른쪽 비교함
        if left1[0]<right1[0]: #오른쪽이 더 크면 왼쪽꺼를 p리스트에 넣음
            pList.append(left1[0]) #
            del left1[0] #왼쪽에 넣은 값을 지워서 그 다음값을 0번째로 만듦
        else:
            pList.append(right1[0])
            del right1[0]
      
    while len(left1)>1: ##왼쪽끼리 비교
        if left1[0]<left1[1]: #왼쪽에 있는 0번째 값 1첫째 값 비교
            pList.append(left1[0]) #왼쪽이 작으면 p리스트에 넣음
            del left1[0] ##왼쪽에 넣은 값을 지워서 그 다음값을 0번째로 만듦
        else:
            pList.append(left1[1]) 
            del left1[1]

    if len(left1)==1: #리스트에 1만 남으면 p리스트에 넣음
        pList.append(left1[0])
        del left1[0]


    while len(right1)>1: ##오른쪽끼리 비교
        if right1[0]<right1[1]: 
            pList.append(right1[0])
            del right1[0]
        else:
            pList.append(right1[1])
            del right1[1]
            
    if len(right1)==1:
        pList.append(right1[0])
        del right1[0]

    return pList #p리스트값 리턴


print("############# Merge Sort #############")
sort=mergeSort(num_List)
print(sort)

elapsed = time.time() - t
print("정렬 시간:",elapsed)
