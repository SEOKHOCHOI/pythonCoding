# 반복적으로 사용되는 코드를 재사용하기 위해 함수로 만든다.

'''
  함수 만드는 법

  def 함수이름(매개변수):
        명령블록
        ...
        return 리턴값
  dif는 디파인 정의하다의 약자.

  def sum(a,b):
        result = a+b
        return result
'''
# 함수 사용법


import random


def sum(a, b):
    result = a+b
    return result


x = sum(1, 2)
y = sum(3, 4)
print(x)
print(y)

# 1.매개변수가 없는 함수
'''
  def 함수이름():
      명령블록
      ...
      return 리턴값
      
  random.randint는 (1,10)1~10사이에 있는
  값 중 랜덤으로 뽑아 한개를 반환해주는 명령어.

  random을 파일안에 import random 해줘야 해.
'''


def getRandomNumber():
    number = random.randint(1, 10)
    return number


print(getRandomNumber())

# 2. 리턴값이 없는 함수
'''
  def 함수이름(매개변수):
      명령블록
'''


def printName(name):
    print(name)


printName('최석호')

# 3. 매개변수, 리턴값이 없는 함수
'''
  def 함수이름():
      명령블록
'''


def sayHi():
    print("안녕?")


sayHi()
