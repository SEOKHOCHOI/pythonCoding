# input(), int(), float()
'''
# input() : 사용자로부터 콘솔로 입력을 받는 함수
기본적으로 입력을 받은 내용은 문자열로 처리가 됨.
정수형식으로 바꾸기 위해서는 int() 함수를 추가적으로 함께 사용.

# int() :  정수 자료형으로 변환
a = 12.5
print(int(a))  -> 12 출력 

# float() : 문자열, 정수 등의 자료형을 실수형으로 변환
b = 10
print(float(b)) -> 10.0 출력
'''
user_input = input('정수를 입력하세요: ')
print("제곱: ", int(user_input) ** 2)


# max(), min()
'''
# max(), min() : 시퀀스 자료형에 포함되어 있는 원소 중 최대값 혹은 최소값을 구하는 함수.
'''
list = [5, 6, 3, 2, 9, 8, 4, 1, 7]
print(max(list))
print(min(list))


# bin(), hex()
'''
# bin() : 10진수 -> 2진수 변환
# hex() : 10진수 -> 16진수
이때 반환값은 문자열 이라는 특징이 있다.
# int로 10진수 변환 가능.
int('문자열들어가', 기존의 진수)
'''
print(bin(128))  # -> 0b10000000 출력, b는 바이너리의 약자로써 2진수 라는걸 알려주는 것.
print(hex(230))  # -> 0xe6
print(int('0xe6', 16))  # 16진수 -> 10진수

# round()
'''
# round() : 반올림을 수행하는 함수
print(round(반올림할 수, 소수점 몇째자리에서 반올림할지 정하는 수 기본값은 0))
'''
print(round(123.789))  # 124 출력
print(round(123.789, 2))  # 0,1,2 니까 소수점 이하 3번째 자리인 9에서 반올림 수행 -> 123.79 출력
print(round(123.789, -1))  # -> 소숫점 이상 몇번째 자리에서 반올림 수행할지, 120.0 출력


# type()
'''
# type() : 자료형의 종류를 알려줌.
'''
int = 1
str = "문자열"
list = [1, 2, 3]
dict = {'apple': '사과'}
print(type(int))   # ->  <class 'int'> 출력
print(type(str))   # ->  <class 'str'> 출력
print(type(list))  # ->  <class 'list'> 출력
print(type(dict))  # ->  <class 'dict'> 출력
