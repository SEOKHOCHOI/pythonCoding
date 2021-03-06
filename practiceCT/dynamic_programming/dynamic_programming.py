'''
다이나믹 프로그래밍은 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법입니다.
이미 계산된 결과(작은 무게)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 합니다.
다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑다운과 보텀업)으로 구성됩니다.

다이나믹 프로그래밍은 동적 계획법이라고도 부릅니다.
일반적인 프로그래밍 분야에서의 동적(Dynamic)이란 어떤 의미를 가질까요?
  자료구조에서 동적 할당(Dynamic Allocotion)은 
  '프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'을 의미합니다.
  반면에 알고리즘에서 다이나믹 프로그래밍에서 '다이나믹'은 별다른 의미 없이 사용된 단어입니다.
'''
'''
다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용할 수 있습니다.
1. 최적 부분 구조(Optimal Substructure)
  큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있습니다.
2. 중복되는 부분 문제 (Overlapping Subproblem)
  동일한 작은 문제를 반복적으로 해결해야 합니다.

대표적인 문제로는 파보나치 수열이 있습니다.
프로그래밍에서는 이러한 수열을 배열이나 리스트를 이용해 표현합니다.
이러한 방법은 다이나믹 프로그래밍에서도 그대로 사용됩니다.
그래서 다이나믹 프로그래밍에서 각각의 계산된 결과를 담기 위해서 배열이나 리스트를 사용하고
별도로 테이블과 같은 공간에 값을 기록한다고 하여 배열이나 리스트를 테이블이라 부르기도 합니다.
'''
# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현


def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)


print(fibo(4))

'''
위처럼 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 됩니다. (중복되는 부분 문제 발생)
피보나치 수열의 시간 복잡도는 다음과 같습니다.
빅오 표기법:O(2^N)
빅오 표기법을 기준으로 f(30)을 계산하기 위해 약 10억가량의 연산을 수행해야 합니다.
'''

'''
피보나치 수열의 효울적인 해법: 다이나믹 프로그래밍
다이나믹 프로그래밍의 사용 조건을 만족하는지 확인합니다.
  1. 최적 부분 구조: 큰 문제를 작은 문제로 나눌 수 있습니다.
  2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결합니다.
피보나치 수열은 다이나믹 프로그래밍의 사용 조건을 만족합니다.
'''
'''
메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나입니다.
한 번 계산한 결과를 메모리 공간에 메모하는 기법입니다.
  같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옵니다.
  값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 합니다.
'''
'''
다이나믹 프로그램 구현방법

-탑다운(메모이제이션) 방식은 하향식이라고도 하며 보텀업 방식은 상향식이라고도 합니다.
-다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식입니다.
  결과 저장용 리스트는 DP 테이블이라고 부릅니다.
-엄밀히 말하면 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미합니다.
  따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아닙니다.
  한 번 게산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있습니다.

보텀업 방식에선 반복문 이용.
'''
# 피보나치 수열: 탑다운 다이나믹 프로그래밍 소스코드
# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)


def fibon(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibon(x - 1) + fibon(x - 2)
    return d[x]


print(fibon(99))


# 보텀업 방식
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화 동일
d2 = [0] * 100
# 보텀업에선 재귀함수가 아니라 반복문이 사용되기 때문에
# 종료조건 대신 점화식에서의 시작항에 대한 값들을 먼저 초기화 하면됩니다.
# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d2[1] = 1
d2[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현 (보텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d2[i] = d[i - 1] + d[i - 2]

print(d2[n])

# 메모이제이션을 이용하는 경우 피보나치 수열 함수의 시간 복잡도는 O(N)입니다.
d3 = [0] * 100


def fibo2(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d3[x] != 0:
        return d3[x]
    d3[x] = fibo2(x - 1) + fibo2(x - 2)
    return d3[x]


fibo2(6)
