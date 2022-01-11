'''
  1. 로또 번호 6개를 생성
  2. 로또 번호는 1~45까지의 랜덤한 번호
  3. 6개의 숫자 모두 달라야 한다.
  4. 로또 번호 생성함수를 작성하고 사용한다.
'''

# 나의 답안 (중복 체크 실패)
import random

lotto_num = []


def lotto():
    for i in range(1, 7):
        number = random.randint(1, 45)
        i = number
        lotto_num.append(i)
    return lotto_num


print(lotto())

# 나의 답안 수정
lotto_num2 = []


def lotto2():
    number2 = random.randint(1, 45)
    return number2


count = 0
while True:
    if count > 5:
        break
    random_num = lotto2()
    if random_num not in lotto_num2:
        lotto_num2.append(random_num)
    count += count


print(lotto_num2)
# 다른사람 답안(중복처리 안돼서 틀림)


def getRandomNumber():
    number = random.randint(1, 45)
    return number


for i in range(6):  # 0, 1, 2, 3, 4, 5 (솔직히 이게 몇번 반복될지 모름.7~8번 될수도)
    random_number = getRandomNumber()
    print(random_number)

# 다른사람 답안02
lotto_num = []  # 빈 로또 번호 리스트 생성


def getRandomNumber():
    number = random.randint(1, 45)
    return number


count = 0  # 횟수를 저장할 변수
while True:
    if count > 5:
        break
    random_number = getRandomNumber()  # 로또 번호 하나를 뽑는다.
    if random_number not in lotto_num:  # 로또 번호 리스트 안에 뽑은 로또 번호가 없으면
        lotto_num.append(random_number)  # 로또 번호 리스트에 뽑은 로또 번호를 추가해라.
        count = count + 1
print(lotto_num)
