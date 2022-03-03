# 파이썬 이진 탐색 라이브러리
'''
bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환.
bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환.

예를들어 정렬된 1 2 4 4 8 리스트가 있다고 하면
bisect_left(a, 4)는 2와 4 사이에 인덱스 2로 들어가고
bisect_right(a, 4)는 4와 8 사이에 인덱스 4로 들어간다.
'''
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))


# 이러한 함수를 이용해서 값이 특정 범위에 속하는 데이터 개수를 구할 수 있다.
# from bisect import bisect_left, bisect_right는 위에 해줌

# 값이 [left_value, right_vlaue]인 데이터의 개수를 반환하는 함수
# 현재 리스트에 포함돼 있는 값들 중에 left_value와 right_value사이에 있는 값들의 갯수가 반환되는거임.
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    # 해당 값의 범위에 포함돼 있는 데이터의 갯수를 구한거임.
    return right_index - left_index


# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
# 4, 4의 의미는 left_value와 right_value의 값이 둘다 4라고 설정한것.
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 추력
print(count_by_range(a, -1, 3))


# 파라메트릭 서치 (Parametric Search)
'''
파라메트릭 서치란 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법.
  여기에서 최적화 문제란 어떤 함수의 값을 가능한 낮추거나 혹은 최대한 높이거나 등의 문제를 의미.
  그러한 문제를 바로 해결하기가 어려운 경우 그 문제를 여러번의 결정문제를 이용해서,
  문제 형태를 바꾸어 해결하는 경우가 존재하는데 그런 기법을 파라메트릭 서치라고 한다.
  
  ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제.
      탐색 범위를 좁혀가며 현재 범위에서는 이 조건을 만족하는지 체크를해서 그 여부에 따라서
      탐색 범위를 좁혀가며 가장 알맞은 값을 찾을 수 있는것.

그래서!     
일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용해 해결 가능.
'''
