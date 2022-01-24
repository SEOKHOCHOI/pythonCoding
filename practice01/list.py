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


# list 함수 !!!

# index(원소) : 리스트 내 특정한 원소의 인덱스를 찾는 함수
# + 존재하지 않는 원소 찾으려 하면 오류메시지
list1 = ['최석호', '나동빈', '유호익', '박우현', '박요한']
print(list1.index('박요한'))  # -> 박요한의 인덱스인 4 출력


# reverse() : 리스트의 원소를 뒤집기
'''
reverse함수의 경우 함수를 불러오자마자 자동으로 해당변수의 값이 바로 
뒤집혀지기 때문에 즉시 이용할 수 있고,
슬랑이싱 기법을 이용할때는 슬라이싱으로 변경된 리스트를 다시 
기존의 리스트에 담아 주어야 출력을 했을때 변경된 결과가 출력돼.
list = list[::-1]
print(list)
'''
list2 = [1, 2, 3]
list2.reverse()  # 슬라이싱과 다르게 list2 = list2.reverse() 해줄필용 없어
print(list2)  # -> [3, 2, 1] 출력
print(list2[::-1])  # -> 슬라이싱 기법도 이용가능! 다시 뒤집어 [1, 2, 3] 출력

list3 = [3, 4, 5]
list3[::-1]
print(list3)  # 이건 뒤집기 안된단 말이야 list3 = list3[::-1] 해줘야돼.


# sum(리스트 자료형) : 리스트의 모든 원소의 합이 구해짐
# + 숫자가 아닌 문자가 자료형으로 들어가면 오류메시지 출력. 실수자료형은 계산가능
print(sum(list3))  # -> 12 출력


# range(): 특정 범위를 지정, range(시작, 끝) 끝에서 -1한 값까지만 실제 수행범위.
# + 특정범위의 원소가 포함돼 있는 리스트를 즉시 만들 수 있다
# list(특정 범위) : 특정 범위의 원소를 가지는 리스트를 반환
# + list를 변수명으로 사용 후 list() 함수를 사용하려하면 오류 발생하니 주의
my_range = range(5, 10)  # -> 5부터 9까지
list4 = list(my_range)
print(list4)  # -> [5, 6, 7, 8, 9]  출력


# all() : 리스트의 모든 원소가 참인지 판별해주는 함수
# any() : 하나라도 참인지 판별해주는 함수
list5 = [True, False, True]
print(all(list5))  # -> False 하나 껴있으니 False 출력
print(any(list5))  # -> True 출력


# enumerate() : 리스트에서 인덱스와 함께 추출 (for문 안에서도 자주 사용)
list6 = ['최석호', '나동빈', '유호익', '박우현', '박우현']
result = list(enumerate(list6))
print(result)
# -> [(0, '최석호'), (1, '나동빈'), (2, '유호익'), (3, '박우현')]
# 이와같이 튜플 형태로 각각의 원소가 인덱스 및 값의 형태로 출력돼.
# for문 사용시 인덱스는 i에 원소값은 k에 담기게 돼.
for i, k in enumerate(list6):
    print("인덱스: ", i, " / 원소: ", k)  # 첫줄-> 인덱스 0 / 원소: 최석호 출력(나머지줄도 이렇게 출력)


# sort(): 리스트의 원소를 정렬할때 사용, 기본적으로는 오름차순, 바로밑에 sorted와 헷갈리지 마.
list6.sort()
print(list6)  # -> 사전순으로 오름차순 정렬돼 출력

# sorted(문자열 자료형) : 각 문자를 정렬하는 함수
'''
sorted()함수를 불러오게 되면 그 결과는 list 자료형이 돼.
'''
str8 = "helloworld"
list = sorted(str8)
print(list)  # -> ['d', 'e', 'h', ...] 이렇게 오름차순으로 출력
print(''.join(list))  # -> dehllloorw 출력 (정렬된게 하나의 문자열로 합쳐짐)
list = sorted(str, reverse=True)  # 내림차순 정렬시 reverse=True
print(''.join(list))  # -> roollledWH 출력


# count() : 특정한 원소의 개수를 추출
print(list6.count('박우현'))  # -> 2 출력


# del: 리스트의 특정 원소를 제거
list7 = ['123', '456', '789']
del list7[1]
print(list7)  # -> 1번 인덱스 '456' 제거된 ['123', '789'] 출력

list8 = ['123', '456', '789']
del list8[1:3]  # 1번 인덱스부터 2번 인덱스까지 제거
print(list8)  # -> ['123']  출력


# insert() : 리스트에 특정 원소를 삽입
# + insert(삽입할위치, 어떠한 원소를 삽입할지)
list9 = ['123', '456', '789', '00', '23']
list9.insert(3, '-1')  # 원래 인덱스 3 자리의 00을 뒤로 밀어내고 그 자리를 차지
print(list9)


# append(): 리스트의 가장 마지막 원소로서 원소를 삽입
list10 = ['123', '456', '789']
list10.append('1000')
print(list10)
