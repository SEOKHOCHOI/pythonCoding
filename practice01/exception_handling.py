# 예외처리
# 특정한 구문에 있어 오류가 발생할때 이를 정상적으로 체크할 수 있음
# 기본적으로 try:   except: 구문을 이용할 수 있음
# try: 여기서 어떠한 내용을 실행, 그 사이에 오류가 발생시,
# except: 구문이 실행됨.
# else: 예외가 발생하지 않은 경우 추가적으로 덧붙여서 예외가 발생하지 않았다 해줄수있음.
# finally: 예외가 발생했는지 발생하지 않았는지 여부와 상관없이 무조건 실행되도록 만드는 명령어 구문.
try:
    print(3 / 0)
except:
    print("0으로는 나눌 수 없습니다.")
else:
    print("예외 없이 성공적으로 실행되었습니다.")
finally:
    print("예외 처리를 마칩니다.")

try:
    print(3 / 2)
except:
    print("0으로는 나눌 수 없습니다.")
else:
    print("예외 없이 성공적으로 실행되었습니다.")
finally:
    print("예외 처리를 마칩니다.")


# 프로그램이 실행되고 있을때 오류 메시지를 직접 출력하고자 한다면
# exception 관련 객체를 이용하자. 파이썬이 기본적으로 제공해주고 있는 객체다
# 실제로 어떠한 오류가 발생했는지가 e라는 변수에 담기게 돼 출력돼
try:
    print(3 / 0)
except Exception as e:
    print(e)
