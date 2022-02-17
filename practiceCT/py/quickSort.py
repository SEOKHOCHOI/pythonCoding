# 정렬 - 버블, 선택, 삽입, 병합, 퀵

# 가장 빠른건 퀵 정렬
# 나눠서 처리하는 정렬임
# [40, 35, 27] 정렬을 할때 40번 기준으로 한다면
# 40 뽑고 35, 27 두개가 남음
# 40보다 작으니 35 40 이렇게 배치함
# 그다음 27 35 40 이렇게 배치함
# 이런 순서로 배치됨.
# [40, 35, 27, 50, 75] 라면?
# 40뽑음 -> 35 40 -> 27 35 40 -> 27 35 40 50 -> 27 35 40 50 75
# 27 35 40 50 75 이렇게 오름차순 정렬됨.
# 어떤 한가지 숫자를 가지고 걔를 기준으로 양쪽 옆에 배열을 하면서 정렬을 하는것이 퀵정렬!

# 재귀를 이용해서 남은 애들을 계속 함수를 태웁니다.
numbers = [40, 35, 27, 75, 50]


def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [number for number in array[1:] if number <= pivot]
        greater = [number for number in array[1:] if number > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


result = quickSort(numbers)
print(result)
