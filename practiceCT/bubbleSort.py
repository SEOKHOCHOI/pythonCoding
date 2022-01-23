# 버블 정렬(Bubble Sort)
# 거품이 물에서 떠오르는 모양처럼 숫자가 정렬돼.
# 알고리즘에서 가장 첫번째로 나오는 알고리즘

# 핵심로직
'''
  첫번째꺼랑 두번째꺼랑 비교해서 두번째께 더 작으면
  첫번째꺼랑 자리를 바꾼다.
  보통 n, n+1 이런식으로 표기를 많이함.
'''

# 0번째와 나머지를 모두 비교를 한다. 1바퀴
# 가장 작은게 0번째에 온다.
# 그 다음으로 작은게 1번째에 오게 해야 한다.
numbers = [7, 3, 2, 9, 4]


def bubbleSort(arr):
    for front_index in range(0, len(arr) - 1):
        for index in range(front_index + 1, len(arr)):
            if arr[front_index] > arr[index]:
                temp = arr[front_index]
                arr[front_index] = arr[index]
                arr[index] = temp
    return arr


result = bubbleSort(numbers)
print(result)
