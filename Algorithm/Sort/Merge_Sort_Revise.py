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
    
  mid = len(table1)//2
  left = table[:mid]
  right = table[mid:]

  left = merge_sort(left)
  right = merge_sort(right)

  return merge(left, right)

def merge(left, right):
  merged = []
  left_index, right_index = 0,0

  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      merged.append(left[left_index])
      left_index += 1

  else:
    merged.append(right[right_index])
    right_index += 1

  merged.extend(left[left_index:])
  merged.extend(right[right_index:])

  return merged

sorted = merge_sort(num_List)
print(sorted)
    
    
  



