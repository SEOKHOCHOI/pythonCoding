#  for변수in리스트:
#       명령블록
#  for a in [1,2,3,4]:
#         print(a)
# 1
# 2
# 3
# 4
# 이렇게 출력돼. 즉, 리스트안의 요소들을 하나씩 뽑아내면서 명령블록을 실행한다.

names = ["티모", "리신", "이즈리얼"]

for name in names:
    if name == "티모":
        print(name + "는 팀 챔피언입니다.")
    elif name == "리신":
        print(name + "은 정글 챔피언입니다.")
    elif name == "이즈리얼":
        print(name + "은 원딜 챔피언 입니다.")

# 반복횟수 지정: range(10) 0~9까지 순서열을 반환. 순서열: 순서가 있는 데이터
# 정수를 입력 받아 순서열을 만들어 주는 함수= range()
for i in range(60):
    print(i+1, "분")

# range(1, 10) 1~9까지의 순서열이 나와.
# ragne(시작숫자, 끝숫자+1)
for i in range(1, 11):
    print(i, "번째 페이지입니다.")

# range(1, 10, 2) -> 1,3,5,7,9 이렇게 두칸씩 떨어진 순서열 나와.
# range(시작숫자, 끝숫자+1, 단계)
for i in range(1, 11, 2):
    print(i, "2칸씩 넘어가네?!")


# while
# 왜 for와 while 대체 가능한 두가지로 나눠 사용하지?
# 그때그때마다 편리한 문법이 다르니까!
# while 조건:
#       명령블록
for count in range(5):
    print(count, "번째 반복입니다")

count = 0
while count < 5:
    print(count, "번째 반복입니다")
    count = count+1

# for: 정한 횟수만큼 반복할때 사용.
# while: 어떤 조건이 만족하지 않을때까지 반복을 수행할때 자주 사용.
