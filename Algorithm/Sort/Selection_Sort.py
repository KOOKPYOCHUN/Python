def selection_sort(table):
  num = len(table)
  for i in range(num):
    min_index = i #현재 인덱스 최소값으로 설정

    for j in range(i + 1, num): #현재 인덱스 후 모든 요소와 비교, 최소값 찾음
      if table[j] < table[min_index]:
        min_index = j

    table[i], table[min_index] = table[min_index], table[i] # 최소값과 현재 인덱스 값을 교환하여 정렬
