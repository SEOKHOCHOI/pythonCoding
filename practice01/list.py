# 리스트(list)
# 리스트는 또다른 자료형이다.
# 데이터 한 개가 아니라 여러개를 저장할 수 있는 자료형이라 보면된다.
# 사용이유는 각각의 변수에 하나씩 저장할때 사용.
# 리스트명 = [데이터, 데이터, ....]
# 데이터 접근방법: 인덱스로 접근, 0번 부터 시작.

# 빈 리스트 생성하기
listda = []

# 리스트 생성하기
animals = ["사자", "호랑이", "늑대", "강아지"]

# 데이터 접근하기 []안에 인덱스번호.
name = animals[0]
print(name)

# 데이터 추가하기(리스트의 마지막에 추가돼): 리스트.append(데이터)
animals.append("하마")
animals.append(1)

# 데이터 삭제하기(인덱스 번호적은곳 삭제): del 리스트[인덱스]
# [-1]은 마지막 데이터를 말한다.
del animals[-1]

# 리스트 슬라이싱(리스트를 범위로 가져오는것): 리스트[시작: 끝+1] ex-> 0:4면 0부터 3까지 가지고옴.
slicing = animals[1:3]
print(slicing)

# 리스트 길이(리스트 안에 데이터가 몇개인지 알려줘): len(리스트)
length = len(animals)
print(length)

# 리스트 정렬(알파벳, 한글, 숫자를 순서대로 위치를 맞춰줌, 오름차순으로 정렬): 리스트.sort()
animals.sort()
print(animals)
# 리스트 정렬에 옵션 reverse=True: 오름차순의 역순인 내림차순으로 정렬
animals.sort(reverse=True)
print(animals)

# 중복 확인
# in 이라는 연산자는
# test_list라는 리스트에
# 3이라는 데이터가 있는지 없는지 검사해줘.
# 포함되면 Ture, 되지 안흥면 False
test_list = [1, 2, 3, 4, 5]

if 3 in test_list:
    print("yes")

# not은 반대로 만들어주는 연산자
if 6 not in test_list:
    print("yes")
